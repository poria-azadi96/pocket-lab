<div align="center">

# 📱 Pocket Lab | Mobile Scientific Computing
### Scientific simulations and mathematical modeling directly on smartphone processors

[English](README.md) • [فارسی](README.fa.md)

[![GitHub Profile](https://img.shields.io/badge/GitHub-poria--azadi96-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/poria-azadi96)
[![Telegram Channel](https://img.shields.io/badge/Telegram-The%20Maze-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/the_maze2022)
[![Instagram](https://img.shields.io/badge/Instagram-poria__azadi__official-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/poria_azadi_official/)
[![YouTube](https://img.shields.io/badge/YouTube-PoriaAzadi__official-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@PoriaAzadi_official)
[![ResearchGate](https://img.shields.io/badge/ResearchGate-Poria%20Azadi-00CCBB?style=for-the-badge&logo=researchgate&logoColor=white)](https://www.researchgate.net/profile/Poria-Azadi-2)

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![OS](https://img.shields.io/badge/Env-Termux%20%7C%20Ubuntu-E95420?style=flat-square&logo=ubuntu&logoColor=white)](https://termux.dev/)
[![Platform](https://img.shields.io/badge/Platform-Android%20%7C%20Colab-4CAF50?style=flat-square)](https://github.com/poria-azadi96/pocket-lab)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

<p align="center">
  <b>"Your smartphone is not merely a content consumption device; it can serve as a genuine environment for modeling and simulating complex scientific phenomena."</b>
</p>

[About](#-about-the-project) •
[Episodes](#-simulation-episodes) •
[Quick Start](#-quick-start) •
[Repository Structure](#-repository-structure) •
[Community](#-community--connect)

---

</div>

## 🧬 About the Project

Modern mobile processors possess formidable computational performance, often outperforming the supercomputers of previous decades. The core objective of **Pocket Lab** is to demonstrate that rigorous computational physics, non-linear dynamics, and mathematical modeling do not strictly require costly academic clusters or dedicated workstations.

Throughout this series, we numerically solve coupled differential equations and model natural algorithms natively inside mobile Linux environments using Python.

---

## 🎬 Simulation Episodes

| # | Simulation Title | Scientific Phenomenon | Status | Source Code | Cloud Run |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **00** | **Pocket Environment Setup** | Native Ubuntu Linux and scientific Python via Termux | ✅ Complete | [Setup Guide](episodes/ep00-environment-setup/) | — |
| **01** | **Double Pendulum Simulation** | Deterministic chaos & extreme sensitivity ($1.0^\circ$ offset) | ✅ Complete | [Python Code](episodes/ep01-double-pendulum/double_pendulum.py) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/) |
| **02** | **Boids Flocking Model** | Emergence and self-organizing collective intelligence | ⏳ Coming Soon | — | — |
| **03** | **Conway’s Game of Life** | Cellular automata and complex life dynamics from simple rules | ⏳ Coming Soon | — | — |
| **04** | **Epidemic Dynamics (SIR)** | Mathematical modeling of viral spread and threshold mechanics | ⏳ Coming Soon | — | — |

---

## 🚀 Quick Start

### Track 1: Native Mobile Integration (Android via Termux — Offline)
1. Download and install **Termux** exclusively from [GitHub Releases](https://github.com/termux/termux-app/releases) or F-Droid (do not install the outdated Google Play version).
2. Install the isolated Ubuntu userland and log in:
```bash
pkg install proot-distro -y
proot-distro install ubuntu
proot-distro login ubuntu
