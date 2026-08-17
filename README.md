markdown
# ⚡ GitHub Activity Generator

[![PyPI version](https://badge.fury.io/py/github-activity-generator.svg)](https://pypi.org/project/github-activity-generator/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> *"This tool won't fix your reputation. But it will fix your graph."*

A CLI tool to generate realistic GitHub commit activity for any date range. Features multiple commit patterns, multi-repo support, dry-run simulations, config file automation, interactive folder picking, and safe repo resets.

---

## ⚠️ Disclaimer

This tool is intended for **personal use, testing, and educational purposes only.** The author is not responsible for how this tool is utilized.

---

## ✨ Features

* **Custom Date Ranges:** Backdate or plan commits across any specific start and end dates.
* **Realistic Activity Patterns:**
  * `uniform`: Steady commit count every day.
  * `random`: Varies between 0 and 2x base commits per day.
  * `weekday`: Heavier activity Monday–Friday, lighter on weekends.
  * `burst`: 5 consecutive high-volume days followed by 2 light days.
  * `natural`: Alternates 3–4 active days with 1–2 break days (most organic).
* **Multi-Repo Automation:** Generate and push commits across multiple repositories in a single run.
* **Interactive UI & Folder Picker:** Visual folder picker so you never have to manually type absolute paths.
* **Dry-Run Mode:** Preview estimated commit counts and timelines before applying changes.
* **Config File Support:** Save settings in a `config.json` file for automated, zero-prompt execution.
* **Safe Reset:** Revert generated repos back to their initial commit with force-push support.

---

## 📋 Requirements

* Python >= 3.7
* Git installed and configured locally
* A GitHub account

---

## 🚀 Installation

### Option 1: Install via PyPI (Recommended)

```bash
pip install github-activity-generator

```

### Option 2: Install from Source

```bash
git clone [https://github.com/vedantchouhan/github-activity-generator.git](https://github.com/vedantchouhan/github-activity-generator.git)
cd github-activity-generator
pip install -e .

```

---

## 🛠️ Step-by-Step Setup Guide

### 1. Create a Private Dummy Repository

1. Go to [github.com](https://github.com) and click **New repository**.
2. Name it (e.g., `my-activity`).
3. Set visibility to **Private** *(strongly recommended)*.
4. Check **"Add a README file"**.
5. Click **Create repository**.

### 2. Clone the Dummy Repo Locally

**macOS / Linux:**

```bash
cd ~/Documents
git clone [https://github.com/YOUR_USERNAME/my-activity.git](https://github.com/YOUR_USERNAME/my-activity.git)

```

**Windows:**

```bash
cd C:\Users\YourName\Documents
git clone [https://github.com/YOUR_USERNAME/my-activity.git](https://github.com/YOUR_USERNAME/my-activity.git)

```

### 3. Run the Generator

If installed via pip:

```bash
github-activity-generator

```

If running the Python script directly:

```bash
python3 -m github_activity_generator.main

```

---

## 💻 Usage & Options

### Interactive CLI Mode

Running the command without arguments launches an interactive setup wizard with a folder picker GUI:

```bash
github-activity-generator

```

### Config File Mode

Skip prompts by passing a `config.json` file:

```bash
github-activity-generator --config config.json

```

**Example `config.json`:**

```json
{
  "repos": [
    "/Users/yourname/Documents/my-activity",
    "/Users/yourname/Documents/my-activity-2"
  ],
  "start_date": "2026-01-01",
  "end_date": "2026-06-30",
  "commits_per_day": 3,
  "pattern": "natural",
  "dry_run": false,
  "messages": [
    "update files",
    "fix minor issues",
    "refactor code",
    "clean up",
    "improve structure"
  ]
}

```

### Dry-Run Mode

Preview commits without writing to git history or pushing:

```bash
github-activity-generator --dry-run

```

### Reset Mode

Wipe all generated commits and roll back the repository to its initial commit:

```bash
github-activity-generator --reset

```

---

## 💡 Best Practices

* **Keep It Natural:** Set `commits_per_day` between 2–4 and use the `natural` or `weekday` pattern for an organic-looking commit graph.
* **Date Spans:** Spread activity evenly across months rather than overloading a single week.
* **Keep Repos Private:** Always run activity generation inside dedicated dummy private repositories.

---

## 📁 Repository Structure

```text
github-activity-generator/
├── github_activity_generator/
│   ├── __init__.py
│   └── main.py
├── config.json
├── pyproject.toml
├── LICENSE
└── README.md

```

---

## 📄 License

Distributed under the MIT License. See [LICENSE](https://www.google.com/search?q=LICENSE) for more information.

---

## 👤 Author

**Vedant Chouhan**

* GitHub: [@vedantchouhan](https://github.com/vedantchouhan)
* Email: chouhanvedant84@gmail.com

```

