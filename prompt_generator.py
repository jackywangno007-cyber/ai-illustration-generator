import json
from openai import OpenAI
from config.settings import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, DEEPSEEK_MODEL
from prompt_builder import build_system_prompt


def generate_prompt(user_input: str) -> dict:
    if not DEEPSEEK_API_KEY:
        raise ValueError(
            "DEEPSEEK_API_KEY is not set. Please check your .env file.")

    client = OpenAI(
        api_key=DEEPSEEK_API_KEY,
        base_url=DEEPSEEK_BASE_URL
    )

    system_prompt = build_system_prompt()

    user_prompt = f"""
User request:
{user_input}

Please return the result in valid JSON format like this:
{{
    "main_prompt": "...",
    "negative_prompt": "...",
    "style": "...",
    "aspect_ratio": "...",
    "chinese_summary": "..."
}}
"""

    response = client.chat.completions.create(
        model=DEEPSEEK_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.8
    )

    content = response.choices[0].message.content.strip()

    # 处理模型返回的 Markdown 代码块
    if content.startswith("```json"):
        content = content[len("```json"):].strip()
        if content.endswith("```"):
            content = content[:-3].strip()
    elif content.startswith("```"):
        content = content[3:].strip()
        if content.endswith("```"):
            content = content[:-3].strip()

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {
            "main_prompt": content,
            "negative_prompt": "",
            "style": "",
            "aspect_ratio": "",
            "chinese_summary": "模型未返回标准 JSON，已保留原始输出。"
        }
