'''
Generate a graph of f(x) = x^2 for the Calculus Final document.
'''

import numpy as np
import plotly.graph_objects as go

from graph_utils import (
    create_parabola_trace,
    get_standard_layout,
    save_figure
)


def main() -> None:
    '''
    Generate and save the x^2 graph image.
    '''
    fig = go.Figure()

    x = np.linspace(-3, 3, 400)
    fig.add_trace(create_parabola_trace(x))

    fig.update_layout(**get_standard_layout(
        title='Graph of f(x) = x²',
        x_range=[-3, 3],
        y_range=[-10, 10]
    ))

    save_figure(fig, 'x_squared_graph.png')


if __name__ == "__main__":
    main()
