'''
Generate a graph of f(x) = x^2 with tangent line at x = 1.
'''

import os

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    '''
    Generate and save the x^2 graph with tangent line at x = 1.
    '''
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(script_dir, '..', 'images')

    # Create figure and axis
    _, ax = plt.subplots(figsize=(8, 6))

    # Generate x values from -3 to 3
    x = np.linspace(-3, 3, 400)

    # Calculate y values for f(x) = x^2
    y = x**2

    # Plot the parabola
    ax.plot(x, y, 'b-', linewidth=2, label=r'$f(x) = x^2$')

    # Tangent line at x = 1
    # f(1) = 1, f'(x) = 2x, f'(1) = 2
    # Tangent line: y - 1 = 2(x - 1) => y = 2x - 1
    tangent_y = 2 * x - 1
    ax.plot(x, tangent_y, 'r--', linewidth=2, label=r'Tangent at $x = 1$')

    # Mark the point of tangency
    ax.plot(1, 1, 'ko', markersize=8, label=r'Point $(1, 1)$')

    # Set axis limits
    ax.set_xlim(-3, 3)
    ax.set_ylim(-10, 10)

    # Add grid
    ax.grid(True, linestyle='--', alpha=0.7)

    # Add axis lines through origin
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)

    # Labels and title
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title(r'Graph of $f(x) = x^2$ with Tangent Line at $x = 1$', fontsize=14)
    ax.legend(loc='upper right')

    # Save the figure
    output_path = os.path.join(images_dir, 'x_squared_tangent_graph.png')
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()

    print(f"Graph saved to '{output_path}'")


if __name__ == "__main__":
    main()
