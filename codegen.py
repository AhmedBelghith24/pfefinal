# import json

# # Load the filtered JSON data from the file
# filtered_file_path = "/Users/ahmedbelghith/Desktop/app/Pfe/filtreddata.json"
# with open(filtered_file_path, "r") as f:
#     problems = json.load(f)

# # Function to generate a generic solution code for a given problem
# def generate_solution_code(problem_header, problem_content):
#     solution_code = f"""
# {problem_header}
#     # Your implementation here
#     pass
# """
#     return solution_code

# # Generate solution codes for the first three problems
# solutions = []
# for problem in problems[:3]:
#     solution_code = generate_solution_code(problem["problem_header"], problem["problem_content"])
#     solutions.append({
#         "title": problem["title"],
#         "problem_header": problem["problem_header"],
#         "problem_content": problem["problem_content"],
#         "solution_code": solution_code
#     })

# # Save the solutions to a new JSON file
# output_file_path = "/Users/ahmedbelghith/Desktop/app/Pfe/solutions.json"
# with open(output_file_path, "w") as f:
#     json.dump(solutions, f, indent=4)

# print(f"Solution codes for the first three problems have been saved to {output_file_path}")


import json
import openai

# Replace with your OpenAI API key
openai.api_key = 'sk-proj-ClML4UKuEmJ5P0eGKfeET3BlbkFJ4uZZPXqc3VINVO7q0Gav'

# Load the filtered JSON data from the file
filtered_file_path = "/Users/ahmedbelghith/Desktop/app/Pfe/filtreddata.json"
with open(filtered_file_path, "r") as f:
    problems = json.load(f)

# Function to generate solution code using GPT-4 API
def generate_solution_code(problem_header, problem_content):
    prompt = f"""
Problem Content:
{problem_content}

Problem Header:
{problem_header}

Please provide the complete implementation for the problem described above. Do not include any explanations, comments, or markdown, just the code.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1500,
        n=1,
        stop=None,
        temperature=0.5,
    )
    solution_code = response['choices'][0]['message']['content'].strip()

    # Remove any leading or trailing markdown code block indicators
    if solution_code.startswith("```") and solution_code.endswith("```"):
        solution_code = solution_code[3:-3].strip()
    elif solution_code.startswith("```python") and solution_code.endswith("```"):
        solution_code = solution_code[10:-3].strip()

    return solution_code

# Generate solution codes for the first three problems
solutions = []
for problem in problems[:3]:
    solution_code = generate_solution_code(problem["problem_header"], problem["problem_content"])
    solutions.append({
        "title": problem["title"],
        "problem_header": problem["problem_header"],
        "problem_content": problem["problem_content"],
        "solution_code": solution_code
    })

# Save the solutions to a new JSON file
output_file_path = "/Users/ahmedbelghith/Desktop/app/Pfe/solutions.json"
with open(output_file_path, "w") as f:
    json.dump(solutions, f, indent=4)

print(f"Solution codes for the first three problems have been saved to {output_file_path}")
