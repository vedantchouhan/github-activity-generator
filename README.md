# ⚡ GitHub Activity Generator

> "This tool won't fix your reputation. But it will fix your graph."

A CLI tool to generate GitHub commit activity for any date range. Supports multiple patterns, multiple repos, dry run mode, config file, and folder picker. No BS, no GUI — just clone, configure, and run.

---

## ⚠️ Disclaimer

This tool is intended for **personal use and learning purposes only.**
The author is not responsible for how this is used.

---

## 🚀 What it does

- Generates commits across a custom date range
- 4 commit patterns — uniform, random, weekday, burst
- Folder picker popup — no need to type repo paths manually
- Dry run mode — preview before committing anything
- Multiple repos support — run across several repos at once
- Reset mode — wipe all generated commits and start fresh
- Config file support — save settings and reuse anytime

---

## 📋 Requirements

- Python 3.x
- Git installed and configured
- A GitHub account

---

## ⚙️ Setup — Step by Step

**Step 1 — Clone this repo:**
```bash
git clone https://github.com/vedantchouhan/github-activity-generator.git
cd github-activity-generator
```

**Step 2 — Install dependency:**
```bash
pip3 install gitpython
```

**Step 3 — Create a private dummy repo on GitHub:**

This is the repo where commits will be generated. Keep it private.

1. Go to [github.com](https://github.com) and click **New repository**
2. Give it any name (e.g. `my-activity`)
3. Set visibility to **Private**
4. Check **"Add a README file"**
5. Click **Create repository**

**Step 4 — Clone your dummy repo locally:**

**Mac:**
```bash
cd ~/Documents
git clone https://github.com/YOUR_USERNAME/my-activity.git
```

**Windows:**
```bash
cd C:\Users\YourName\Documents
git clone https://github.com/YOUR_USERNAME/my-activity.git
```

Replace `YOUR_USERNAME` with your actual GitHub username.

**Step 5 — Run the generator:**
```bash
python3 generate.py
```

---

## 💻 How it works — Step by Step

**1. A folder picker popup will open automatically**

Select the dummy repo folder you cloned in Step 4.
If you select a wrong folder (not a git repo), an error popup will appear — just select the correct folder.

After selecting, it will ask:
```
Add another repo? (yes/no):
```
Type `yes` to add more repos, or `no` to continue.

**2. Enter date range**
```
Start date (YYYY-MM-DD): 2026-01-01
End date (YYYY-MM-DD): 2026-06-30
```
This fills your contribution graph from January to June 2026.

**3. Enter base commits per day**
```
Base commits per day (1-10): 3
```
Keep it between 2–5 for a natural-looking graph.

**4. Choose a pattern**
```
1. uniform  — same commits every day
2. random   — varies 0 to 2x per day (most natural)
3. weekday  — more on weekdays, less on weekends
4. burst    — heavy for 5 days, light for 2 days
```
`random` or `weekday` look most organic.

**5. Choose commit messages**
```
1. Use default random messages
2. Enter your own
```
Default messages are developer-style (e.g. "fix typo", "refactor code"). Or enter your own.

**6. Dry run**
```
Dry run first? (yes/no): yes
```
Type `yes` to preview — shows how many commits will be made without actually doing anything.
Type `no` to generate and push directly.

---

## ✅ Full example run

```
==================================================
   GitHub Activity Generator
   github.com/vedantchouhan
==================================================

A folder picker will open — select your dummy repo folder.
  Repo selected: /Users/john/Documents/my-activity
  Add another repo? (yes/no): no

Start date (YYYY-MM-DD): 2026-01-01
End date (YYYY-MM-DD): 2026-03-31
Base commits per day (1-10): 3
Choose (1-4): 2
Choose (1/2): 1
Dry run first? (yes/no): no

  Repo    : /Users/john/Documents/my-activity
  Range   : 2026-01-01 to 2026-03-31
  Pattern : random
  Days    : 90
  Est. total commits: ~270

  Generating commits...
  [1/90] 2026-01-01 — 3 commit(s)
  [2/90] 2026-01-02 — 5 commit(s)
  ...
  [90/90] 2026-03-31 — 2 commit(s)

  Pushing /Users/john/Documents/my-activity...
  Pushed successfully.

All done. Check your GitHub profile.
This tool won't fix your reputation. But it will fix your graph.
```

---

## ⚙️ Config file mode

Instead of answering questions every time, save your settings in `config.json`:

```json
{
    "repos": [
        "/Users/yourname/Documents/my-activity"
    ],
    "start_date": "2026-01-01",
    "end_date": "2026-06-30",
    "commits_per_day": 3,
    "pattern": "random",
    "dry_run": false,
    "messages": [
        "update files",
        "fix minor issues",
        "refactor code"
    ]
}
```

Then run:
```bash
python3 generate.py --config config.json
```

No questions asked — runs automatically with your saved settings.

---

## 🔄 Reset mode

Want to wipe all generated commits and start fresh?

```bash
python3 generate.py --reset
```

A folder picker opens — select the repo you want to reset. All commits will be deleted and the repo will go back to its first commit.

---

## 👁️ Dry run mode

Preview without making any commits:

```bash
python3 generate.py --dry-run
```

---

## 📌 Tips

- Keep commits per day between 2–5 for a natural-looking graph
- Use `random` or `weekday` pattern — looks most organic
- Spread across several months, not just a few days
- Always use a **private** repo — keep it separate from real work
- Running the same date range twice will double your commits — use reset first if you want to redo

---

## 📁 Project Structure

```
github-activity-generator/
├── generate.py       # main script
├── config.json       # config file template
├── requirements.txt  # dependencies
├── LICENSE           # MIT
└── README.md
```

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 👤 Author

**Vedant Chouhan**
B.Tech CSE (AI/ML) — UPES Dehradun
[github.com/vedantchouhan](https://github.com/vedantchouhan)