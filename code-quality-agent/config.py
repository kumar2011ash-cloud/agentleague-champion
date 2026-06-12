"""
Configuration for Code Quality Agent
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration"""
    
    # API Keys
    GROK_API_KEY = os.getenv("GROK_API_KEY")
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", None)
    
    # API Endpoints
    GROK_BASE_URL = "https://api.x.ai/v1"
    GROK_MODEL = "grok-beta"
    # Use mock mode to avoid calling external APIs during demos
    MOCK = os.getenv("MOCK", "false").lower() in ("1", "true", "yes")
    
    # Analysis Settings
    MAX_CODE_LENGTH = 10000  # Max characters to analyze
    TEMPERATURE = 0.7  # Grok response temperature
    MAX_TOKENS = 1000  # Max tokens per analysis
    
    # File Types
    CODE_EXTENSIONS = [
        '.py', '.js', '.ts', '.java', '.go', '.cpp', 
        '.c', '.rb', '.php', '.swift', '.kt', '.rs'
    ]
    
    @staticmethod
    def validate():
        """Validate configuration"""
        if not Config.GROK_API_KEY:
            raise ValueError("GROK_API_KEY not set in .env file")
        return True
