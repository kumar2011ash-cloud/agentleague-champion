"""
GitHub Repository Analyzer
Fetches and analyzes code from GitHub repositories
"""
import requests
from typing import List, Dict


class GitHubAnalyzer:
    """Fetches code files from GitHub repositories"""
    
    def __init__(self, github_token: str = None):
        self.github_token = github_token
        self.base_url = "https://api.github.com"
        self.headers = {}
        
        if github_token:
            self.headers["Authorization"] = f"token {github_token}"
        
        self.headers["Accept"] = "application/vnd.github.v3.raw"
    
    def get_repo_files(self, owner: str, repo: str, file_types: List[str] = None) -> Dict[str, str]:
        """
        Fetch code files from repository
        
        Args:
            owner: Repository owner
            repo: Repository name
            file_types: List of file extensions to fetch (e.g., ['.py', '.js'])
        
        Returns:
            Dictionary mapping file paths to file contents
        """
        if file_types is None:
            file_types = ['.py', '.js', '.ts', '.java', '.go']
        
        files = {}
        
        try:
            # Get repository structure
            response = requests.get(
                f"{self.base_url}/repos/{owner}/{repo}/git/trees/main?recursive=1",
                headers=self.headers
            )
            
            if response.status_code != 200:
                print(f"Error fetching repo: {response.status_code}")
                return files
            
            tree = response.json().get('tree', [])
            
            # Filter by file type
            code_files = [
                item for item in tree 
                if item['type'] == 'blob' and any(
                    item['path'].endswith(ft) for ft in file_types
                )
            ]
            
            # Fetch first 5 files (limit for demo)
            for file_obj in code_files[:5]:
                file_path = file_obj['path']
                print(f"📥 Fetching {file_path}...")
                
                file_response = requests.get(
                    f"{self.base_url}/repos/{owner}/{repo}/contents/{file_path}",
                    headers=self.headers
                )
                
                if file_response.status_code == 200:
                    files[file_path] = file_response.text
            
            return files
        
        except Exception as e:
            print(f"Error: {e}")
            return files
    
    @staticmethod
    def fetch_raw_file(url: str) -> str:
        """Fetch raw file from GitHub URL"""
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            return ""
        except Exception as e:
            print(f"Error fetching file: {e}")
            return ""


# Example usage
if __name__ == "__main__":
    analyzer = GitHubAnalyzer()
    
    # Analyze a sample repository
    files = analyzer.get_repo_files("torvalds", "linux", file_types=['.c'])
    
    print(f"Found {len(files)} files")
    for path in files.keys():
        print(f"  - {path}")
