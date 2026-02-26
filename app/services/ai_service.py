import openai
import os
from dotenv import load_dotenv
import time

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

SYSTEM_PROMPT = "You are a helpful AI task summarizer."

def summarize_task(task_description: str):
    user_prompt = f"Summarize this task clearly:\n{task_description}"

    for attempt in range(2):  # Retry max 2
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt}
                ],
                timeout=10
            )

            return {
                "summary": response.choices[0].message.content,
                "tokens": response.usage.total_tokens
            }

        except Exception:
            time.sleep(1)

    return {"summary": "AI service temporarily unavailable.", "tokens": 0}