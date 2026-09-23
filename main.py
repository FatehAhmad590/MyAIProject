import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: OPENAI_API_KEY পাওয়া যায়নি।")
    exit(1)

client = OpenAI(api_key=api_key)

print("--- OpenAI AI Bot Started ---")
print("AI-কে প্রশ্ন করুন। বের হতে 'exit' লিখুন।")

while True:
    try:
        user_input = input("\nআপনি: ").strip()
        if user_input.lower() == "exit":
            print("বিদায়!")
            break
        if not user_input:
            continue

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful and smart AI assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        print(f"AI Assistant: {response.choices.message.content}")
    except Exception as e:
        print(f"একটি সমস্যা হয়েছে: {e}")
