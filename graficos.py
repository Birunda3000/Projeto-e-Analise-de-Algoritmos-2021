import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def print_2d(x, x_label, y, y_label, title, save=False, show=False, path=''):
    plt.plot(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(color = 'g', linestyle=':', linewidth=.3)
    if show:
        plt.show()
    if save:
        plt.savefig(path, dpi=300)

def print_3d(xx, x_label, yy, y_label, z, z_label, title, save=False, show=False, path=''):

    fig = plt.figure()

    ax = fig.add_subplot(111,projection='3d')

    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel(z_label)

    #xx, yy = np.meshgrid(range(10), range(10))
    #z = (9 - xx**3 - yy**2) / 2 

    ax.plot_surface(xx, yy, z, alpha=0.5)
    if show:
        plt.show()
    if save:
        plt.savefig(path, dpi=300)