'''
Generate graphs showing Riemann sum approximations for sqrt(x).

Creates three graphs with n=5, n=10, and n=20 rectangles.
'''

import numpy as np
import plotly.graph_objects as go

from graph_utils import get_axis_config, save_figure


def generate_riemann_sum_graph(n_rectangles: int, output_filename: str) -> None:
    '''
    Generate a graph showing Riemann sum rectangles under sqrt(x).

    Args:
        n_rectangles: Number of rectangles to use.
        output_filename: Name of the output image file.
    '''
    fig = go.Figure()

    # Plot the curve
    x_curve = np.linspace(0, 20, 400)
    fig.add_trace(go.Scatter(
        x=x_curve,
        y=np.sqrt(x_curve),
        mode='lines',
        name=r'$f(x) = \sqrt{x}$',
        line={'color': 'blue', 'width': 2}
    ))

    # Draw rectangles using midpoints
    a, b = 0, 20
    delta_x = (b - a) / n_rectangles

    for i in range(n_rectangles):
        x_left = a + i * delta_x
        x_mid = x_left + delta_x / 2
        height = np.sqrt(x_mid)

        fig.add_shape(
            type='rect',
            x0=x_left, y0=0, x1=x_left + delta_x, y1=height,
            line={'color': 'red', 'width': 1.5},
            fillcolor='rgba(240, 128, 128, 0.6)'
        )

        # Label rectangles with appropriate font size
        fontsize = 12 if n_rectangles == 5 else (10 if n_rectangles == 10 else 7)
        fig.add_annotation(x=x_mid, y=height / 2, text=f'h<sub>{i + 1}</sub>',
                           showarrow=False, font={'size': fontsize})
        fig.add_annotation(x=x_mid, y=-0.5, text=f'x<sub>{i + 1}</sub>',
                           showarrow=False, font={'size': fontsize})

    fig.update_layout(
        title={'text': f'Area Approximation: n = {n_rectangles} rectangles', 'font': {'size': 16}},
        xaxis=get_axis_config('x', [-2, 22]),
        yaxis=get_axis_config('y', [-2, 6]),
        showlegend=True,
        legend={'x': 0.85, 'y': 0.95},
        plot_bgcolor='white',
        width=900,
        height=600
    )

    save_figure(fig, output_filename)


def main() -> None:
    '''
    Generate all three Riemann sum approximation graphs.
    '''
    configs = [
        (5, 'riemann_sum_n5.png'),
        (10, 'riemann_sum_n10.png'),
        (20, 'riemann_sum_n20.png'),
    ]

    for n_rect, filename in configs:
        generate_riemann_sum_graph(n_rect, filename)


if __name__ == "__main__":
    main()
