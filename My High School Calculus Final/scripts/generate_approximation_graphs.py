'''
Generate graphs showing tangent line approximations using secant lines.

Creates three graphs for x = 3, x = 2, and x = 1.5 approximations.
'''

import os

import matplotlib.pyplot as plt
import numpy as np


def generate_approximation_graph(
    x_point: float,
    output_filename: str,
    images_dir: str
) -> None:
    '''
    Generate a graph showing the actual tangent and secant line approximation.

    Args:
        x_point: The x-value for the secant line endpoint.
        output_filename: Name of the output image file.
        images_dir: Directory to save the image.
    '''
    # Create figure and axis
    _, ax = plt.subplots(figsize=(8, 6))

    # Generate x values from -3 to 3
    x = np.linspace(-3, 3, 400)

    # Calculate y values for f(x) = x^2
    y = x**2

    # Plot the parabola
    ax.plot(x, y, 'b-', linewidth=2, label=r'$f(x) = x^2$')

    # Actual tangent line at x = 1: y = 2x - 1
    tangent_y = 2 * x - 1
    ax.plot(x, tangent_y, 'g-', linewidth=2, label=r'Tangent at $x = 1$')

    # Calculate secant line (approximation)
    # Points: (1, 1) and (x_point, x_point^2)
    y1 = 1
    y2 = x_point**2
    slope = (y2 - y1) / (x_point - 1)

    # Secant line: y - y1 = slope * (x - x1) => y = slope * (x - 1) + 1
    secant_y = slope * (x - 1) + 1
    ax.plot(
        x, secant_y, 'r--', linewidth=2,
        label=f'Secant (slope = {slope:.2f})'
    )

    # Mark the points of intersection
    ax.plot(1, 1, 'ko', markersize=10, zorder=5)
    ax.annotate(
        '(1, 1)', (1, 1), textcoords="offset points",
        xytext=(10, -15), fontsize=10
    )

    ax.plot(x_point, x_point**2, 'ro', markersize=10, zorder=5)
    ax.annotate(
        f'({x_point}, {x_point**2})', (x_point, x_point**2),
        textcoords="offset points", xytext=(10, 10), fontsize=10
    )

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
    ax.set_title(
        f'Approximation using $x = {x_point}$ (slope = {slope:.2f})',
        fontsize=14
    )
    ax.legend(loc='upper left')

    # Save the figure
    output_path = os.path.join(images_dir, output_filename)
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()

    print(f"Graph saved to '{output_path}'")


def main() -> None:
    '''
    Generate all three approximation graphs.
    '''
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(script_dir, '..', 'images')

    # Generate graphs for each approximation
    approximations = [
        (3.0, 'approximation_x3.png'),
        (2.0, 'approximation_x2.png'),
        (1.5, 'approximation_x1_5.png'),
    ]

    for x_point, filename in approximations:
        generate_approximation_graph(x_point, filename, images_dir)


if __name__ == "__main__":
    main()
