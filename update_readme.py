import os
import requests
import shutil
from bs4 import BeautifulSoup

# 난이도별 디렉토리 설정
DIFFICULTY_MAP = {
    "Bronze": "Bronze",
    "Silver": "Silver",
    "Gold": "Gold",
    "Platinum": "Platinum",
    "Diamond": "Diamond",
    "Ruby": "Ruby"
}

# 언어별 디렉토리 설정
LANGUAGES = {
    "Python": "Python",
    "C++": "C++",
    "Java": "Java"
}

# 백준 문제 URL
BAEKJOON_URL = "https://www.acmicpc.net/problem/"

def fetch_problem_info(problem_number):
    """ 백준 문제 정보 가져오기 (제목, 난이도, 문제 설명, 입력, 출력) """
    url = f"{BAEKJOON_URL}{problem_number}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")

        # ✅ 문제 제목 가져오기
        title_tag = soup.find("span", id="problem_title")
        problem_title = title_tag.text.strip() if title_tag else "제목 없음"

        # ✅ 난이도 가져오기
        difficulty_tag = soup.find("img", class_="solvedac-tier")
        difficulty = "Unrated"
        if difficulty_tag and "alt" in difficulty_tag.attrs:
            difficulty_text = difficulty_tag["alt"].split()[-1]  # 예: "Silver 3" -> "Silver"
            difficulty = DIFFICULTY_MAP.get(difficulty_text, "Unrated")

        # ✅ 문제 설명, 입력, 출력 가져오기
        description_tag = soup.find("div", id="problem_description")
        input_tag = soup.find("div", id="problem_input")
        output_tag = soup.find("div", id="problem_output")

        problem_description = description_tag.get_text(separator="\n").strip() if description_tag else "문제 설명 없음"
        problem_input = input_tag.get_text(separator="\n").strip() if input_tag else "입력 정보 없음"
        problem_output = output_tag.get_text(separator="\n").strip() if output_tag else "출력 정보 없음"

        return problem_title, difficulty, problem_description, problem_input, problem_output

    except requests.RequestException:
        return "제목 불러오기 실패", "Unrated", "문제 설명 없음", "입력 정보 없음", "출력 정보 없음"

def organize_solved_problems():
    """ 문제 풀이 파일을 정리하고, 난이도별 & 언어별 폴더 구조 생성 """
    for lang, folder in LANGUAGES.items():
        if not os.path.exists(folder):
            continue
        for filename in os.listdir(folder):
            if filename.endswith((".py", ".cpp", ".java")):
                problem_number = ''.join(filter(str.isdigit, filename))
                if problem_number:
                    title, difficulty, description, input_desc, output_desc = fetch_problem_info(problem_number)

                    # 난이도 폴더 경로 설정
                    difficulty_dir = os.path.join(difficulty, lang)
                    if not os.path.exists(difficulty_dir):
                        os.makedirs(difficulty_dir)

                    # 문제 제목을 포함한 폴더 생성
                    problem_dir = os.path.join(difficulty_dir, f"{problem_number} - {title}")
                    if not os.path.exists(problem_dir):
                        os.makedirs(problem_dir)

                    # 문제별 README.md 생성
                    problem_readme = os.path.join(problem_dir, "README.md")
                    with open(problem_readme, "w", encoding="utf-8") as f:
                        f.write(f"# {title} ({problem_number})\n\n")
                        f.write(f"## 난이도: {difficulty}\n\n")
                        f.write(f"## 문제 설명\n{description}\n\n")
                        f.write(f"## 입력\n{input_desc}\n\n")
                        f.write(f"## 출력\n{output_desc}\n")

                    # 코드 파일 이동
                    old_path = os.path.join(folder, filename)
                    new_path = os.path.join(problem_dir, filename)
                    shutil.move(old_path, new_path)

def update_main_readme():
    """ 메인 README 업데이트 (문제 목록 링크 추가) """
    difficulty_levels = [d for d in os.listdir() if os.path.isdir(d) and d in DIFFICULTY_MAP.values()]
    
    table_header = "| 난이도 | 문제 번호 | 문제 제목 | 언어 | 링크 |\n|--------|----------|----------|------|------|\n"
    table_content = ""

    for difficulty in difficulty_levels:
        for lang in LANGUAGES.values():
            lang_path = os.path.join(difficulty, lang)
            if os.path.exists(lang_path):
                for problem_folder in os.listdir(lang_path):
                    problem_number = problem_folder.split(" - ")[0]
                    problem_title = problem_folder.split(" - ")[1]
                    table_content += f"| {difficulty} | {problem_number} | {problem_title} | {lang} | [문제 풀이]({difficulty}/{lang}/{problem_folder}/README.md) |\n"

    new_readme = f"""# 🏆 Baekjoon Online Judge Solutions

이 저장소는 [백준 온라인 저지](https://www.acmicpc.net/) 문제 풀이를 기록하는 공간입니다.

## 📂 문제 목록
{table_header}{table_content}
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_readme)

if __name__ == "__main__":
    organize_solved_problems()  # 문제 정리 및 이동
    update_main_readme()  # 메인 README 업데이트
    print("✅ 문제 정리 및 README.md 업데이트 완료!")
