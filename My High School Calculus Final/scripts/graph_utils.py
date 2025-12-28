'''
Shared utilities for Plotly graph generation.

Provides common configurations, styling, and helper functions
used across all graph generation scripts.
'''

import os
from typing import Any

import numpy as np
import plotly.graph_objects as go


def get_images_dir() -> str:
    '''
    Get the path to the images directory relative to the scripts folder.

    Returns:
        Absolute path to the images directory.
    '''
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, '..', 'images')


def get_axis_config(
    title: str,
    axis_range: list[float],
    zeroline: bool = True
) -> dict[str, Any]:
    '''
    Get standard axis configuration for Plotly graphs.

    Args:
        title: Axis title (e.g., 'x' or 'y').
        axis_range: List of [min, max] values for the axis range.
        zeroline: Whether to show the zero line.

    Returns:
        Dictionary of axis configuration options.
    '''
    return {
        'title': title,
        'range': axis_range,
        'zeroline': zeroline,
        'zerolinewidth': 1,
        'zerolinecolor': 'black',
        'showgrid': True,
        'gridwidth': 1,
        'gridcolor': 'rgba(128, 128, 128, 0.3)'
    }


def get_standard_layout(  # pylint: disable=too-many-arguments,too-many-positional-arguments
    title: str,
    x_range: list[float],
    y_range: list[float],
    width: int = 800,
    height: int = 600,
    legend_position: tuple[float, float] = (0.85, 0.95)
) -> dict[str, Any]:
    '''
    Get standard layout configuration for Plotly graphs.

    Args:
        title: Graph title.
        x_range: List of [min, max] for x-axis.
        y_range: List of [min, max] for y-axis.
        width: Figure width in pixels.
        height: Figure height in pixels.
        legend_position: Tuple of (x, y) for legend placement.

    Returns:
        Dictionary of layout configuration options.
    '''
    return {
        'title': {'text': title, 'font': {'size': 16}},
        'xaxis': get_axis_config('x', x_range),
        'yaxis': get_axis_config('y', y_range),
        'showlegend': True,
        'legend': {'x': legend_position[0], 'y': legend_position[1]},
        'plot_bgcolor': 'white',
        'width': width,
        'height': height
    }


def save_figure(fig: go.Figure, filename: str) -> None:
    '''
    Save a Plotly figure to the images directory.

    Args:
        fig: The Plotly figure to save.
        filename: Name of the output file (e.g., 'graph.png').
    '''
    output_path = os.path.join(get_images_dir(), filename)
    fig.write_image(output_path, scale=2)
    print(f"Graph saved to '{output_path}'")


def create_parabola_trace(
    x: np.ndarray,
    name: str = r'$f(x) = x^2$',
    color: str = 'blue'
) -> go.Scatter:
    '''
    Create a trace for f(x) = x^2.

    Args:
        x: Array of x values.
        name: Legend name for the trace.
        color: Line color.

    Returns:
        Plotly Scatter trace object.
    '''
    return go.Scatter(
        x=x,
        y=x**2,
        mode='lines',
        name=name,
        line={'color': color, 'width': 2}
    )


def create_tangent_trace(
    x: np.ndarray,
    name: str = 'Tangent at x = 1',
    color: str = 'green',
    dash: str | None = None
) -> go.Scatter:
    '''
    Create a trace for the tangent line to x^2 at x = 1.

    The tangent line is y = 2x - 1.

    Args:
        x: Array of x values.
        name: Legend name for the trace.
        color: Line color.
        dash: Dash style (None, 'dash', 'dot', etc.).

    Returns:
        Plotly Scatter trace object.
    '''
    line_config: dict[str, Any] = {'color': color, 'width': 2}
    if dash:
        line_config['dash'] = dash

    return go.Scatter(
        x=x,
        y=2 * x - 1,
        mode='lines',
        name=name,
        line=line_config
    )


def create_secant_trace(
    x: np.ndarray,
    x_point: float,
    color: str = 'red',
    dash: str = 'dash'
) -> go.Scatter:
    '''
    Create a trace for a secant line from (1, 1) to (x_point, x_point^2).

    Args:
        x: Array of x values.
        x_point: The x-coordinate of the second point on the parabola.
        color: Line color.
        dash: Dash style.

    Returns:
        Plotly Scatter trace object.
    '''
    slope = (x_point**2 - 1) / (x_point - 1)
    secant_y = slope * (x - 1) + 1

    return go.Scatter(
        x=x,
        y=secant_y,
        mode='lines',
        name=f'Secant (slope = {slope:.2f})',
        line={'color': color, 'width': 2, 'dash': dash}
    )


def create_point_trace(  # pylint: disable=too-many-arguments,too-many-positional-arguments
    x_vals: list[float],
    y_vals: list[float],
    color: str = 'black',
    size: int = 10,
    name: str | None = None,
    show_legend: bool = False
) -> go.Scatter:
    '''
    Create a trace for marking points on a graph.

    Args:
        x_vals: List of x coordinates.
        y_vals: List of y coordinates.
        color: Marker color.
        size: Marker size.
        name: Legend name (optional).
        show_legend: Whether to show in legend.

    Returns:
        Plotly Scatter trace object.
    '''
    return go.Scatter(
        x=x_vals,
        y=y_vals,
        mode='markers',
        name=name,
        marker={'color': color, 'size': size},
        showlegend=show_legend
    )
