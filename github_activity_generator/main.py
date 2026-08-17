import subprocess
import random
import sys
import json
import os
import argparse
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import filedialog, messagebox

DEFAULT_MESSAGES = [
    "update files", "fix minor issues", "refactor code", "clean up",
    "improve structure", "update readme", "minor changes", "code cleanup",
    "fix typo", "update config", "add comments", "optimize logic",
    "update dependencies", "fix formatting", "improve readability",
]

def get_commits_for_day(date, pattern, base_count, start_date):
    if pattern == "uniform":
        return base_count
    elif pattern == "random":
        return random.randint(0, min(base_count * 2, 10))
    elif pattern == "weekday":
        if date.weekday() < 5:
            return random.randint(base_count, min(base_count + 2, 10))
        else:
            return random.randint(0, max(1, base_count - 1))
    elif pattern == "burst":
        day_num = (date - datetime(date.year, 1, 1)).days
        if day_num % 7 < 5:
            return random.randint(base_count, min(base_count + 3, 10))
        else:
            return random.randint(0, 1)
    elif pattern == "natural":
        # 3-4 days active, 1-2 days break, repeat — most realistic pattern
        cycle_day = (date - start_date).days
        cycle_length = random.choice([5, 6])
        cycle_pos = cycle_day % cycle_length
        active_days = random.randint(3, 4)
        if cycle_pos < active_days:
            return random.randint(base_count, min(base_count + 2, 10))
        else:
            return random.randint(0, 1)
    return base_count

def pick_repo(title="Select your dummy repo folder"):
    while True:
        root = tk.Tk()
        root.withdraw()
        root.lift()
        root.attributes('-topmost', True)
        path = filedialog.askdirectory(title=title)
        root.destroy()

        if not path:
            print("  No folder selected. Exiting.")
            sys.exit(0)

        if not os.path.exists(os.path.join(path, ".git")):
            root2 = tk.Tk()
            root2.withdraw()
            messagebox.showerror(
                "Invalid Repo",
                f"Not a Git repository:\n{path}\n\nMake sure you cloned your dummy repo first."
            )
            root2.destroy()
            print(f"  Error: Not a git repo — {path}")
            continue

        print(f"  Repo selected: {path}")
        return path

def make_commit(date, message, repo_path):
    date_str = date.strftime("%Y-%m-%dT%H:%M:%S")
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str

    log_file = os.path.join(repo_path, "activity.log")
    with open(log_file, "a") as f:
        f.write(f"{date_str} - {message}\n")

    subprocess.run(["git", "add", "."], cwd=repo_path, env=env, capture_output=True)
    subprocess.run(["git", "commit", "-m", message], cwd=repo_path, env=env, capture_output=True)

def reset_repo():
    print("Select the repo you want to reset:")
    path = pick_repo("Select repo to reset")
    print(f"\nResetting repo: {path}")
    confirm = input("This will delete ALL commits. Are you sure? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Reset cancelled.")
        return
    result = subprocess.run(["git", "rev-list", "--max-parents=0", "HEAD"],
                            cwd=path, capture_output=True, text=True)
    first_commit = result.stdout.strip()
    if not first_commit:
        print("No commits found.")
        return
    subprocess.run(["git", "reset", "--hard", first_commit], cwd=path, capture_output=True)
    subprocess.run(["git", "push", "--force"], cwd=path, capture_output=True)
    print("Reset complete.")

def generate_for_repo(repo_path, start_date, end_date, base_count, pattern, messages, dry_run):
    dates = []
    current = start_date
    while current <= end_date:
        dates.append(current)
        current += timedelta(days=1)

    total = sum(get_commits_for_day(d, pattern, base_count, start_date) for d in dates)
    print(f"\n  Repo    : {repo_path}")
    print(f"  Range   : {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
    print(f"  Pattern : {pattern}")
    print(f"  Days    : {len(dates)}")
    print(f"  Est. commits: ~{total}")

    if dry_run:
        print("  [DRY RUN] No commits will be made.")
        return

    print("\n  Generating commits...")
    for i, date in enumerate(dates):
        count = get_commits_for_day(date, pattern, base_count, start_date)
        for _ in range(count):
            message = random.choice(messages)
            varied_date = date + timedelta(hours=random.randint(8, 22),
                                           minutes=random.randint(0, 59))
            make_commit(varied_date, message, repo_path)
        if count > 0:
            print(f"  [{i+1}/{len(dates)}] {date.strftime('%Y-%m-%d')} — {count} commit(s)")

    print(f"\n  Pushing...")
    result = subprocess.run(["git", "push"], cwd=repo_path, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"  Pushed successfully.")
    else:
        print(f"  Push failed. Run 'git push' manually.")
        print(f"  Error: {result.stderr}")

def load_config(config_path):
    with open(config_path, "r") as f:
        return json.load(f)

def interactive_mode():
    repos = []
    print("A folder picker will open — select your dummy repo folder.")
    while True:
        path = pick_repo("Select your dummy repo folder")
        repos.append(path)
        another = input("  Add another repo? (yes/no): ").strip().lower()
        if another != "yes":
            break

    start_str = input("\nStart date (YYYY-MM-DD): ").strip()
    end_str = input("End date (YYYY-MM-DD): ").strip()

    try:
        start_date = datetime.strptime(start_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        sys.exit(1)

    if start_date > end_date:
        print("Start date must be before end date.")
        sys.exit(1)

    base_count = int(input("Base commits per day (1-10): ").strip())

    print("\nPattern:")
    print("  1. uniform  — same commits every day")
    print("  2. random   — varies 0 to 2x per day")
    print("  3. weekday  — more Mon-Fri, less weekends")
    print("  4. burst    — heavy 5 days, light 2 days")
    print("  5. natural  — 3-4 days on, 1-2 days break (most realistic)")
    pattern_map = {"1": "uniform", "2": "random", "3": "weekday",
                   "4": "burst", "5": "natural"}
    pattern = pattern_map.get(input("Choose (1-5): ").strip(), "natural")

    print("\nCommit messages:")
    print("  1. Use default random messages")
    print("  2. Enter your own")
    msg_choice = input("Choose (1/2): ").strip()

    if msg_choice == "2":
        print("Enter messages one per line. Press Enter twice when done:")
        messages = []
        while True:
            msg = input().strip()
            if msg == "":
                break
            messages.append(msg)
        if not messages:
            messages = DEFAULT_MESSAGES
    else:
        messages = DEFAULT_MESSAGES

    dry_run = input("\nDry run first? (yes/no): ").strip().lower() == "yes"
    return repos, start_date, end_date, base_count, pattern, messages, dry_run

def main():
    parser = argparse.ArgumentParser(description="GitHub Activity Generator")
    parser.add_argument("--config", help="Path to config.json", default=None)
    parser.add_argument("--reset", action="store_true", help="Reset a repo")
    parser.add_argument("--dry-run", action="store_true", help="Preview without committing")
    args = parser.parse_args()

    print("=" * 50)
    print("   GitHub Activity Generator")
    print("   github.com/vedantchouhan")
    print("=" * 50)
    print()

    if args.reset:
        reset_repo()
        return

    if args.config:
        print(f"Loading config: {args.config}")
        config = load_config(args.config)
        repos = config.get("repos", [])
        start_date = datetime.strptime(config["start_date"], "%Y-%m-%d")
        end_date = datetime.strptime(config["end_date"], "%Y-%m-%d")
        base_count = config.get("commits_per_day", 3)
        pattern = config.get("pattern", "natural")
        messages = config.get("messages", DEFAULT_MESSAGES)
        dry_run = config.get("dry_run", False) or args.dry_run
    else:
        repos, start_date, end_date, base_count, pattern, messages, dry_run = interactive_mode()

    if dry_run:
        print("\n[DRY RUN MODE — no commits will be made]\n")

    for repo_path in repos:
        if not os.path.exists(repo_path):
            print(f"\nRepo not found: {repo_path} — skipping")
            continue
        generate_for_repo(repo_path, start_date, end_date,
                          base_count, pattern, messages, dry_run)

    if not dry_run:
        print("\nAll done. Check your GitHub profile.")
        print("This tool won't fix your reputation. But it will fix your graph.")
    else:
        print("\nDry run complete.")
        proceed = input("Proceed with real commits now? (yes/no): ").strip().lower()
        if proceed == "yes":
            print("\n[GENERATING REAL COMMITS]\n")
            for repo_path in repos:
                if not os.path.exists(repo_path):
                    continue
                generate_for_repo(repo_path, start_date, end_date,
                                  base_count, pattern, messages, dry_run=False)
            print("\nAll done. Check your GitHub profile.")
            print("This tool won't fix your reputation. But it will fix your graph.")
        else:
            print("Exited without making commits.")

if __name__ == "__main__":
    main()