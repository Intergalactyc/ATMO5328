# For problems 2b & 2c

import pathlib

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors


SAVEDIR = pathlib.Path(__file__).parent / "plots"

def get_solution_function(x0, y0, z0, q):
    def solution_function(x, y, z):
        return q/(4*np.pi)/np.sqrt((x-x0)**2+(y-y0)**2+(z-z0)**2)
    return solution_function

def plot_contours(phi):
    # problem 2b
    x = np.linspace(0, 40, 100)
    z = np.linspace(0, 40, 100)
    xx, zz = np.meshgrid(x, z, sparse=True)
    solution = phi(xx, 0, zz)

    fig, ax = plt.subplots()
    contour = ax.contourf(x, z, solution, levels=10)
    ax.set_aspect("equal")
    ax.set_xlabel("X")
    ax.set_ylabel("Z")
    fig.colorbar(contour)

    plt.savefig(SAVEDIR / "contours.png")

def plot_vectors(phi):
    # problem 2c
    fig, ax = plt.subplots()

    x = np.linspace(0, 40, 40)
    z = np.linspace(0, 40, 40)
    xx, zz = np.meshgrid(x, z)
    solution = phi(xx, 0, zz)
    ax.quiver(xx, zz, 0, solution, scale=0.4, width=0.004, minlength=0.1)

    ax.set_aspect("equal")
    ax.set_xlabel("X")
    ax.set_ylabel("Z")

    plt.savefig(SAVEDIR / "arrows.png")

def plot_together(phi):
    # combine the above two into one plot
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.set_xlabel("X")
    ax.set_ylabel("Z")

    x = np.linspace(0, 40, 100)
    z = np.linspace(0, 40, 100)
    xx, zz = np.meshgrid(x, z, sparse=True)
    solution = phi(xx, 0, zz)
    contour = ax.contourf(x, z, solution, levels=10)
    fig.colorbar(contour)

    x = np.linspace(0, 40, 40)
    z = np.linspace(0, 40, 40)
    xx, zz = np.meshgrid(x, z)
    solution = phi(xx, 0, zz)
    ax.quiver(xx, zz, 0, solution, scale=0.4, width=0.004, minlength=0.1)

    plt.savefig(SAVEDIR / "together.png")

def main():
    phi = get_solution_function(20, 0, 20, 0.5)

    plot_contours(phi)
    plot_vectors(phi)
    plot_together(phi)


if __name__ == "__main__":
    main()
