import os, subprocess
from datetime import date, datetime, timedelta

# С какого дня заполнять:
start = date(2022, 7, 7)
end   = date.today()    # по сегодня

# Сколько коммитов на день (можно 1–3; 3 = «ярче» квадраты)
COMMITS_PER_DAY = 2

def run_git_commit(d):
    ts = datetime(d.year, d.month, d.day, 12, 0, 0).strftime("%Y-%m-%d %H:%M:%S")
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = ts
    env["GIT_COMMITTER_DATE"] = ts
    subprocess.run(
        ["git", "commit", "--allow-empty", "-m", f"fill {d.isoformat()}"],
        check=True, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )

d = start
while d <= end:
    for _ in range(COMMITS_PER_DAY):
        run_git_commit(d)
    d += timedelta(days=1)

# Финальный push
subprocess.run(["git", "push", "-f", "origin", "main"], check=True)
print("Готово: пуш отправлен.")
