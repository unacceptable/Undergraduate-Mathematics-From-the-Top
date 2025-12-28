'''
Generate graphs showing Riemann sum approximations for sqrt(x).

Creates three graphs with n=5, n=10, and n=20 rectangles.
'''

import os

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np


def generate_riemann_sum_graph(
    n_rectangles: int,
    output_filename: str,
    images_dir: str
) -> None:
    '''
    Generate a graph showing Riemann sum rectangles under sqrt(x).

    Args:
        n_rectangles: Number of rectangles to use.
        output_filename: Name of the output image file.
        images_dir: Directory to save the image.
    '''
    # Create figure and axis
    _, ax = plt.subplots(figsize=(10, 6))

    # Generate x values for the curve (only positive values for sqrt)
    x_curve = np.linspace(0, 20, 400)
    y_curve = np.sqrt(x_curve)

    # Plot the curve
    ax.plot(x_curve, y_curve, 'b-', linewidth=2, label=r'$f(x) = \sqrt{x}$')

    # Define the interval for Riemann sum [a, b]
    a, b = 0, 20
    delta_x = (b - a) / n_rectangles

    # Draw rectangles using midpoints
    for i in range(n_rectangles):
        x_left = a + i * delta_x
        x_mid = x_left + delta_x / 2
        height = np.sqrt(x_mid)

        # Draw rectangle
        rect = patches.Rectangle(
            (x_left, 0),
            delta_x,
            height,
            linewidth=1.5,
            edgecolor='red',
            facecolor='lightcoral',
            alpha=0.6
        )
        ax.add_patch(rect)

        # Label the rectangles
        # Adjust font size based on number of rectangles
        if n_rectangles <= 10:
            fontsize = 10 if n_rectangles == 5 else 8
            ax.text(
                x_mid,
                height / 2,
                f'$h_{{{i + 1}}}$',
                fontsize=fontsize,
                ha='center',
                va='center'
            )
            ax.text(
                x_mid,
                -0.5,
                f'$x_{{{i + 1}}}$',
                fontsize=fontsize,
                ha='center',
                va='top'
            )
        elif n_rectangles == 20:
            ax.text(
                x_mid,
                height / 2,
                f'$h_{{{i + 1}}}$',
                fontsize=6,
                ha='center',
                va='center'
            )
            ax.text(
                x_mid,
                -0.5,
                f'$x_{{{i + 1}}}$',
                fontsize=6,
                ha='center',
                va='top'
            )

    # Set axis limits
    ax.set_xlim(-2, 20)
    ax.set_ylim(-5, 5)

    # Add grid
    ax.grid(True, linestyle='--', alpha=0.7)

    # Add axis lines through origin
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)

    # Labels and title
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title(
        rf'Area Approximation: $n = {n_rectangles}$ rectangles',
        fontsize=14
    )
    ax.legend(loc='upper right')

    # Save the figure
    output_path = os.path.join(images_dir, output_filename)
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()

    print(f"Graph saved to '{output_path}'")


def main() -> None:
    '''
    Generate all three Riemann sum approximation graphs.
    '''
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(script_dir, '..', 'images')

    # Generate graphs for each n value
    rectangles_configs = [
        (5, 'riemann_sum_n5.png'),
        (10, 'riemann_sum_n10.png'),
        (20, 'riemann_sum_n20.png'),
    ]

    for n_rect, filename in rectangles_configs:
        generate_riemann_sum_graph(n_rect, filename, images_dir)


if __name__ == "__main__":
    main()
