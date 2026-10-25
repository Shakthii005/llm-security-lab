import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise SystemExit("GROQ_API_KEY is missing. Check your .env file.")

client = Groq(api_key=api_key)

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": (
                "Explain an overly permissive S3 bucket policy "
                "in three sentences."
            )
        }
    ],
    max_completion_tokens=300
)

print(response.choices[0].message.content)