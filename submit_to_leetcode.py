import os
import requests

def submit_solution(question_slug, code):
    url = f"https://leetcode.com/problems/{question_slug}/submit/"
    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/problems/{question_slug}/",
        "X-CSRFToken": os.getenv("LEETCODE_CSRFTOKEN"),
        "Cookie": f"LEETCODE_SESSION={os.getenv('LEETCODE_SESSION')}; csrftoken={os.getenv('LEETCODE_CSRFTOKEN')}"
    }

    payload = {
        "lang": "python3",
        "question_id": question_slug,
        "typed_code": code
    }

    response = requests.post(url, json=payload, headers=headers)

    # Debugging output
    print("Status Code:", response.status_code)
    print("Response Headers:", response.headers)
    print("Response Text:", response.text)

    try:
        response_json = response.json()
        print(response_json)
    except ValueError as e:
        print("JSON decode error:", e)
        print("Response text was not JSON:", response.text)

if __name__ == "__main__":
    question_slug = "two-sum"  # Replace with the actual question slug
    file_path = "solution.py"  # Path to the solution file

    with open(file_path, 'r') as file:
        code = file.read()

    submit_solution(question_slug, code)
