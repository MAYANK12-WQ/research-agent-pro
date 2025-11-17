"""
Configuration settings for Research Agent Pro
"""
from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    """Application settings"""

    # App Info
    APP_NAME: str = "Research Agent Pro"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Sophisticated AI research agent with automatic visualizations"

    # Environment
    ENVIRONMENT: str = "development"

    # API Settings
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_RELOAD: bool = True

    # CORS
    CORS_ORIGINS: str = "http://localhost:3000,http://localhost:3001,http://127.0.0.1:3000,null"

    @property
    def cors_origins_list(self) -> List[str]:
        """Parse CORS_ORIGINS from comma-separated string"""
        origins = [origin.strip() for origin in self.CORS_ORIGINS.split(",")]
        # Allow all origins in development for testing
        if self.ENVIRONMENT == "development":
            return ["*"]
        return origins

    # LLM API Keys
    GROQ_API_KEY: str = ""
    DEEPSEEK_API_KEY: str = ""
    OPENAI_API_KEY: str = ""

    # Search API Keys
    SERPER_API_KEY: str = ""
    TAVILY_API_KEY: str = ""
    BRAVE_SEARCH_API_KEY: str = ""

    # Scraping
    SCRAPER_API_KEY: str = ""

    # Optional Data Sources
    NEWS_API_KEY: str = ""
    ALPHA_VANTAGE_KEY: str = ""

    # Database
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/research_agent"

    # Redis
    REDIS_URL: str = "redis://localhost:6379"

    # Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = 60

    # Image Generation (Optional)
    STABILITY_API_KEY: str = ""
    UNSPLASH_ACCESS_KEY: str = ""

    # LLM Settings
    DEFAULT_LLM_MODEL: str = "llama-3.3-70b-versatile"  # Groq model
    LLM_TEMPERATURE: float = 0.3
    LLM_MAX_TOKENS: int = 4096

    # Research Settings
    MAX_SEARCH_RESULTS: int = 10
    MAX_SCRAPE_PAGES: int = 5
    RESEARCH_TIMEOUT: int = 30  # seconds

    # Visualization Settings
    CHART_WIDTH: int = 800
    CHART_HEIGHT: int = 500
    INFOGRAPHIC_WIDTH: int = 1200
    INFOGRAPHIC_HEIGHT: int = 1600

    class Config:
        env_file = ".env"
        case_sensitive = True


# Create global settings instance
settings = Settings()


def get_settings() -> Settings:
    """Get application settings"""
    return settings
