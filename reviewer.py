import openai
import os
import argparse

def get_review(filepath):
    with open(filepath,"r") as file:
        content = file.read()
    code_review = make_code_review(content)
    print(code_review)

def make_code_review(filecontent:str) -> str:

    PROMPT = """
    You will receive a file's contents as text.
    Generate a code review for the file. Indicate what changes should be made to improve
    its style, performance, readability, and maintainability. If there are any reputable
    libraries that could be introduced to imporve the code, suggest them. Be kind and constructive.
    For each suggested change, include line numbers to which you are referring.
    """
    messages = [
        {"role":"system", "content":PROMPT},
        {"role":"user", "content":f"Code review the following file: {filecontent}"}
    ]

    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return (res["choices"][0]["message"]["content"])

def main():
    openai.api_key = os.getenv("OpenAIKey")
    parser = argparse.ArgumentParser(description="Simple code reviewer for a file")
    parser.add_argument("file")
    args=parser.parse_args()
    get_review(args.file)

if __name__ == "__main__":
    main()
