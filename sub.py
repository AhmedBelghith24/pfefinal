import os
import requests
import time
import subprocess
import json

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

    max_retries = 5
    for attempt in range(max_retries):
        try:
            response = requests.post(url, json=payload, headers=headers)

            # Debugging output
            print(f"Attempt: {attempt + 1}")
            print(f"Status Code: {response.status_code}")
            print(f"Response Headers: {response.headers}")
            print(f"Response Text: {response.text[:500]}")  # Print the first 500 characters of the response text

            if response.status_code == 200:
                try:
                    response_json = response.json()
                    return {
                        "status_code": response.status_code,
                        "response_headers": dict(response.headers),
                        "response_json": response_json
                    }
                except ValueError as e:
                    return {
                        "status_code": response.status_code,
                        "response_headers": dict(response.headers),
                        "response_text": response.text,
                        "json_decode_error": str(e)
                    }
            
            if response.status_code == 429:
                retry_after = int(response.headers.get("Retry-After", 2 ** attempt))
                print(f"Rate limit exceeded. Retrying after {retry_after} seconds...")
                time.sleep(retry_after)
            elif response.status_code == 500:
                print("Internal server error. Retrying after a short delay...")
                time.sleep(2 ** attempt)
            else:
                time.sleep(2 ** attempt)  # Exponential backoff for other errors

        except requests.RequestException as e:
            print(f"Request failed: {e}")
            time.sleep(2 ** attempt)

    return {
        "status_code": response.status_code,
        "response_headers": dict(response.headers),
        "response_text": response.text
    }

def write_result_to_file(result, file_path="result.json"):
    with open(file_path, "w") as file:
        json.dump(result, file, indent=4)

def commit_and_push(file_path, message="Update result"):
    # Set git user email and name
    subprocess.run(["git", "config", "--global", "user.email", "abelghith@oakland.edu"], check=True)  # Replace with your GitHub email
    subprocess.run(["git", "config", "--global", "user.name", "AhmedBelghith24"], check=True)  # Replace with your GitHub name
    # Add, commit, and push the file
    subprocess.run(["git", "add", file_path], check=True)
    subprocess.run(["git", "commit", "-m", message], check=True)
    # Use the personal access token to push changes
    repo_url = f"https://{os.getenv('PERSONAL_ACCESS_TOKEN')}@github.com/AhmedBelghith24/pfefinal.git"
    subprocess.run(["git", "push", repo_url, "main"], check=True)  # or the appropriate branch

if __name__ == "__main__":
    question_slug = "two-sum"  # Replace with the actual question slug
    file_path = "solution.py"  # Path to the solution file
    result_file_path = "result.json"

    with open(file_path, 'r') as file:
        code = file.read()

    result = submit_solution(question_slug, code)
    write_result_to_file(result, result_file_path)
    commit_and_push(result_file_path, "Update LeetCode submission result")
