"""
Research API Routes
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List

from app.agents.research_agent import ResearchAgent
from app.engines.chart_generator import ChartGenerator
from app.engines.infographic_generator import InfographicGenerator


router = APIRouter()

# Initialize agents and generators
research_agent = ResearchAgent()
chart_generator = ChartGenerator()
infographic_generator = InfographicGenerator()


class ResearchRequest(BaseModel):
    """Research request model"""
    query: str


class ResearchResponse(BaseModel):
    """Research response model"""
    query: str
    status: str
    charts: List[Dict[str, Any]]
    infographics: List[Dict[str, Any]]
    insights: Dict[str, Any]
    sources: List[Dict[str, str]]


@router.post("/", response_model=ResearchResponse)
async def conduct_research(request: ResearchRequest):
    """
    Conduct comprehensive research with visualizations

    Args:
        request: Research request with query

    Returns:
        Complete research results with charts and infographics
    """

    try:
        print(f"\n{'='*60}")
        print(f"NEW RESEARCH REQUEST: {request.query}")
        print(f"{'='*60}\n")

        # Step 1: Conduct research
        research_results = await research_agent.research(request.query)

        # Step 2: Generate charts
        charts = []
        structured_data = research_results.get("structured_data", {})
        query_analysis = research_results.get("query_analysis", {})
        visualizations = query_analysis.get("visualizations", {})

        # Generate trend chart if we have trend data
        if structured_data.get("trend_data"):
            print("Generating line chart...")
            trend_data = structured_data["trend_data"]
            # Convert string to list if needed
            if isinstance(trend_data, str):
                import json
                try:
                    trend_data = json.loads(trend_data)
                except:
                    trend_data = []
            if not isinstance(trend_data, list):
                trend_data = []

            if trend_data:  # Only generate if we have valid data
                line_chart = chart_generator.generate_chart(
                    "line",
                    trend_data,
                    f"{request.query} - Trend Over Time"
                )
                charts.append({
                    "type": "line",
                    "title": f"{request.query} - Trend Over Time",
                    "data": line_chart
                })

        # Generate comparison chart if we have comparison data
        if structured_data.get("comparison_data"):
            print("Generating bar chart...")
            comparison_data = structured_data["comparison_data"]
            # Convert string to list if needed
            if isinstance(comparison_data, str):
                import json
                try:
                    comparison_data = json.loads(comparison_data)
                except:
                    comparison_data = []
            if not isinstance(comparison_data, list):
                comparison_data = []

            if comparison_data:
                bar_chart = chart_generator.generate_chart(
                    "bar",
                    comparison_data,
                    f"{request.query} - Comparison"
                )
                charts.append({
                    "type": "bar",
                    "title": f"{request.query} - Comparison",
                    "data": bar_chart
                })

        # Generate distribution chart if we have distribution data
        if structured_data.get("distribution_data"):
            print("Generating pie chart...")
            distribution_data = structured_data["distribution_data"]
            # Convert string to list if needed
            if isinstance(distribution_data, str):
                import json
                try:
                    distribution_data = json.loads(distribution_data)
                except:
                    distribution_data = []
            if not isinstance(distribution_data, list):
                distribution_data = []

            if distribution_data:
                pie_chart = chart_generator.generate_chart(
                    "pie",
                    distribution_data,
                    f"{request.query} - Distribution"
                )
                charts.append({
                    "type": "pie",
                    "title": f"{request.query} - Distribution",
                    "data": pie_chart
                })

        # Step 3: Generate infographics
        infographics = []

        if structured_data.get("key_statistics"):
            print("Generating infographic...")
            stats_infographic = infographic_generator.generate_infographic(
                "statistics",
                structured_data,
                f"{request.query} - Key Insights"
            )
            infographics.append(stats_infographic)

        print(f"\nResearch complete!")
        print(f"   - Generated {len(charts)} charts")
        print(f"   - Generated {len(infographics)} infographics")
        print(f"   - Found {len(research_results.get('sources', []))} sources")
        print(f"{'='*60}\n")

        return ResearchResponse(
            query=request.query,
            status="completed",
            charts=charts,
            infographics=infographics,
            insights=research_results.get("insights", {}),
            sources=research_results.get("sources", [])
        )

    except Exception as e:
        print(f"ERROR during research: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/test")
async def test_research():
    """Test endpoint to verify research system is working"""

    try:
        test_query = "AI market trends 2024"
        result = await conduct_research(ResearchRequest(query=test_query))
        return {
            "status": "success",
            "message": "Research system is working!",
            "test_query": test_query,
            "charts_generated": len(result.charts),
            "infographics_generated": len(result.infographics)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Test failed: {str(e)}")
