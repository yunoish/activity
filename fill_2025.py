import os, sys, subprocess, random
from datetime import date, datetime, timedelta

def run(args, **kw):
    """Запуск команды с выводом ошибки, если что-то пошло не так."""
    p = subprocess.run(args, text=True, capture_output=True, **kw)
    if p.returncode != 0:
        print("ERROR CMD:", " ".join(args))
        print(p.stdout)
        print(p.stderr)
        sys.exit(p.returncode)
    return p

def ensure_repo_ready():
    # Внутри git-репо?
    run(["git", "rev-parse", "--is-inside-work-tree"])
    # user.name / user.email — если пустые, зададим базовые
    if not subprocess.run(["git","config","user.name"], capture_output=True, text=True).stdout.strip():
        run(["git","config","user.name","yunoish"])
    if not subprocess.run(["git","config","user.email"], capture_output=True, text=True).stdout.strip():
        run(["git","config","user.email","you@example.com"])
    # безопасная директория (иногда нужно на Windows)
    run(["git","config","--global","--add","safe.directory", os.getcwd()])
    # если нет коммитов — сделать init
    if subprocess.run(["git","log","-1"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
        if not os.path.exists("README.md"):
            with open("README.md","w",encoding="utf-8") as f:
                f.write("# activity\n")
        run(["git","add","README.md"])
        run(["git","commit","-m","init"])
        subprocess.run(["git","branch","-M","main"], check=False)

def do_commit(d, h, m):
    ts = datetime(d.year, d.month, d.day, h, m, 0).strftime("%Y-%m-%d %H:%M:%S")
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = ts
    env["GIT_COMMITTER_DATE"] = ts
    # -c commit.gpgsign=false на случай, если где-то включена подпись
    run(["git","-c","commit.gpgsign=false","commit","--allow-empty","-m",f"fill {d}"], env=env)

def main():
    ensure_repo_ready()
    start = date(2025, 1, 1)
    end   = date(2025,12,31)

    d = start
    since_last_push = 0
    while d <= end:
        for _ in range(random.randint(5,10)):
            do_commit(d, random.randint(9,23), random.randint(0,59))
            since_last_push += 1
        d += timedelta(days=1)
        # пушим порциями, чтобы не завалить один гигантский push
        if since_last_push >= 500:
            subprocess.run(["git","push","-f","origin","main"])
            since_last_push = 0

    run(["git","push","-f","origin","main"])
    print("Готово: пуш отправлен.")

if __name__ == "__main__":
    main()
