import os
import requests
import shutil
from bs4 import BeautifulSoup

# 풀이 코드가 저장된 폴더들
LANGUAGES = {
    "Python": "Python",
    "C++": "C++",
    "Java": "Java"
}

# 백준 문제 URL
BAEKJOON_URL = "https://www.acmicpc.net/problem/"

# README 파일 경로
README_PATH = "README.md"

def fetch_problem_info(problem_number):
    """ 백준 문제 정보 가져오기 (제목, 문제 설명, 입력, 출력) """
    url = f"{BAEKJOON_URL}{problem_number}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        title_tag = soup.find("span", id="problem_title")
        problem_title = title_tag.text.strip() if title_tag else "제목 없음"

        # 문제 설명, 입력, 출력 가져오기
        description_tag = soup.find("div", id="problem_description")
        input_tag = soup.find("div", id="problem_input")
        output_tag = soup.find("div", id="problem_output")

        problem_description = description_tag.get_text(separator="\n").strip() if description_tag else "문제 설명 없음"
        problem_input = input_tag.get_text(separator="\n").strip() if input_tag else "입력 정보 없음"
        problem_output = output_tag.get_text(separator="\n").strip() if output_tag else "출력 정보 없음"

        return problem_title, problem_description, problem_input, problem_output

    except requests.RequestException:
        return "제목 불러오기 실패", "문제 설명 없음", "입력 정보 없음", "출력 정보 없음"

def organize_solved_problems():
    """ 문제 풀이 파일을 정리하고, 문제별 폴더와 README.md 생성 """
    for lang, folder in LANGUAGES.items():
        if not os.path.exists(folder):
            continue
        for filename in os.listdir(folder):
            if filename.endswith((".py", ".cpp", ".java")):
                problem_number = ''.join(filter(str.isdigit, filename))
                if problem_number:
                    title, description, input_desc, output_desc = fetch_problem_info(problem_number)

                    # 문제 제목을 폴더명으로 설정
                    problem_dir = f"{problem_number} - {title}"
                    if not os.path.exists(problem_dir):
                        os.makedirs(problem_dir)

                    # README.md 생성
                    problem_readme = os.path.join(problem_dir, "README.md")
                    with open(problem_readme, "w", encoding="utf-8") as f:
                        f.write(f"# {title} ({problem_number})\n\n")
                        f.write(f"## 문제 설명\n{description}\n\n")
                        f.write(f"## 입력\n{input_desc}\n\n")
                        f.write(f"## 출력\n{output_desc}\n")

                    # 코드 파일 이동
                    old_path = os.path.join(folder, filename)
                    new_path = os.path.join(problem_dir, filename)
                    shutil.move(old_path, new_path)

def update_main_readme():
    """ 메인 README 업데이트 (문제 목록 링크 추가) """
    problem_folders = [d for d in os.listdir() if os.path.isdir(d) and d.split()[0].isdigit()]
    problem_folders.sort(key=lambda x: int(x.split()[0]))  # 문제 번호 기준 정렬

    table_header = "| 문제 번호 | 문제 제목 | 링크 |\n|----------|----------|------|\n"
    table_content = "\n".join([f"| {folder.split(' - ')[0]} | {folder.split(' - ')[1]} | [문제 풀이]({folder}/README.md) |" for folder in problem_folders])

    new_readme = f"""# 🏆 Baekjoon Online Judge Solutions

이 저장소는 [백준 온라인 저지](https://www.acmicpc.net/) 문제 풀이를 기록하는 공간입니다.

## 📂 문제 목록
{table_header}{table_content}

## 📌 사용법
1. 백준 문제를 풀이하고 저장합니다.
2. `git add .` → `git commit -m "메시지"` → `git push origin main`으로 업데이트합니다.
"""

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_readme)

if __name__ == "__main__":
    organize_solved_problems()  # 문제 정리 및 이동
    update_main_readme()  # 메인 README 업데이트
    print("✅ 문제 정리 및 README.md 업데이트 완료!")
