"""
Utilities to convert analysis into structured JSON and send webhook notifications.
"""
import json
import re
import requests
from typing import Dict

SEVERITY_KEYWORDS = {
    'critical': ['critical', 'severity: critical', 'CRITICAL'],
    'high': ['high', 'severity: high', 'HIGH'],
    'medium': ['medium', 'severity: medium', 'MEDIUM'],
    'low': ['low', 'severity: low', 'LOW']
}


def detect_severity(text: str) -> str:
    txt = text.lower()
    for level, kws in SEVERITY_KEYWORDS.items():
        for kw in kws:
            if kw.lower() in txt:
                return level
    return 'info'


def to_structured(analysis: Dict[str, str]) -> Dict:
    """Convert raw analysis map to structured JSON with severity and summary."""
    structured = {'summary': [], 'details': {}}
    for key, value in analysis.items():
        sev = detect_severity(value)
        # Create a short summary line (first sentence)
        summary_line = re.split(r'\n|\\n|\.|!|\?', value.strip())[0]
        structured['summary'].append({'area': key, 'severity': sev, 'summary': summary_line})
        structured['details'][key] = {'severity': sev, 'content': value}
    # Order summary by severity
    order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3, 'info': 4}
    structured['summary'].sort(key=lambda x: order.get(x['severity'], 4))
    return structured


def save_json(path: str, data: Dict):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


def send_webhook(url: str, payload: Dict):
    headers = {'Content-Type': 'application/json'}
    resp = requests.post(url, json=payload, headers=headers, timeout=10)
    resp.raise_for_status()
    return resp.status_code

if __name__ == '__main__':
    print('report_utils ready')
