"""
Chart Generator - Creates beautiful, professional charts using Plotly
"""
import plotly.graph_objects as go
import plotly.express as px
from typing import Dict, List, Any
import json


class ChartGenerator:
    """Generates professional charts from structured data"""

    def __init__(self):
        # Professional color palette
        self.colors = {
            "primary": "#3B82F6",  # Blue
            "secondary": "#8B5CF6",  # Purple
            "success": "#10B981",  # Green
            "warning": "#F59E0B",  # Orange
            "danger": "#EF4444",  # Red
            "info": "#06B6D4",  # Cyan
        }

        self.color_scale = [
            "#3B82F6", "#8B5CF6", "#10B981",
            "#F59E0B", "#EF4444", "#06B6D4",
            "#EC4899", "#14B8A6", "#F97316"
        ]

    def generate_chart(self, chart_type: str, data: List[Dict], title: str) -> str:
        """
        Generate a chart and return as JSON (Plotly JSON format)

        Args:
            chart_type: Type of chart (line, bar, pie, scatter, heatmap)
            data: Data for the chart
            title: Chart title

        Returns:
            JSON string of Plotly figure
        """

        if chart_type == "line" or chart_type == "line_chart":
            fig = self._create_line_chart(data, title)
        elif chart_type == "bar" or chart_type == "bar_chart":
            fig = self._create_bar_chart(data, title)
        elif chart_type == "pie" or chart_type == "pie_chart":
            fig = self._create_pie_chart(data, title)
        elif chart_type == "scatter" or chart_type == "scatter_plot":
            fig = self._create_scatter_plot(data, title)
        elif chart_type == "heatmap":
            fig = self._create_heatmap(data, title)
        else:
            # Default to bar chart
            fig = self._create_bar_chart(data, title)

        # Convert to JSON
        return fig.to_json()

    def _create_line_chart(self, data: List[Dict], title: str) -> go.Figure:
        """Create a beautiful line chart"""

        # Extract x and y values
        x_values = [item.get("year", item.get("date", item.get("x", i)))
                    for i, item in enumerate(data)]
        y_values = [item.get("value", item.get("y", 0)) for item in data]

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=x_values,
            y=y_values,
            mode='lines+markers',
            name='Trend',
            line=dict(color=self.colors["primary"], width=3),
            marker=dict(size=10, color=self.colors["primary"]),
            hovertemplate='<b>%{x}</b><br>Value: %{y}<extra></extra>'
        ))

        fig.update_layout(
            title=dict(text=title, font=dict(size=20, color='#1F2937')),
            xaxis=dict(
                title="",
                showgrid=True,
                gridcolor='#E5E7EB',
                linecolor='#9CA3AF'
            ),
            yaxis=dict(
                title="Value",
                showgrid=True,
                gridcolor='#E5E7EB',
                linecolor='#9CA3AF'
            ),
            plot_bgcolor='white',
            paper_bgcolor='white',
            hovermode='x unified',
            font=dict(family="Inter, sans-serif", size=12, color='#374151')
        )

        return fig

    def _create_bar_chart(self, data: List[Dict], title: str) -> go.Figure:
        """Create a beautiful bar chart"""

        # Extract categories and values
        categories = [item.get("category", item.get("country", item.get("name", f"Item {i+1}")))
                      for i, item in enumerate(data)]
        values = [item.get("value", item.get("funding", 0)) for item in data]

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=categories,
            y=values,
            marker=dict(
                color=values,
                colorscale=[[0, self.colors["primary"]], [1, self.colors["secondary"]]],
                line=dict(width=0)
            ),
            hovertemplate='<b>%{x}</b><br>Value: %{y}<extra></extra>'
        ))

        fig.update_layout(
            title=dict(text=title, font=dict(size=20, color='#1F2937')),
            xaxis=dict(
                title="",
                showgrid=False,
                linecolor='#9CA3AF'
            ),
            yaxis=dict(
                title="Value",
                showgrid=True,
                gridcolor='#E5E7EB',
                linecolor='#9CA3AF'
            ),
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(family="Inter, sans-serif", size=12, color='#374151'),
            showlegend=False
        )

        return fig

    def _create_pie_chart(self, data: List[Dict], title: str) -> go.Figure:
        """Create a beautiful pie chart"""

        # Extract labels and values
        labels = [item.get("name", item.get("label", f"Segment {i+1}"))
                  for i, item in enumerate(data)]
        values = [item.get("value", 0) for item in data]

        # Use custom colors if provided, otherwise use color scale
        colors = [item.get("color", self.color_scale[i % len(self.color_scale)])
                  for i, item in enumerate(data)]

        fig = go.Figure()

        fig.add_trace(go.Pie(
            labels=labels,
            values=values,
            marker=dict(colors=colors, line=dict(color='white', width=2)),
            hovertemplate='<b>%{label}</b><br>Value: %{value}<br>Percentage: %{percent}<extra></extra>',
            textposition='auto',
            textinfo='label+percent'
        ))

        fig.update_layout(
            title=dict(text=title, font=dict(size=20, color='#1F2937')),
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(family="Inter, sans-serif", size=12, color='#374151'),
            showlegend=True,
            legend=dict(
                orientation="v",
                yanchor="middle",
                y=0.5,
                xanchor="left",
                x=1.05
            )
        )

        return fig

    def _create_scatter_plot(self, data: List[Dict], title: str) -> go.Figure:
        """Create a beautiful scatter plot"""

        x_values = [item.get("x", i) for i, item in enumerate(data)]
        y_values = [item.get("y", item.get("value", 0)) for item in data]

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=x_values,
            y=y_values,
            mode='markers',
            marker=dict(
                size=12,
                color=self.colors["primary"],
                opacity=0.7,
                line=dict(width=2, color='white')
            ),
            hovertemplate='<b>X: %{x}</b><br>Y: %{y}<extra></extra>'
        ))

        fig.update_layout(
            title=dict(text=title, font=dict(size=20, color='#1F2937')),
            xaxis=dict(
                title="X Axis",
                showgrid=True,
                gridcolor='#E5E7EB',
                linecolor='#9CA3AF'
            ),
            yaxis=dict(
                title="Y Axis",
                showgrid=True,
                gridcolor='#E5E7EB',
                linecolor='#9CA3AF'
            ),
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(family="Inter, sans-serif", size=12, color='#374151')
        )

        return fig

    def _create_heatmap(self, data: List[Dict], title: str) -> go.Figure:
        """Create a beautiful heatmap"""

        # Assuming data is in format [{x, y, value}, ...]
        # Group by x and y to create matrix
        x_values = sorted(set(item.get("x", 0) for item in data))
        y_values = sorted(set(item.get("y", 0) for item in data))

        # Create matrix
        matrix = [[0] * len(x_values) for _ in range(len(y_values))]

        for item in data:
            x_idx = x_values.index(item.get("x", 0))
            y_idx = y_values.index(item.get("y", 0))
            matrix[y_idx][x_idx] = item.get("value", 0)

        fig = go.Figure()

        fig.add_trace(go.Heatmap(
            z=matrix,
            x=x_values,
            y=y_values,
            colorscale='Blues',
            hovertemplate='X: %{x}<br>Y: %{y}<br>Value: %{z}<extra></extra>'
        ))

        fig.update_layout(
            title=dict(text=title, font=dict(size=20, color='#1F2937')),
            xaxis=dict(title="X Axis"),
            yaxis=dict(title="Y Axis"),
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(family="Inter, sans-serif", size=12, color='#374151')
        )

        return fig
