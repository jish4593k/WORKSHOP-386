import os
import torch
import matplotlib.pyplot as plt
import numpy as np

def generate_random_data(num_points):
    """
    Generate random data for plotting.

    Args:
        num_points (int): Number of data points.

    Returns:
        Tuple[torch.Tensor, torch.Tensor]: X and Y coordinates of the generated data.
    """
    x = torch.linspace(0, 10, num_points)
    y = torch.sin(x) + torch.randn(num_points) * 0.5
    return x, y

def plot_random_data(savefile):
    """
    Generate and plot random data.

    Args:
        savefile (str): Path to save the plot.
    """
    x, y = generate_random_data(100)

    plt.figure(figsize=(8, 6))
    plt.plot(x.numpy(), y.numpy(), label='Random Data')
    plt.title('Random Data Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.savefig(savefile)
    plt.show()

if __name__ == "__main__":
    # Example usage:
    savefile = "random_plot.png"
    plot_random_data(savefile)
