'''
Generate a graph showing the distance h between secant intersection points.

Uses x = 1 and x = 1.5 to illustrate h = 0.5.
'''

import os

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    '''
    Generate graph showing secant line with distance h labeled.
    '''
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(script_dir, '..', 'images')

    # Create figure and axis
    _, ax = plt.subplots(figsize=(10, 7))

    # Generate x values from -3 to 3
    x = np.linspace(-3, 3, 400)

    # Calculate y values for f(x) = x^2
    y = x**2

    # Plot the parabola
    ax.plot(x, y, 'b-', linewidth=2, label=r'$f(x) = x^2$')

    # Actual tangent line at x = 1: y = 2x - 1
    tangent_y = 2 * x - 1
    ax.plot(x, tangent_y, 'g-', linewidth=2, label=r'Tangent at $x = 1$')

    # Secant line from (1, 1) to (1.5, 2.25)
    x1, y1 = 1, 1
    x2, y2 = 1.5, 2.25
    slope = (y2 - y1) / (x2 - x1)
    secant_y = slope * (x - x1) + y1
    ax.plot(
        x, secant_y, 'r--', linewidth=2,
        label=f'Secant (slope = {slope:.2f})'
    )

    # Mark the points
    ax.plot(x1, y1, 'ko', markersize=10, zorder=5)
    ax.plot(x2, y2, 'ro', markersize=10, zorder=5)

    # Annotate points with f(x) notation
    ax.annotate(
        r'$(x, f(x))$' + f'\n({x1}, {y1})',
        (x1, y1),
        textcoords="offset points",
        xytext=(-60, -25),
        fontsize=11,
        ha='center'
    )
    ax.annotate(
        r'$(x+h, f(x+h))$' + f'\n({x2}, {y2})',
        (x2, y2),
        textcoords="offset points",
        xytext=(60, 10),
        fontsize=11,
        ha='center'
    )

    # Draw horizontal line showing h
    h_y = 0.3  # y position for the h annotation
    ax.annotate(
        '',
        xy=(x2, h_y),
        xytext=(x1, h_y),
        arrowprops={'arrowstyle': '<->', 'color': 'purple', 'lw': 2}
    )
    ax.text(
        (x1 + x2) / 2,
        h_y - 0.5,
        r'$h = 0.5$',
        fontsize=14,
        ha='center',
        color='purple',
        fontweight='bold'
    )

    # Draw vertical dashed lines from points to x-axis
    ax.vlines(x1, 0, y1, colors='gray', linestyles=':', linewidth=1.5)
    ax.vlines(x2, 0, y2, colors='gray', linestyles=':', linewidth=1.5)

    # Mark x positions on x-axis
    ax.plot(x1, 0, 'k|', markersize=15)
    ax.plot(x2, 0, 'r|', markersize=15)
    ax.text(x1, -0.8, r'$x$', fontsize=12, ha='center')
    ax.text(x2, -0.8, r'$x + h$', fontsize=12, ha='center')

    # Set axis limits
    ax.set_xlim(-1, 3)
    ax.set_ylim(-2, 10)

    # Add grid
    ax.grid(True, linestyle='--', alpha=0.7)

    # Add axis lines through origin
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)

    # Labels and title
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title(
        r'Distance $h$ Between Secant Points',
        fontsize=14
    )
    ax.legend(loc='upper left')

    # Save the figure
    output_path = os.path.join(images_dir, 'secant_distance_h.png')
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()

    print(f"Graph saved to '{output_path}'")


if __name__ == "__main__":
    main()
