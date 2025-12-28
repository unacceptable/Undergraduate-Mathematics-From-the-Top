'''
Generate a graph showing the distance h between secant intersection points.

Uses x = 1 and x = 1.5 to illustrate h = 0.5.
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


def main() -> None:
    '''
    Generate graph showing secant line with distance h labeled.
    '''
    fig = go.Figure()

    x = np.linspace(-3, 3, 400)
    x1, y1 = 1, 1
    x2, y2 = 1.5, 2.25

    # Add main traces
    fig.add_trace(create_parabola_trace(x))
    fig.add_trace(create_tangent_trace(x))
    fig.add_trace(create_secant_trace(x, 1.5))

    # Mark the points
    fig.add_trace(create_point_trace([x1], [y1]))
    fig.add_trace(create_point_trace([x2], [y2], color='red'))

    # Annotate points with f(x) notation
    fig.add_annotation(
        x=x1, y=y1,
        text=f'(x, f(x))<br>({x1}, {y1})',
        showarrow=True, arrowhead=2, ax=-70, ay=30, font={'size': 11}
    )
    fig.add_annotation(
        x=x2, y=y2,
        text=f'(x+h, f(x+h))<br>({x2}, {y2})',
        showarrow=True, arrowhead=2, ax=70, ay=-30, font={'size': 11}
    )

    # Draw horizontal line showing h
    h_y = 0.3
    fig.add_shape(type='line', x0=x1, y0=h_y, x1=x2, y1=h_y,
                  line={'color': 'purple', 'width': 2})
    fig.add_trace(go.Scatter(
        x=[x1, x2], y=[h_y, h_y],
        mode='markers',
        marker={'symbol': ['triangle-right', 'triangle-left'], 'size': 10, 'color': 'purple'},
        showlegend=False
    ))
    fig.add_annotation(
        x=(x1 + x2) / 2, y=h_y - 0.6,
        text='<b>h = 0.5</b>',
        showarrow=False, font={'size': 14, 'color': 'purple'}
    )

    # Draw vertical dashed lines from points to x-axis
    fig.add_shape(type='line', x0=x1, y0=0, x1=x1, y1=y1,
                  line={'color': 'gray', 'width': 1.5, 'dash': 'dot'})
    fig.add_shape(type='line', x0=x2, y0=0, x1=x2, y1=y2,
                  line={'color': 'gray', 'width': 1.5, 'dash': 'dot'})

    # Mark x positions on x-axis
    fig.add_annotation(x=x1, y=-0.5, text='x', showarrow=False, font={'size': 12})
    fig.add_annotation(x=x2, y=-0.5, text='x + h', showarrow=False, font={'size': 12})

    fig.update_layout(**get_standard_layout(
        title='Distance h Between Secant Points',
        x_range=[-1, 3],
        y_range=[-2, 10],
        width=900,
        height=700,
        legend_position=(0.02, 0.98)
    ))

    save_figure(fig, 'secant_distance_h.png')


if __name__ == "__main__":
    main()
