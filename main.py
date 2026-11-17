#!/usr/bin/env python3
"""Static checks for common systemd service unit configuration issues."""
import argparse
import configparser
import json
from pathlib import Path

def lint(text):
    parser = configparser.ConfigParser(interpolation=None, strict=False, delimiters=("=",), comment_prefixes=("#", ";"), allow_no_value=True)
    parser.optionxform = str
    issues = []
    try:
        parser.read_string(text)
    except configparser.Error as exc:
        return [{"level":"error","code":"parse-error","message":str(exc)}]
    def value(section, key, default=""):
        return parser.get(section, key, fallback=default).strip() if parser.has_section(section) else default
    if not parser.has_section("Unit"):
        issues.append({"level":"warning","code":"missing-unit-section","message":"No [Unit] section was found."})
    elif not value("Unit", "Description"):
        issues.append({"level":"warning","code":"missing-description","message":"Add a Description= value to [Unit]."})
    if not parser.has_section("Service"):
        issues.append({"level":"error","code":"missing-service-section","message":"A service unit needs a [Service] section."})
        return issues
    if not value("Service", "ExecStart"):
        issues.append({"level":"error","code":"missing-execstart","message":"No ExecStart= command was found in [Service]."})
    user = value("Service", "User")
    if not user:
        issues.append({"level":"warning","code":"implicit-user","message":"No User= is set; a system service may run with elevated privileges."})
    elif user == "root":
        issues.append({"level":"warning","code":"root-user","message":"User=root is explicit; check whether the service really needs full privileges."})
    checks = [
        ("NoNewPrivileges","yes","missing-no-new-privileges","Consider NoNewPrivileges=yes."),
        ("PrivateTmp","yes","missing-private-tmp","Consider PrivateTmp=yes to isolate temporary directories."),
        ("ProtectSystem","strict","weak-protect-system","Consider an appropriate ProtectSystem= setting."),
        ("ProtectHome","yes","missing-protect-home","Consider ProtectHome=yes or a narrower setting."),
    ]
    for key, expected, code, message in checks:
        actual = value("Service", key).lower()
        if not actual:
            issues.append({"level":"warning","code":code,"message":message})
    exec_start = value("Service", "ExecStart")
    if exec_start.startswith(("/bin/sh -c", "/bin/bash -c")):
        issues.append({"level":"warning","code":"shell-wrapper","message":"ExecStart uses a shell wrapper; prefer a direct executable when practical."})
    if not value("Service", "Restart") and value("Service", "Type", "simple") != "oneshot":
        issues.append({"level":"info","code":"no-restart-policy","message":"No Restart= policy is set for this service."})
    if parser.has_section("Install") and not value("Install", "WantedBy"):
        issues.append({"level":"info","code":"no-wantedby","message":"No WantedBy= target is configured in [Install]."})
    return issues

def main():
    cli = argparse.ArgumentParser(description="Statically inspect a systemd .service file; this is not a security certification.")
    cli.add_argument("file", help="path to a systemd service unit")
    cli.add_argument("--json", action="store_true", help="print findings as JSON")
    args = cli.parse_args()
    path = Path(args.file)
    try:
        findings = lint(path.read_text(encoding="utf-8"))
    except OSError as exc:
        cli.error(str(exc))
    if args.json:
        print(json.dumps({"file":str(path),"findings":findings},indent=2))
    else:
        print("SYSTEMD UNIT LINT")
        print("=" * 48)
        print("File: " + str(path))
        if not findings:
            print("No findings from the included checks.")
        for item in findings:
            print("[{0}] {1}: {2}".format(item["level"].upper(),item["code"],item["message"]))
        print("\nStatic checks only. Review the unit and your system's threat model.")
    return 1 if any(item["level"]=="error" for item in findings) else 0

if __name__ == "__main__":
    raise SystemExit(main())
