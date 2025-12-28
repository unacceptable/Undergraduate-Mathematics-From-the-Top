'''
Generate graphs showing tangent line approximations using secant lines.

Creates three graphs for x = 3, x = 2, and x = 1.5 approximations.
'''

import numpy as np
import plotly.graph_objects as go

from graph_utils import (
    create_parabola_trace,
    create_point_trace,
    create_secant_trace,
    create_tangent_trace,
    get_standard_layout,
    save_figure
)


def generate_approximation_graph(x_point: float, output_filename: str) -> None:
    '''
    Generate a graph showing the actual tangent and secant line approximation.

    Args:
        x_point: The x-value for the secant line endpoint.
        output_filename: Name of the output image file.
    '''
    fig = go.Figure()

    x = np.linspace(-3, 3, 400)

    fig.add_trace(create_parabola_trace(x))
    fig.add_trace(create_tangent_trace(x))
    fig.add_trace(create_secant_trace(x, x_point))

    # Mark the intersection points
    fig.add_trace(create_point_trace([1], [1]))
    fig.add_annotation(x=1, y=1, text='(1, 1)', showarrow=True, arrowhead=2, ax=30, ay=30)

    fig.add_trace(create_point_trace([x_point], [x_point**2], color='red'))
    fig.add_annotation(
        x=x_point, y=x_point**2,
        text=f'({x_point}, {x_point**2})',
        showarrow=True, arrowhead=2, ax=30, ay=-30
    )

    slope = (x_point**2 - 1) / (x_point - 1)
    fig.update_layout(**get_standard_layout(
        title=f'Approximation using x = {x_point} (slope = {slope:.2f})',
        x_range=[-3, 3],
        y_range=[-10, 10],
        legend_position=(0.02, 0.98)
    ))

    save_figure(fig, output_filename)


def main() -> None:
    '''
    Generate all three approximation graphs.
    '''
    approximations = [
        (3.0, 'approximation_x3.png'),
        (2.0, 'approximation_x2.png'),
        (1.5, 'approximation_x1_5.png'),
    ]

    for x_point, filename in approximations:
        generate_approximation_graph(x_point, filename)


if __name__ == "__main__":
    main()
