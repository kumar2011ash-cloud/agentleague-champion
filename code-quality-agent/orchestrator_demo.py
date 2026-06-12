"""Run the orchestrator and save an aggregated markdown report."""
from orchestrator import Orchestrator
from agent import CodeQualityAgent

if __name__ == '__main__':
    sample_code = '''
# Example vulnerable code

def process(user_id, data):
    db = open_db()
    query = f"SELECT * FROM users WHERE id = {user_id}"
    user = db.execute(query)
    return user
'''
    orch = Orchestrator()
    results = orch.run(sample_code, 'python')

    # Convert to a report format
    report = '# Aggregated Multi-Agent Report\n\n'
    for k, v in results.items():
        report += f'## {k.capitalize()}\n\n'
        report += v + '\n\n'

    with open('aggregated_report.md', 'w', encoding='utf-8') as f:
        f.write(report)

    print('Aggregated report written to aggregated_report.md')
