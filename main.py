import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("No API Key Found")

client = genai.Client(api_key=api_key)
model = "gemini-2.5-flash"
content = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

def main():
    print("Hello from aiagent!")

    response = client.models.generate_content(model=model, contents=content)
    if response.usage_metadata == None:
        raise RuntimeError("No response metadata found. Possible failed API request.")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(response.text)

if __name__ == "__main__":
    main()
