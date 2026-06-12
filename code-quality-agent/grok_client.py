"""
Lightweight Grok HTTP client using `requests`.
"""
import requests
from typing import List, Dict

class GrokClient:
    def __init__(self, api_key: str, base_url: str = "https://api.x.ai/v1"):
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        })

    def create_chat_completion(self, model: str, messages: List[Dict], temperature: float = 0.7, max_tokens: int = 1000) -> Dict:
        url = f"{self.base_url}/chat/completions"
        payload = {
            'model': model,
            'messages': messages,
            'temperature': temperature,
            'max_tokens': max_tokens
        }
        resp = self.session.post(url, json=payload, timeout=30)
        resp.raise_for_status()
        return resp.json()


if __name__ == '__main__':
    print('GrokClient ready')
