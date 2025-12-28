'''
Generate a graph showing the function sqrt(x) and its revolution around the x-axis.

Creates a visualization for the solid of revolution concept.
'''

import os

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def main() -> None:
    '''
    Generate graph showing sqrt(x) revolved around the x-axis.
    '''
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(script_dir, '..', 'images')

    # Create figure with two subplots - 2D and 3D views
    fig = make_subplots(
        rows=1, cols=2,
        specs=[[{'type': 'xy'}, {'type': 'scene'}]],
        subplot_titles=(
            'Cross-section: y = √x revolved around x-axis',
            'Solid of Revolution: V = 128π'
        ),
        horizontal_spacing=0.1
    )

    # Generate x values from 0 to 16
    x = np.linspace(0, 16, 400)
    y = np.sqrt(x)

    # Left subplot: 2D view showing the function and radius
    # Plot the function (upper curve)
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode='lines',
        name=r'$f(x) = \sqrt{x}$',
        line={'color': 'blue', 'width': 2}
    ), row=1, col=1)

    # Mirror the function below x-axis
    fig.add_trace(go.Scatter(
        x=x,
        y=-y,
        mode='lines',
        name='Mirror',
        line={'color': 'blue', 'width': 2},
        showlegend=False
    ), row=1, col=1)

    # Fill the area to show the cross-section
    fig.add_trace(go.Scatter(
        x=np.concatenate([x, x[::-1]]),
        y=np.concatenate([y, -y[::-1]]),
        fill='toself',
        fillcolor='rgba(0, 0, 255, 0.2)',
        line={'color': 'rgba(0, 0, 255, 0)'},
        name='Cross-section',
        showlegend=False
    ), row=1, col=1)

    # Show a sample radius at x = 9
    sample_x = 9
    sample_y = np.sqrt(sample_x)
    fig.add_trace(go.Scatter(
        x=[sample_x, sample_x],
        y=[0, sample_y],
        mode='lines',
        name='Radius',
        line={'color': 'red', 'width': 2}
    ), row=1, col=1)
    fig.add_trace(go.Scatter(
        x=[sample_x, sample_x],
        y=[0, -sample_y],
        mode='lines',
        line={'color': 'red', 'width': 2, 'dash': 'dash'},
        showlegend=False
    ), row=1, col=1)

    # Mark the points
    fig.add_trace(go.Scatter(
        x=[sample_x, sample_x],
        y=[sample_y, -sample_y],
        mode='markers',
        marker={'color': 'red', 'size': 8},
        showlegend=False
    ), row=1, col=1)

    # Add radius annotation
    fig.add_annotation(
        x=sample_x + 1,
        y=sample_y / 2,
        text='r = f(x) = √x',
        showarrow=False,
        font={'size': 11, 'color': 'red'},
        xref='x1',
        yref='y1'
    )

    # Right subplot: 3D view of the solid of revolution
    # Create the surface of revolution
    x_3d = np.linspace(0.01, 16, 50)
    theta = np.linspace(0, 2 * np.pi, 50)
    x_mesh, theta_mesh = np.meshgrid(x_3d, theta)

    # r = sqrt(x) is the radius at each x
    r_mesh = np.sqrt(x_mesh)

    # Convert to Cartesian coordinates
    y_mesh = r_mesh * np.cos(theta_mesh)
    z_mesh = r_mesh * np.sin(theta_mesh)

    # Plot the surface
    fig.add_trace(go.Surface(
        x=x_mesh,
        y=y_mesh,
        z=z_mesh,
        colorscale='Blues',
        opacity=0.8,
        showscale=False,
        name='Solid'
    ), row=1, col=2)

    # Update 2D subplot layout
    fig.update_xaxes(
        title_text='x',
        range=[-1, 18],
        zeroline=True,
        zerolinewidth=1,
        zerolinecolor='black',
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(128, 128, 128, 0.3)',
        row=1, col=1
    )
    fig.update_yaxes(
        title_text='y',
        range=[-5, 5],
        zeroline=True,
        zerolinewidth=1,
        zerolinecolor='black',
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(128, 128, 128, 0.3)',
        scaleanchor='x1',
        scaleratio=1,
        row=1, col=1
    )

    # Update 3D scene layout
    fig.update_scenes(
        xaxis_title='x',
        yaxis_title='y',
        zaxis_title='z',
        aspectmode='data'
    )

    # Update overall layout
    fig.update_layout(
        showlegend=True,
        legend={'x': 0.02, 'y': 0.98},
        plot_bgcolor='white',
        width=1400,
        height=600
    )

    # Save the figure
    output_path = os.path.join(images_dir, 'revolution_sqrt_x.png')
    fig.write_image(output_path, scale=2)

    print(f"Graph saved to '{output_path}'")


if __name__ == "__main__":
    main()
