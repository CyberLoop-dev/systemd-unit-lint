<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:0f766e&height=180&section=header&text=systemd%20Unit%20Lint&fontSize=38&fontColor=ffffff&animation=fadeIn" width="100%" alt="systemd Unit Lint banner" />
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&duration=2800&pause=900&color=2DD4BF&center=true&vCenter=true&width=760&lines=Review%20systemd%20service%20files%20for%20common%20configuration%20gaps." alt="Review systemd service files for common configuration gaps." />
<img src="assets/icon.svg" width="116" alt="systemd Unit Lint icon" />

[![License](https://img.shields.io/github/license/CyberLoop-dev/systemd-unit-lint?style=for-the-badge)](LICENSE)
[![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/systemd-unit-lint?style=for-the-badge)](https://github.com/CyberLoop-dev/systemd-unit-lint)
[![Stars](https://img.shields.io/github/stars/CyberLoop-dev/systemd-unit-lint?style=for-the-badge)](https://github.com/CyberLoop-dev/systemd-unit-lint/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/systemd-unit-lint?style=for-the-badge)](https://github.com/CyberLoop-dev/systemd-unit-lint/commits/main)

**Review systemd service files for common configuration gaps.**

</div>

## 🧭 Overview

systemd Unit Lint is a small, local-first utility. Review systemd service files for common configuration gaps. It runs on your machine and does not require an account or hosted service.

## ✨ Features

- ✨ Check for missing service sections and ExecStart directives.
- ✨ Flag implicit or explicit root execution for review.
- ✨ Highlight missing common service hardening options.
- ✨ Inspect shell-wrapped ExecStart commands.
- ✨ Print human-readable findings or JSON; never edits the source file.

## 🎬 Demo

Run the included example service file to see findings. The checks are advisory and do not certify a unit as secure; review each suggestion against the service's requirements.

## 🚀 Quick Start

```bash
python main.py examples/demo.service
```

## 🧰 Tech Stack

- 🟢 Python 3 standard library
- 🧱 Small, readable source files
- 🔒 Local processing with no telemetry

## 🗂️ Folder Structure

```text
systemd-unit-lint/
├── main.py
├── examples/demo.service
├── requirements.txt
├── assets/icon.svg
├── .gitignore
└── README.md
```

## 🗺️ Roadmap

- [ ] 🧪 Add focused automated tests
- [ ] 🧩 Add more examples based on feedback
- [ ] 📦 Publish a versioned release

## 🤝 Contributing

Issues and pull requests are welcome. Include a clear reproduction and keep changes focused.

## 📄 License

MIT — see [LICENSE](LICENSE).

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:111827&height=110&section=footer" width="100%" alt="Decorative wave footer" />
</div>
