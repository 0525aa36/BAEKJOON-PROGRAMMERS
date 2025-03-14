import os

# 풀이 코드가 저장된 폴더들
LANGUAGES = {
    "Python": "Python",
    "C++": "C++",
    "Java": "Java"
}

# README 파일 경로
README_PATH = "README.md"

def get_solved_problems():
    problems = []
    for lang, folder in LANGUAGES.items():
        if not os.path.exists(folder):
            continue
        for filename in os.listdir(folder):
            if filename.endswith((".py", ".cpp", ".java")):
                # ✅ 파일 이름에서 숫자만 추출 (예: "1000.py" → 1000)
                problem_number = ''.join(filter(str.isdigit, filename))
                if problem_number:  # 숫자가 포함된 경우만 추가
                    problems.append((problem_number, lang, filename))
    return sorted(problems, key=lambda x: int(x[0]))  # 문제 번호 기준 정렬

def update_readme():
    problems = get_solved_problems()

    table_header = "| 문제 번호 | 언어 | 파일 |\n|----------|------|------|\n"
    table_content = "\n".join([f"| {num} | {lang} | [{file}]({lang}/{file}) |" for num, lang, file in problems])
    
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
