"""Plotting functions"""

# Authors: Lukas Stranger

import numpy as np
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt


def create_yellow_blue_cdict():
    """
        Builds and registers a dictionary of color values that represent the
        yellow-blue spectrum of the Haidinger brush
    """
    cdict = {'red':   ((0.0, 1.0, 1.0),
                       (0.5, 0.0, 0.0),
                       (1.0, 0.0, 0.0)),

             'green': ((0.0, 1.0, 1.0),
                       (0.5, 0.0, 0.0),
                       (1.0, 0.0, 0.0)),

             'blue':  ((0.0, 0.0, 0.0),
                       (0.5, 0.0, 0.0),
                       (1.0, 1.0, 1.0)),
            }

    yellow_blue = LinearSegmentedColormap('YellowBlue', cdict)
    plt.register_cmap(cmap=yellow_blue)


###############################################################################
# Base class for a canvas holding a matplotlib figure

class PolarPlotCanvas(FigureCanvas):
    """ Base class that initializes the most basic parameters for a polar plot
    """
    def __init__(self, parent=None, width=100, height=50, dpi=100, angle_resolution=360, magnitude_resolution=30):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111, polar=True)
        self.axes.hold(False)

        self.magnitude_grid = np.linspace(0, 1, magnitude_resolution)
        self.angular_grid = np.linspace(0, 2 * np.pi, angle_resolution)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


###############################################################################
# Class for plotting the Yellow-bluish Haidinger brush

class ColorPlotCanvas(PolarPlotCanvas):

    def __init__(self, *args, **kwargs):
        PolarPlotCanvas.__init__(self, *args, **kwargs)
        self.cb = None

    def update_figure(self, eye_view):
        """
            Plots the characteristic Yellow-bluish Haidinger brush based on intensity values
            ----------
            eye_view : ndarray
                The intensity values per angle.
        """
        self.axes.set_yticklabels([])

        intensity_dist = np.ones((len(self.magnitude_grid), len(self.angular_grid)))
        for i, alpha in enumerate(self.angular_grid):
            intensity_dist[:, i] = eye_view[i]

        cmap = plt.get_cmap('YellowBlue')
        ctf = self.axes.contourf(self.angular_grid, self.magnitude_grid, intensity_dist,
                                 levels=np.linspace(0, 1, 25), cmap=cmap)

        if self.cb is None:
            self.cb = self.fig.colorbar(ctf)
            self.cb.set_ticks(np.linspace(0, 1, 11))
        self.cb.ax.set_autoscale_on(True)
        self.draw()

###############################################################################
# Class for plotting the Intensity distribution


class IntensityDistributionCanvas(PolarPlotCanvas):

    def __init__(self, *args, **kwargs):
        PolarPlotCanvas.__init__(self, *args, **kwargs)

    def update_figure(self, eye_view):
        """
            Plots a intensity distribution of bluish passed light
            ----------
            eye_view : ndarray
                The intensity values per angle.
        """
        self.axes.set_yticklabels([])

        intensity_dist = np.ones((len(self.magnitude_grid), len(self.angular_grid)))
        for i, alpha in enumerate(self.angular_grid):
            intensity_dist[int((len(self.magnitude_grid)-1) * eye_view[i]), i] = 0

        ctf = self.axes.contourf(self.angular_grid, self.magnitude_grid, intensity_dist,
                                 levels=np.linspace(0, 1, 25))
        ctf.set_cmap('gray')
        self.draw()
