"""
Orchestrator to run multiple specialized agents in parallel and aggregate results.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict
from agent import CodeQualityAgent

class Orchestrator:
    def __init__(self):
        self.agent = CodeQualityAgent()
        self.tasks = {
            'code_quality': self.agent._code_reviewer,
            'security': self.agent._security_analyzer,
            'performance': self.agent._performance_analyzer,
            'architecture': self.agent._architecture_reviewer,
            'documentation': self.agent._documentation_analyzer if hasattr(self.agent, '_documentation_analyzer') else (lambda c,l: 'No documentation analyzer configured')
        }

    def run(self, code: str, language: str = 'python') -> Dict[str, str]:
        results = {}
        with ThreadPoolExecutor(max_workers=len(self.tasks)) as ex:
            futures = {ex.submit(func, code, language): name for name, func in self.tasks.items()}
            for fut in as_completed(futures):
                name = futures[fut]
                try:
                    results[name] = fut.result()
                except Exception as e:
                    results[name] = f'Error: {e}'
        return results

if __name__ == '__main__':
    # Simple CLI demo
    sample_code = '''
def unsafe_query(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return execute_db(query)
'''
    orch = Orchestrator()
    res = orch.run(sample_code, 'python')
    import json
    print(json.dumps(res, indent=2))
