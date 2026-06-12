# 🚀 Multi-Agent Code Quality Analyzer

## Overview
A sophisticated multi-agent AI system that analyzes code repositories and provides comprehensive quality reports. Perfect for Agent League hackathon - demonstrates reasoning, multi-agent coordination, and enterprise-grade analysis.

## 🎯 Features

### Multi-Agent Architecture
- **Code Reviewer Agent** - Evaluates readability, maintainability, and best practices
- **Security Analyzer Agent** - Identifies vulnerabilities and security risks
- **Performance Analyzer Agent** - Detects bottlenecks and optimization opportunities
- **Architecture Reviewer Agent** - Reviews design patterns and system design
- **Documentation Analyzer Agent** - Assesses documentation quality

### Output
- Structured analysis from each specialized agent
- Comprehensive markdown reports
- Actionable recommendations

## 🛠️ Tech Stack
- **Python 3.10+**
- **Grok API** (via OpenAI SDK)
- **CrewAI** (for future multi-agent orchestration)

## 📦 Installation

```bash
# Navigate to the agent directory
cd code-quality-agent

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Usage

### Basic Analysis
```python
from agent import CodeQualityAgent

agent = CodeQualityAgent()

code = '''
def process_data(user_id, data):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    # ... rest of code
'''

results = agent.analyze_code(code, language="python")
report = agent.generate_report(results)
print(report)
```

### Run Demo
```bash
python agent.py
```

This will:
1. Analyze sample vulnerable code
2. Generate a comprehensive report
3. Save report to `code_quality_report.md`

## 📊 What Gets Analyzed

### Code Quality
- Readability and maintainability
- Naming conventions
- Code organization
- DRY principle adherence
- Error handling

### Security
- Injection vulnerabilities
- Authentication issues
- Data exposure risks
- Unsafe dependencies
- Cryptographic weaknesses

### Performance
- Time/space complexity
- Memory leaks
- Caching opportunities
- Database optimization
- Bottleneck detection

### Architecture
- Design patterns
- Separation of concerns
- Modularity and coupling
- Scalability
- SOLID principles

## 🎬 Agent League Value Proposition

✅ **Reasoning**: Multiple agents collaborate to analyze code from different perspectives
✅ **Enterprise Use**: Can analyze any codebase for security, performance, quality
✅ **Scalability**: Extensible to add more specialized agents
✅ **Actionable Output**: Provides concrete recommendations with severity levels
✅ **Innovation**: Demonstrates advanced multi-agent coordination

## 📝 Environment Setup

Create `.env` file:
```
GROK_API_KEY=your_grok_api_key_here
```

## 🔄 Future Enhancements
- GitHub repository integration
- Real-time code monitoring
- Compliance checking (GDPR, SOC2)
- Cost estimation
- Automated remediation suggestions
- Integration with CI/CD pipelines

## 📧 Support
For Agent League hackathon queries, contact the team.
