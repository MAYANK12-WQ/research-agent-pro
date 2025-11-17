"""
Infographic Generator - Creates beautiful infographic data structures
"""
from typing import Dict, List, Any


class InfographicGenerator:
    """Generates infographic data structures"""

    def generate_infographic(
        self,
        infographic_type: str,
        data: Dict[str, Any],
        title: str
    ) -> Dict[str, Any]:
        """
        Generate infographic data structure

        Args:
            infographic_type: Type of infographic (statistics, timeline, comparison, geographic)
            data: Data for the infographic
            title: Infographic title

        Returns:
            Dict with infographic configuration
        """

        if infographic_type == "statistics" or infographic_type == "stats":
            return self._create_statistics_infographic(data, title)
        elif infographic_type == "timeline":
            return self._create_timeline_infographic(data, title)
        elif infographic_type == "comparison":
            return self._create_comparison_infographic(data, title)
        elif infographic_type == "geographic":
            return self._create_geographic_infographic(data, title)
        else:
            # Default to statistics
            return self._create_statistics_infographic(data, title)

    def _create_statistics_infographic(self, data: Dict, title: str) -> Dict:
        """Create a statistics card infographic"""

        # Extract key statistics from data
        key_stats = data.get("key_statistics", [
            {"label": "Key Metric 1", "value": "100", "icon": "trending_up"},
            {"label": "Key Metric 2", "value": "50%", "icon": "percent"},
            {"label": "Key Metric 3", "value": "1,000", "icon": "users"}
        ])

        return {
            "type": "statistics",
            "title": title,
            "layout": "grid",
            "stats": key_stats,
            "style": {
                "background": "gradient",
                "gradient_from": "#3B82F6",
                "gradient_to": "#8B5CF6",
                "text_color": "white",
                "card_style": "glassmorphism"
            }
        }

    def _create_timeline_infographic(self, data: Dict, title: str) -> Dict:
        """Create a timeline infographic"""

        # Extract timeline events
        timeline_data = data.get("trend_data", [])

        events = [
            {
                "date": item.get("year", item.get("date", f"Event {i+1}")),
                "title": f"Milestone: {item.get('value', 'N/A')}",
                "description": f"Value reached: {item.get('value', 0)}"
            }
            for i, item in enumerate(timeline_data)
        ]

        return {
            "type": "timeline",
            "title": title,
            "layout": "vertical",
            "events": events,
            "style": {
                "line_color": "#3B82F6",
                "marker_color": "#8B5CF6",
                "text_color": "#1F2937"
            }
        }

    def _create_comparison_infographic(self, data: Dict, title: str) -> Dict:
        """Create a comparison infographic"""

        # Extract comparison data
        comparison_data = data.get("comparison_data", [])

        items = [
            {
                "name": item.get("category", item.get("name", f"Item {i+1}")),
                "value": item.get("value", 0),
                "percentage": round((item.get("value", 0) / sum(d.get("value", 1) for d in comparison_data)) * 100, 1)
            }
            for i, item in enumerate(comparison_data)
        ]

        return {
            "type": "comparison",
            "title": title,
            "layout": "side_by_side",
            "items": items,
            "style": {
                "primary_color": "#3B82F6",
                "secondary_color": "#8B5CF6",
                "text_color": "#1F2937"
            }
        }

    def _create_geographic_infographic(self, data: Dict, title: str) -> Dict:
        """Create a geographic map infographic"""

        # Extract geographic data
        geo_data = data.get("comparison_data", [])

        regions = [
            {
                "name": item.get("country", item.get("region", f"Region {i+1}")),
                "value": item.get("value", 0)
            }
            for i, item in enumerate(geo_data)
        ]

        return {
            "type": "geographic",
            "title": title,
            "layout": "map",
            "regions": regions,
            "style": {
                "map_type": "world",
                "color_scale": ["#E0F2FE", "#3B82F6"],
                "text_color": "#1F2937"
            }
        }
