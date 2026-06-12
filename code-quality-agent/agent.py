"""
Multi-Agent Code Quality Analyzer
Analyzes code repositories and provides comprehensive quality reports
"""
import os
import json
from typing import Dict, List
from dotenv import load_dotenv
from config import Config

load_dotenv()

class CodeQualityAgent:
    """Main orchestrator for code quality analysis"""
    
    def __init__(self):
        # Use mock mode if configured
        self.mock = Config.MOCK
        if not self.mock:
            Config.validate()
            # Use a lightweight HTTP client to call Grok-compatible endpoint
            try:
                from grok_client import GrokClient
            except Exception:
                raise RuntimeError("grok_client import failed. Ensure grok_client.py exists and dependencies (requests) are installed")

            self.client = GrokClient(api_key=Config.GROK_API_KEY, base_url=Config.GROK_BASE_URL)
        else:
            self.client = None
        
        # Define specialized agents
        self.agents = {
            "code_reviewer": "Analyzes code structure, readability, and best practices",
            "security_analyzer": "Identifies security vulnerabilities and risks",
            "performance_analyzer": "Evaluates performance issues and optimization opportunities",
            "architecture_reviewer": "Reviews system design and architecture patterns",
            "documentation_analyzer": "Assesses documentation quality and completeness"
        }
    
    def analyze_code(self, code_snippet: str, language: str = "python") -> Dict:
        """
        Orchestrates analysis using multiple specialized agents
        """
        print(f"🔍 Starting multi-agent analysis for {language} code...")
        
        results = {}
        
        # Agent 1: Code Quality Review
        results["code_quality"] = self._code_reviewer(code_snippet, language)
        print("✅ Code Quality Review completed")
        
        # Agent 2: Security Analysis
        results["security"] = self._security_analyzer(code_snippet, language)
        print("✅ Security Analysis completed")
        
        # Agent 3: Performance Analysis
        results["performance"] = self._performance_analyzer(code_snippet, language)
        print("✅ Performance Analysis completed")
        
        # Agent 4: Architecture Review
        results["architecture"] = self._architecture_reviewer(code_snippet, language)
        print("✅ Architecture Review completed")
        
        return results
    
    def _code_reviewer(self, code: str, language: str) -> str:
        """Agent: Code Quality Reviewer"""
        prompt = f"""You are an expert {language} code reviewer. Analyze this code and provide feedback on:
1. Code readability and maintainability
2. Naming conventions and consistency
3. Code organization and structure
4. DRY principle adherence
5. Error handling

Code:
```{language}
{code}
```

Provide a concise, actionable review."""
        
        return self._query_grok(prompt)
    
    def _security_analyzer(self, code: str, language: str) -> str:
        """Agent: Security Vulnerability Detector"""
        prompt = f"""You are a security expert specializing in {language}. Analyze this code for:
1. Injection vulnerabilities
2. Authentication/Authorization issues
3. Data exposure risks
4. Unsafe dependencies
5. Cryptographic weaknesses

Code:
```{language}
{code}
```

List vulnerabilities with severity levels (Critical, High, Medium, Low)."""
        
        return self._query_grok(prompt)
    
    def _performance_analyzer(self, code: str, language: str) -> str:
        """Agent: Performance Optimization Analyzer"""
        prompt = f"""You are a performance optimization expert for {language}. Analyze this code for:
1. Time complexity issues
2. Memory leaks or inefficiencies
3. Database query optimization
4. Caching opportunities
5. Bottlenecks

Code:
```{language}
{code}
```

Suggest specific optimizations with expected improvements."""
        
        return self._query_grok(prompt)
    
    def _architecture_reviewer(self, code: str, language: str) -> str:
        """Agent: Architecture and Design Patterns"""
        prompt = f"""You are a software architect. Review this {language} code for:
1. Design pattern implementation
2. Separation of concerns
3. Modularity and coupling
4. Scalability considerations
5. SOLID principles adherence

Code:
```{language}
{code}
```

Provide architectural recommendations."""
        
        return self._query_grok(prompt)
    
    def _query_grok(self, prompt: str) -> str:
        """Query Grok API"""
        if self.mock:
            return self._mock_response(prompt)

        try:
            messages = [
                {"role": "system", "content": "You are an expert software engineer providing detailed code analysis."},
                {"role": "user", "content": prompt}
            ]
            resp = self.client.create_chat_completion(
                model=Config.GROK_MODEL,
                messages=messages,
                temperature=Config.TEMPERATURE,
                max_tokens=Config.MAX_TOKENS
            )
            # Expecting an OpenAI-like response structure
            choice = resp.get('choices', [{}])[0]
            message = choice.get('message') or choice.get('text') or {}
            if isinstance(message, dict):
                return message.get('content', '')
            if isinstance(choice.get('text'), str):
                return choice.get('text')
            return str(resp)
        except Exception as e:
            return f"Error analyzing code: {str(e)}"

    def _mock_response(self, prompt: str) -> str:
        """Return a canned response for demos when MOCK is enabled."""
        # Basic heuristics to decide response type
        if "Injection" in prompt or "injection" in prompt or "SQL" in prompt:
            return (
                "- Potential SQL injection where user input is interpolated into queries.\n"
                "- Recommendation: Use parameterized queries or ORM parameter binding.\n"
                "Severity: Critical"
            )
        if "performance" in prompt or "Time complexity" in prompt:
            return (
                "- Nested loops detected leading to O(n^2) complexity.\n"
                "- Recommendation: Refactor algorithm to reduce nested iterations or use vectorized operations.\n"
                "Estimated improvement: 5-20x depending on dataset.\n"
            )
        if "security" in prompt or "Authentication" in prompt:
            return (
                "- No authentication checks observed for sensitive operations.\n"
                "- Recommendation: Enforce authN/authZ, validate inputs, and sanitize outputs.\n"
                "Severity: High"
            )
        # Default mock reply
        return (
            "- Code looks like it needs improved error handling and clearer naming.\n"
            "- Recommendation: Add try/except blocks around I/O and database calls, and use descriptive variable names.\n"
            "- Consider adding unit tests for core logic.\n"
        )
    
    def generate_report(self, analysis_results: Dict) -> str:
        """Generate a comprehensive markdown report"""
        report = "# 📊 Code Quality Analysis Report\n\n"
        report += "Generated by Multi-Agent Code Quality Analyzer\n\n"
        report += "---\n\n"
        
        report += "## 🔍 Code Quality Review\n"
        report += analysis_results.get("code_quality", "No analysis") + "\n\n"
        
        report += "## 🔐 Security Analysis\n"
        report += analysis_results.get("security", "No analysis") + "\n\n"
        
        report += "## ⚡ Performance Analysis\n"
        report += analysis_results.get("performance", "No analysis") + "\n\n"
        
        report += "## 🏗️ Architecture Review\n"
        report += analysis_results.get("architecture", "No analysis") + "\n\n"
        
        report += "---\n"
        report += "*Report generated by AgentLeague Multi-Agent Code Quality Analyzer*"
        
        return report


def main():
    """Demo: Analyze sample code"""
    
    # Sample code to analyze
    sample_code = '''
def process_user_data(user_id, data):
    """Process user data"""
    db = open_database()  # Direct connection
    query = f"SELECT * FROM users WHERE id = {user_id}"  # SQL injection!
    user = db.execute(query)
    
    for item in data:
        result = calculate(item)
        results = results + [result]  # O(n²) complexity
    
    return results

def calculate(x):
    if x < 0:
        return None
    total = 0
    for i in range(x):
        for j in range(x):
            total += i * j
    return total
'''
    
    # Initialize agent
    agent = CodeQualityAgent()
    
    # Run analysis
    results = agent.analyze_code(sample_code, language="python")
    
    # Generate report
    report = agent.generate_report(results)
    
    # Save report (use UTF-8 encoding to support emojis and special chars)
    with open("code_quality_report.md", "w", encoding="utf-8") as f:
        f.write(report)
    
    print("\n✅ Analysis complete! Report saved to code_quality_report.md")
    print("\n" + "="*60)
    print(report)


if __name__ == "__main__":
    main()
