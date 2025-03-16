import os
import subprocess
import requests
from bs4 import BeautifulSoup

# 풀이 코드가 저장된 폴더들
LANGUAGES = {
    "Python": "Python",
    "C++": "C++",
    "Java": "Java"
}

# README 파일 경로
README_PATH = "README.md"

def fetch_problem_title(problem_number):
    """ 백준 문제 제목 가져오기 """
    url = f"https://www.acmicpc.net/problem/{problem_number}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        title_tag = soup.find("span", id="problem_title")  # ✅ 문제 제목이 있는 태그
        
        return title_tag.text.strip() if title_tag else "제목 없음"

    except requests.RequestException:
        return "제목 불러오기 실패"

def get_commit_order():
    """ Git에서 파일별 커밋 순서를 가져오기 (나중에 커밋한 파일이 밑으로 가게) """
    result = subprocess.run(
        ["git", "log", "--pretty=format:%at", "--name-only"],
        capture_output=True, text=True
    )

    commit_order = {}
    current_timestamp = None

    for line in result.stdout.split("\n"):
        if line.strip().isdigit():  # UNIX 타임스탬프 값이면
            current_timestamp = int(line.strip())
        elif line.strip():  # 파일명이면
            commit_order[line.strip()] = current_timestamp
    
    return commit_order

def get_solved_problems():
    """ 문제 풀이 기록을 커밋 순서대로 가져오기 """
    problems = []
    commit_order = get_commit_order()  # 🔹 Git에서 커밋 순서 가져오기

    for lang, folder in LANGUAGES.items():
        if not os.path.exists(folder):
            continue
        for filename in os.listdir(folder):
            if filename.endswith((".py", ".cpp", ".java")):
                problem_number = ''.join(filter(str.isdigit, filename))
                if problem_number:
                    title = fetch_problem_title(problem_number)  # 🔹 문제 제목 가져오기
                    commit_time = commit_order.get(f"{folder}/{filename}", float("inf"))
                    problems.append((commit_time, problem_number, title, lang, filename))
    
    return sorted(problems, key=lambda x: x[0], reverse=True)  # 🔹 커밋된 순서대로 정렬

def update_readme():
    problems = get_solved_problems()

    table_header = "| # | 문제 번호 | 문제 제목 | 언어 | 파일 |\n|---|----------|----------|------|------|\n"
    table_content = "\n".join([f"| {idx + 1} | {num} | {title} | {lang} | [{file}]({lang}/{file}) |"
                               for idx, (_, num, title, lang, file) in enumerate(problems)])

    # ✅ 문제 풀이가 없는 경우 기본 메시지 추가
    if not table_content:
        table_content = "| - | 등록된 문제가 없습니다 | - | - | - |\n"

    new_readme = f"""# BOJ

## 📂 폴더 구조
- `Python/` : 파이썬 풀이 코드

## ✅ 문제 풀이 기록
{table_header}{table_content}

"""

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_readme)

if __name__ == "__main__":
    update_readme()
    print("✅ README.md 업데이트 완료!")
