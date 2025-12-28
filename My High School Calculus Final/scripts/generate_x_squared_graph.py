'''
Generate a graph of f(x) = x^2 for the Calculus Final document.
'''

import os

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    '''
    Generate and save the x^2 graph image.
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

    # Plot the function
    ax.plot(x, y, 'b-', linewidth=2, label=r'$f(x) = x^2$')

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
    ax.set_title(r'Graph of $f(x) = x^2$', fontsize=14)
    ax.legend(loc='upper right')

    # Save the figure
    output_path = os.path.join(images_dir, 'x_squared_graph.png')
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()

    print(f"Graph saved to '{output_path}'")


if __name__ == "__main__":
    main()
