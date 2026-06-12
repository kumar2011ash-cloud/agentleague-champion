"""
Fetch code from a GitHub repo and run the orchestrator to analyze it.
Usage: python run_on_repo.py owner repo
Defaults to psf/requests
"""
import sys
from github_analyzer import GitHubAnalyzer
from orchestrator import Orchestrator
from report_utils import to_structured, save_json


def main(owner='psf', repo='requests'):
    gh = GitHubAnalyzer()
    print(f'Fetching code files from {owner}/{repo}...')
    files = gh.get_repo_files(owner, repo)
    if not files:
        print('No files fetched; aborting')
        return
    # Concatenate up to first 10 files for analysis
    combined = '\n\n'.join(list(files.values())[:10])

    orch = Orchestrator()
    results = orch.run(combined, 'python')

    # Save markdown
    md = '# Repo Analysis Report for {}/{}\n\n'.format(owner, repo)
    for k, v in results.items():
        md += f'## {k.capitalize()}\n\n{v}\n\n'
    with open('repo_report.md', 'w', encoding='utf-8') as f:
        f.write(md)

    # Save JSON
    structured = to_structured(results)
    save_json('repo_report.json', structured)

    print('Wrote repo_report.md and repo_report.json')

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        main(sys.argv[1], sys.argv[2])
    else:
        main()
