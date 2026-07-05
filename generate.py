import subprocess
import random
import sys
from datetime import datetime, timedelta

# ── Commit message templates ────────────────────────────────────────────
DEFAULT_MESSAGES = [
    "update files",
    "fix minor issues",
    "refactor code",
    "clean up",
    "improve structure",
    "update readme",
    "minor changes",
    "code cleanup",
    "fix typo",
    "update config",
]

def get_date_range(start_date, end_date):
    dates = []
    current = start_date
    while current <= end_date:
        dates.append(current)
        current += timedelta(days=1)
    return dates

def make_commit(date, message, repo_path):
    date_str = date.strftime("%Y-%m-%dT12:00:00")
    env_vars = {
        "GIT_AUTHOR_DATE": date_str,
        "GIT_COMMITTER_DATE": date_str,
    }
    import os
    env = os.environ.copy()
    env.update(env_vars)

    # Create a small change so commit isn't empty
    log_file = os.path.join(repo_path, "activity.log")
    with open(log_file, "a") as f:
        f.write(f"{date_str} - {message}\n")

    subprocess.run(["git", "add", "."], cwd=repo_path, env=env)
    subprocess.run(
        ["git", "commit", "-m", message],
        cwd=repo_path,
        env=env
    )

def main():
    print("=" * 45)
    print("   GitHub Activity Generator")
    print("   github.com/vedantchouhan")
    print("=" * 45)
    print()

    # ── Get inputs ──────────────────────────────
    repo_path = input("Enter path to your local repo: ").strip()
    
    start_str = input("Start date (YYYY-MM-DD): ").strip()
    end_str = input("End date (YYYY-MM-DD): ").strip()
    
    commits_per_day = int(input("Commits per day (1-10): ").strip())
    
    print("\nCommit messages:")
    print("1. Use default random messages")
    print("2. Enter your own messages")
    choice = input("Choose (1/2): ").strip()

    if choice == "2":
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

    # ── Parse dates ─────────────────────────────
    try:
        start_date = datetime.strptime(start_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        sys.exit(1)

    if start_date > end_date:
        print("Start date must be before end date.")
        sys.exit(1)

    if commits_per_day < 1 or commits_per_day > 10:
        print("Commits per day must be between 1 and 10.")
        sys.exit(1)

    # ── Preview ─────────────────────────────────
    dates = get_date_range(start_date, end_date)
    total = len(dates) * commits_per_day
    print(f"\nPreview:")
    print(f"  Date range : {start_str} to {end_str}")
    print(f"  Total days : {len(dates)}")
    print(f"  Commits/day: {commits_per_day}")
    print(f"  Total commits: {total}")
    print()

    confirm = input("Looks good? Start generating? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Cancelled.")
        sys.exit(0)

    # ── Generate commits ─────────────────────────
    print("\nGenerating commits...")
    for i, date in enumerate(dates):
        for j in range(commits_per_day):
            message = random.choice(messages)
            make_commit(date, message, repo_path)
        print(f"  [{i+1}/{len(dates)}] {date.strftime('%Y-%m-%d')} — {commits_per_day} commit(s) done")

    # ── Push ─────────────────────────────────────
    print("\nPushing to GitHub...")
    result = subprocess.run(
        ["git", "push"],
        cwd=repo_path,
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print("\nDone. Check your GitHub profile.")
        print("Use it wisely. Or don't — you're already more accountable than most politicians.")
    else:
        print("\nPush failed. Error:")
        print(result.stderr)
        print("Try running 'git push' manually in your repo folder.")

if __name__ == "__main__":
    main()