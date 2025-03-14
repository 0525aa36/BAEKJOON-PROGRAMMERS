import os
import requests
from bs4 import BeautifulSoup

# 풀이 코드가 저장된 폴더들
LANGUAGES = {
    "Python": "Python",
    "C": "C",
    "Java": "Java"
}

# README 파일 경로
README_PATH = "README.md"

import requests
from bs4 import BeautifulSoup

def fetch_problem_title(problem_number):
    """ 백준 문제 제목 가져오기 """
    url = f"https://www.acmicpc.net/problem/{problem_number}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        title_tag = soup.find("span", id="problem_title")  # ✅ 문제 제목이 있는 태그 확인
        return title_tag.text.strip() if title_tag else "제목 없음"
    
    except requests.RequestException:
        return "제목 불러오기 실패"


def get_solved_problems():
    problems = []
    for lang, folder in LANGUAGES.items():
        if not os.path.exists(folder):
            continue
        for filename in os.listdir(folder):
            if filename.endswith((".py", ".c", ".java")):
                problem_number = ''.join(filter(str.isdigit, filename))
                if problem_number:
                    title = fetch_problem_title(problem_number)  # 🔹 문제 제목 가져오기
                    problems.append((problem_number, title, lang, filename))
    return sorted(problems, key=lambda x: int(x[0]))  # 문제 번호 기준 정렬

def update_readme():
    problems = get_solved_problems()

    table_header = "| 문제 번호 | 문제 제목 | 언어 | 파일 |\n|----------|----------|------|------|\n"
    table_content = "\n".join([f"| {num} | {title} | {lang} | [{file}]({lang}/{file}) |" for num, title, lang, file in problems])

    # ✅ 문제 풀이가 없는 경우 기본 메시지 추가
    if not table_content:
        table_content = "| 등록된 문제가 없습니다 | - | - | - |\n"

    new_readme = f"""# 🏆 Baekjoon Online Judge Solutions

이 저장소는 [백준 온라인 저지](https://www.acmicpc.net/) 문제 풀이를 기록하는 공간입니다.

## 📂 폴더 구조
- `Python/` : 파이썬 풀이 코드
- `C++/` : C++ 풀이 코드
- `Java/` : 자바 풀이 코드

## 🚀 문제 풀이 기록
{table_header}{table_content}

## 📌 사용법
1. 백준 문제를 풀이하고 저장합니다.
2. `git add .` → `git commit -m "메시지"` → `git push origin main`으로 업데이트합니다.
"""

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_readme)

if __name__ == "__main__":
    update_readme()
    print("✅ README.md 업데이트 완료!")
