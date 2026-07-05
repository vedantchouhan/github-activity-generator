# ⚡ GitHub Activity Generator

> "This tool won't fix your reputation. But it will fix your graph."

A CLI tool to generate GitHub commit activity for any date range. Built in Python. No BS, no GUI — just clone, configure, and run.

---

## ⚠️ Disclaimer

This tool is intended for **personal use and learning purposes only.**
The author is not responsible for how this is used.

---

## 🚀 What it does

- Generates commits across a custom date range
- Customizable commits per day (1–10)
- Random or custom commit messages
- Pushes directly to your GitHub repo
- Makes your contribution graph look like you never sleep

---

## 📋 Requirements

- Python 3.x
- Git installed and configured
- A GitHub account
- A private dummy repo (instructions below)

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
1. Go to github.com → New repository
2. Name it anything (e.g. `my-activity`)
3. Set to **Private**
4. Check "Add a README file"
5. Click **Create repository**

**Step 4 — Clone your dummy repo locally:**
```bash
git clone https://github.com/YOUR_USERNAME/my-activity.git
```

**Step 5 — Run the generator:**
```bash
python3 generate.py
```

---

## 💻 Usage

When you run the script, it will ask you a few questions. Here's exactly what to enter:

```
=============================================
   GitHub Activity Generator
   github.com/vedantchouhan
=============================================

Enter path to your local repo:
```
→ Enter the full path to your cloned dummy repo.
Example: `/Users/john/Documents/my-activity`
*(On Mac: drag the folder into terminal to get the path automatically)*

```
Start date (YYYY-MM-DD):
```
→ The date you want commits to start from.
Example: `2026-01-01` *(1st January 2026)*

```
End date (YYYY-MM-DD):
```
→ The date you want commits to end on.
Example: `2026-06-30` *(fills 6 months of activity)*

```
Commits per day (1-10):
```
→ How many green squares per day. Keep it between 2–5 for a natural look.
Example: `3`

```
Commit messages:
1. Use default random messages
2. Enter your own messages
Choose (1/2):
```
→ Press `1` for automatic messages. Press `2` to type your own — enter one per line, press Enter twice when done.

```
Looks good? Start generating? (yes/no):
```
→ Type `yes` to start. It will generate all commits and push automatically.

---

## ✅ Full example run

```
Enter path to your local repo: /Users/john/Documents/my-activity
Start date (YYYY-MM-DD): 2026-01-01
End date (YYYY-MM-DD): 2026-03-31
Commits per day (1-10): 3
Choose (1/2): 1

Preview:
  Date range : 2026-01-01 to 2026-03-31
  Total days : 90
  Commits/day: 3
  Total commits: 270

Looks good? Start generating? (yes/no): yes

Generating commits...
  [1/90] 2026-01-01 — 3 commit(s) done
  [2/90] 2026-01-02 — 3 commit(s) done
  ...
  [90/90] 2026-03-31 — 3 commit(s) done

Pushing to GitHub...

Done. Check your GitHub profile.
This tool won't fix your reputation. But it will fix your graph.
```

---

## 📁 Project Structure

```
github-activity-generator/
├── generate.py       # main script
├── requirements.txt  # dependencies
├── LICENSE           # MIT
└── README.md
```

---

## 📌 Tips

- Keep commits per day between 2–5 for a natural-looking graph
- Spread across several months for a more organic pattern
- Use your own commit messages for a more authentic feel
- Always use a **private** repo — keep it separate from real work

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 👤 Author

**Vedant Chouhan**
B.Tech CSE (AI/ML) — UPES Dehradun
[github.com/vedantchouhan](https://github.com/vedantchouhan)