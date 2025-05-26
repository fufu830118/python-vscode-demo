import os
import datetime

commit_message = input("請輸入 commit 訊息（預設為時間戳記）：").strip()

if not commit_message:
    commit_message = f"Update on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# 一鍵執行 Git 指令
os.system('git add .')
os.system(f'git commit -m "{commit_message}"')
os.system('git push')
