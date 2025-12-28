'''
Generate a graph showing the function sqrt(x) and its revolution around the x-axis.

Creates a visualization for the solid of revolution concept.
'''

import os

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    '''
    Generate graph showing sqrt(x) revolved around the x-axis.
    '''
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(script_dir, '..', 'images')

    # Create figure with two subplots - 2D and 3D views
    fig = plt.figure(figsize=(14, 6))

    # Left subplot: 2D view showing the function and radius
    ax1 = fig.add_subplot(1, 2, 1)

    # Generate x values from 0 to 16
    x = np.linspace(0, 16, 400)
    y = np.sqrt(x)

    # Plot the function
    ax1.plot(x, y, 'b-', linewidth=2, label=r'$f(x) = \sqrt{x}$')

    # Mirror the function below x-axis to show revolution shape
    ax1.plot(x, -y, 'b-', linewidth=2)

    # Fill the area to show the cross-section
    ax1.fill_between(x, -y, y, alpha=0.3, color='blue')

    # Show a sample radius at x = 9
    sample_x = 9
    sample_y = np.sqrt(sample_x)
    ax1.plot([sample_x, sample_x], [0, sample_y], 'r-', linewidth=2)
    ax1.plot([sample_x, sample_x], [0, -sample_y], 'r--', linewidth=2)
    ax1.annotate(
        r'$r = f(x) = \sqrt{x}$',
        (sample_x, sample_y / 2),
        textcoords="offset points",
        xytext=(15, 0),
        fontsize=11,
        color='red'
    )

    # Mark the point
    ax1.plot(sample_x, sample_y, 'ro', markersize=8)
    ax1.plot(sample_x, -sample_y, 'ro', markersize=8)

    # Set axis limits and labels
    ax1.set_xlim(-1, 18)
    ax1.set_ylim(-5, 5)
    ax1.set_xlabel('x', fontsize=12)
    ax1.set_ylabel('y', fontsize=12)
    ax1.set_title(r'Cross-section: $y = \sqrt{x}$ revolved around x-axis', fontsize=12)
    ax1.axhline(y=0, color='k', linewidth=0.5)
    ax1.axvline(x=0, color='k', linewidth=0.5)
    ax1.grid(True, linestyle='--', alpha=0.7)
    ax1.legend(loc='upper left')
    ax1.set_aspect('equal')

    # Right subplot: 3D view of the solid of revolution
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')

    # Create the surface of revolution
    x_3d = np.linspace(0.01, 16, 100)
    theta = np.linspace(0, 2 * np.pi, 100)
    x_mesh, theta_mesh = np.meshgrid(x_3d, theta)

    # r = sqrt(x) is the radius at each x
    r_mesh = np.sqrt(x_mesh)

    # Convert to Cartesian coordinates
    y_mesh = r_mesh * np.cos(theta_mesh)
    z_mesh = r_mesh * np.sin(theta_mesh)

    # Plot the surface
    ax2.plot_surface(
        x_mesh, y_mesh, z_mesh,
        alpha=0.7,
        cmap='Blues',
        edgecolor='none'
    )

    # Set labels
    ax2.set_xlabel('x', fontsize=10)
    ax2.set_ylabel('y', fontsize=10)
    ax2.set_zlabel('z', fontsize=10)
    ax2.set_title(r'Solid of Revolution: $V = 128\pi$', fontsize=12)

    plt.tight_layout()

    # Save the figure
    output_path = os.path.join(images_dir, 'revolution_sqrt_x.png')
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()

    print(f"Graph saved to '{output_path}'")


if __name__ == "__main__":
    main()
