'''
Generate a graph of f(x) = x^2 with tangent line at x = 1.
'''

import numpy as np
import plotly.graph_objects as go

from graph_utils import (
    create_parabola_trace,
    create_point_trace,
    create_tangent_trace,
    get_standard_layout,
    save_figure
)


def main() -> None:
    '''
    Generate and save the x^2 graph with tangent line at x = 1.
    '''
    fig = go.Figure()

    x = np.linspace(-3, 3, 400)

    fig.add_trace(create_parabola_trace(x))
    fig.add_trace(create_tangent_trace(x, color='red', dash='dash'))
    fig.add_trace(create_point_trace([1], [1], name='Point (1, 1)', show_legend=True))

    fig.update_layout(**get_standard_layout(
        title='Graph of f(x) = x² with Tangent Line at x = 1',
        x_range=[-3, 3],
        y_range=[-10, 10],
        legend_position=(0.75, 0.95)
    ))

    save_figure(fig, 'x_squared_tangent_graph.png')


if __name__ == "__main__":
    main()
