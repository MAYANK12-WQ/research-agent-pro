"""
Research Agent Pro - Main FastAPI Application
The most sophisticated research agent with automatic visualizations
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import uvicorn

from app.core.config import settings

# Import routes
from app.api.routes import research


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events"""
    # Startup
    print(f"Starting {settings.APP_NAME} v{settings.APP_VERSION}")
    print(f"Environment: {settings.ENVIRONMENT}")
    print(f"API Keys configured:")
    print(f"  - Groq: {'YES' if settings.GROQ_API_KEY else 'NO'}")
    print(f"  - Serper: {'YES' if settings.SERPER_API_KEY else 'NO'}")
    print(f"  - Tavily: {'YES' if settings.TAVILY_API_KEY else 'NO'}")

    yield

    # Shutdown
    print(f"Shutting down {settings.APP_NAME}")


# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check endpoint
@app.get("/")
async def root():
    """Root endpoint - API info"""
    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "description": settings.APP_DESCRIPTION,
        "status": "running",
        "docs": "/docs",
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    # Check API keys
    api_keys_status = {
        "groq": bool(settings.GROQ_API_KEY),
        "serper": bool(settings.SERPER_API_KEY),
        "tavily": bool(settings.TAVILY_API_KEY),
    }

    all_keys_configured = all(api_keys_status.values())

    return {
        "status": "healthy" if all_keys_configured else "degraded",
        "api_keys": api_keys_status,
        "environment": settings.ENVIRONMENT,
    }


# Test endpoint for quick research
@app.post("/api/v1/research/quick")
async def quick_research(query: str):
    """Quick research endpoint (MVP)"""
    try:
        # For now, return a mock response
        # We'll implement the real agent in the next step
        return {
            "query": query,
            "status": "completed",
            "summary": f"Research for: {query} (coming soon!)",
            "charts": [],
            "infographics": [],
            "sources": [],
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Include routers
app.include_router(research.router, prefix="/api/v1/research", tags=["research"])


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.API_RELOAD,
    )
