import openai
import json
import os
from openai import OpenAI

def call_openai(prompt, model="gpt-3.5-turbo", max_tokens=500):
    try:
        # Initialize client with API key from environment
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens
        )
        content = response.choices[0].message.content.strip()
        
        # Try to parse JSON if possible
        if content.startswith('{') or content.startswith('['):
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                pass
        return content
    except Exception as e:
        return {"error": f"OpenAI API error: {str(e)}"}
