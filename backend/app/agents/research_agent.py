"""
Research Agent - Main research orchestrator with Groq, Serper, and Tavily
"""
import os
import asyncio
import json
from typing import Dict, List, Any
import httpx
from groq import Groq

from app.core.config import settings


class ResearchAgent:
    """Main research agent that orchestrates web search and AI analysis"""

    def __init__(self):
        self.groq_client = Groq(api_key=settings.GROQ_API_KEY)
        self.serper_key = settings.SERPER_API_KEY
        self.tavily_key = settings.TAVILY_API_KEY

    async def research(self, query: str) -> Dict[str, Any]:
        """
        Conduct comprehensive research on a query

        Args:
            query: The research question

        Returns:
            Dict with research results, insights, and visualization data
        """
        print(f"Starting research for: {query}")

        # Step 1: Analyze query and determine what visualizations are needed
        query_analysis = await self._analyze_query(query)

        # Step 2: Gather data from multiple sources in parallel
        search_results = await self._gather_data(query)

        # Step 3: Extract and structure data for visualizations
        structured_data = await self._extract_structured_data(
            query,
            search_results,
            query_analysis
        )

        # Step 4: Generate insights and summary
        insights = await self._generate_insights(query, structured_data)

        return {
            "query": query,
            "query_analysis": query_analysis,
            "structured_data": structured_data,
            "insights": insights,
            "sources": search_results.get("sources", []),
            "status": "completed"
        }

    async def _analyze_query(self, query: str) -> Dict[str, Any]:
        """Analyze query to determine intent and required visualizations"""

        prompt = f"""Analyze this research query and determine:
1. What type of data is needed (trends, comparisons, distributions, etc.)
2. What visualizations would be most appropriate
3. What specific data points to extract

Query: {query}

Respond in JSON format:
{{
    "intent": "trend_analysis|comparison|distribution|statistics",
    "data_needed": ["specific data points to look for"],
    "visualizations": {{
        "primary": "line_chart|bar_chart|pie_chart|scatter|heatmap",
        "secondary": ["additional chart types"],
        "infographic_type": "statistics|timeline|comparison|geographic"
    }},
    "key_metrics": ["metric1", "metric2", "metric3"]
}}
"""

        try:
            response = self.groq_client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=settings.DEFAULT_LLM_MODEL,
                temperature=0.2,
                response_format={"type": "json_object"}
            )

            analysis = json.loads(response.choices[0].message.content)
            print(f"Query analysis: {analysis['intent']}")
            return analysis

        except Exception as e:
            print(f"WARNING: Query analysis error: {e}")
            # Default fallback
            return {
                "intent": "general_research",
                "data_needed": ["statistics", "trends", "key facts"],
                "visualizations": {
                    "primary": "bar_chart",
                    "secondary": ["line_chart"],
                    "infographic_type": "statistics"
                },
                "key_metrics": ["key statistics"]
            }

    async def _gather_data(self, query: str) -> Dict[str, Any]:
        """Gather data from multiple sources in parallel"""

        async with httpx.AsyncClient() as client:
            # Run searches in parallel
            serper_task = self._search_serper(client, query)
            tavily_task = self._search_tavily(client, query)

            serper_results, tavily_results = await asyncio.gather(
                serper_task,
                tavily_task,
                return_exceptions=True
            )

            # Combine results
            all_results = []
            sources = []

            if not isinstance(serper_results, Exception):
                all_results.extend(serper_results.get("organic", [])[:5])
                sources.extend([
                    {"title": r.get("title"), "url": r.get("link")}
                    for r in serper_results.get("organic", [])[:5]
                ])

            if not isinstance(tavily_results, Exception):
                all_results.extend(tavily_results.get("results", [])[:5])
                sources.extend([
                    {"title": r.get("title"), "url": r.get("url")}
                    for r in tavily_results.get("results", [])[:5]
                ])

            print(f"Gathered {len(all_results)} results from {len(sources)} sources")

            return {
                "results": all_results,
                "sources": sources
            }

    async def _search_serper(self, client: httpx.AsyncClient, query: str) -> Dict:
        """Search using Serper (Google Search API)"""

        try:
            response = await client.post(
                "https://google.serper.dev/search",
                headers={
                    "X-API-KEY": self.serper_key,
                    "Content-Type": "application/json"
                },
                json={"q": query, "num": 10},
                timeout=10.0
            )
            response.raise_for_status()
            print("Serper search completed")
            return response.json()
        except Exception as e:
            print(f"WARNING: Serper search failed: {e}")
            return {"organic": []}

    async def _search_tavily(self, client: httpx.AsyncClient, query: str) -> Dict:
        """Search using Tavily (AI Research API)"""

        try:
            response = await client.post(
                "https://api.tavily.com/search",
                headers={"Content-Type": "application/json"},
                json={
                    "api_key": self.tavily_key,
                    "query": query,
                    "search_depth": "advanced",
                    "max_results": 10
                },
                timeout=15.0
            )
            response.raise_for_status()
            print("Tavily search completed")
            return response.json()
        except Exception as e:
            print(f"WARNING: Tavily search failed: {e}")
            return {"results": []}

    async def _extract_structured_data(
        self,
        query: str,
        search_results: Dict,
        query_analysis: Dict
    ) -> Dict[str, Any]:
        """Extract and structure data for visualizations using AI"""

        # Combine all search results into text
        results_text = "\n\n".join([
            f"Source {i+1}: {r.get('title', '')} - {r.get('snippet', r.get('content', ''))}"
            for i, r in enumerate(search_results.get("results", [])[:10])
        ])

        prompt = f"""Based on this research query and search results, extract structured data for visualizations.

Query: {query}

Search Results:
{results_text}

Extract data for these visualization types: {query_analysis.get('visualizations', {})}

Provide structured data in JSON format:
{{
    "trend_data": [
        {{"year": "2020", "value": 100}},
        {{"year": "2021", "value": 150}},
        ...
    ],
    "comparison_data": [
        {{"category": "Item1", "value": 50}},
        {{"category": "Item2", "value": 75}},
        ...
    ],
    "distribution_data": [
        {{"name": "Segment1", "value": 35, "color": "#3B82F6"}},
        {{"name": "Segment2", "value": 45, "color": "#8B5CF6"}},
        ...
    ],
    "key_statistics": [
        {{"label": "Total Value", "value": "$127B", "icon": "dollar"}},
        {{"label": "Growth Rate", "value": "+43%", "icon": "trending_up"}},
        {{"label": "Market Size", "value": "2,847", "icon": "users"}}
    ]
}}

IMPORTANT: Use real numbers from the search results. If exact numbers aren't available, provide reasonable estimates based on the context.
"""

        try:
            response = self.groq_client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=settings.DEFAULT_LLM_MODEL,
                temperature=0.3,
                response_format={"type": "json_object"}
            )

            structured_data = json.loads(response.choices[0].message.content)
            print(f"Extracted structured data with {len(structured_data)} data sets")
            return structured_data

        except Exception as e:
            print(f"WARNING: Data extraction error: {e}")
            # Return sample data as fallback
            return self._get_sample_data(query)

    async def _generate_insights(self, query: str, structured_data: Dict) -> Dict[str, Any]:
        """Generate AI insights and summary"""

        prompt = f"""Based on this research query and extracted data, provide insightful analysis.

Query: {query}

Data: {json.dumps(structured_data, indent=2)}

Provide analysis in JSON format:
{{
    "summary": "2-3 paragraph summary of key findings",
    "key_insights": [
        "Insight 1 with specific numbers",
        "Insight 2 with trends",
        "Insight 3 with implications"
    ],
    "recommendations": ["Recommendation 1", "Recommendation 2"]
}}
"""

        try:
            response = self.groq_client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=settings.DEFAULT_LLM_MODEL,
                temperature=0.5,
                response_format={"type": "json_object"}
            )

            insights = json.loads(response.choices[0].message.content)
            print("Generated insights")
            return insights

        except Exception as e:
            print(f"WARNING: Insight generation error: {e}")
            return {
                "summary": f"Analysis of {query} based on available research data.",
                "key_insights": ["Data gathered from multiple sources", "Analysis in progress"],
                "recommendations": ["Further research recommended"]
            }

    def _get_sample_data(self, query: str) -> Dict[str, Any]:
        """Fallback sample data if extraction fails"""
        return {
            "trend_data": [
                {"year": "2020", "value": 25},
                {"year": "2021", "value": 42},
                {"year": "2022", "value": 68},
                {"year": "2023", "value": 95},
                {"year": "2024", "value": 127}
            ],
            "comparison_data": [
                {"category": "Category A", "value": 45},
                {"category": "Category B", "value": 28},
                {"category": "Category C", "value": 18},
                {"category": "Category D", "value": 15}
            ],
            "distribution_data": [
                {"name": "Segment 1", "value": 35, "color": "#3B82F6"},
                {"name": "Segment 2", "value": 28, "color": "#8B5CF6"},
                {"name": "Segment 3", "value": 22, "color": "#10B981"},
                {"name": "Segment 4", "value": 15, "color": "#F59E0B"}
            ],
            "key_statistics": [
                {"label": "Total Value", "value": "$127B", "icon": "dollar"},
                {"label": "Growth Rate", "value": "+43%", "icon": "trending_up"},
                {"label": "Market Size", "value": "2,847", "icon": "users"}
            ]
        }
