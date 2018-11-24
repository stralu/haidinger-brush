"""Optic functions that simulate the eye characteristics"""

# Authors: Lukas Stranger

import numpy as np


def get_polarizer(azimuth):
    """
        Builds the Mueller-Matrix of a polarizer
        Parameters
        ----------
        azimuth : float
            The azimuth of the polarizer
        Returns
        -------
        out : ndarray
            A (4, 4) ndarray consisting of the Mueller-Matrix
    """
    return 1. / 2 * np.array([[1, np.cos(2 * azimuth), np.sin(2 * azimuth), 0],
                                [np.cos(2 * azimuth), np.cos(2 * azimuth) ** 2,
                                 np.sin(2 * azimuth) * np.cos(2 * azimuth), 0],
                                [np.sin(2 * azimuth), np.sin(2 * azimuth) * np.cos(2 * azimuth),
                                 np.sin(2 * azimuth) ** 2, 0],
                                [0, 0, 0, 0]])


def get_homogenous_linear_retarder(retardance, fast_ax_azimuth):
    """
        Builds the Mueller-Matrix of a homogenous linear retarder
        Parameters
        ----------
        retardance : float
           The retardance as a multiplier of lambda
        fast_ax_azimuth : float
            The azimuth of the fast axis
        Returns
        -------
        out : ndarray
            A (4, 4) ndarray consisting of the Mueller-Matrix
    """
    retardance *= 2 * np.pi
    return np.array([[1, 0, 0, 0],
                     [0, np.cos(2 * fast_ax_azimuth) ** 2 + np.sin(2 * fast_ax_azimuth) ** 2 * np.cos(retardance),
                      np.sin(2 * fast_ax_azimuth) * np.cos(2 * fast_ax_azimuth) * (1 - np.cos(retardance)),
                      -np.sin(2 * fast_ax_azimuth) * np.sin(retardance)],
                     [0, np.sin(2 * fast_ax_azimuth) * np.cos(fast_ax_azimuth * (1 - np.cos(retardance))),
                      np.sin(2 * fast_ax_azimuth) ** 2 + np.cos(2 * fast_ax_azimuth) ** 2 * np.cos(retardance),
                      np.cos(2 * fast_ax_azimuth) * np.sin(retardance)],
                     [0, np.sin(2 * fast_ax_azimuth) * np.sin(retardance),
                      -np.cos(2 * fast_ax_azimuth) * np.sin(retardance),
                      np.cos(retardance)]])


###############################################################################
# Class that modulates the birefringent components of the human eye

class EyeOptics():
    """ Holds the human's eyes birefringent elements
        Parameters
        ----------
        cornea_retardance : float
               The retardance as a multiplier of lambda
        cornea_fast_ax_azimuth : float
                The azimuth of the fast axis
    """
    def __init__(self, cornea_retardance, cornea_fast_ax_azimuth=0):
        self.cornea = get_homogenous_linear_retarder(cornea_retardance, cornea_fast_ax_azimuth)
        self.macula_exists = True

    def update_cornea_parameter(self, cornea_retardance, cornea_fast_ax_azimuth=0):
        """
            Updates the corneas parameters
            ----------
            Parameters
            ----------
            cornea_retardance : float
               The retardance as a multiplier of lambda
            cornea_fast_ax_azimuth : float
                The azimuth of the fast axis
            Returns
            -------
        """
        self.cornea = get_homogenous_linear_retarder(cornea_retardance, cornea_fast_ax_azimuth)

    def get_view(self, light_azimuth, angles):
        """
            Calculates the intensity for all given angles.
            ----------
            light_azimuth : float
               The azimuth of incident light
            angles : ndarray
                A ndarray consisting of angles for which the intensity is calculated
            Returns
            -------
            out : ndarray
                The calculated intensities
        """
        light_azimuth *= 2 * np.pi / 360
        intensity_dist = np.zeros_like(angles)
        for i, alpha in enumerate(angles):
            incident_light = np.array([1., np.cos(2 * light_azimuth), np.sin(2 * light_azimuth), 0]).T
            if self.macula_exists:
                macula = get_polarizer(alpha)
                stokes_vector = macula.dot(self.cornea).dot(incident_light)
            else:
                stokes_vector = self.cornea.dot(incident_light)

            intensity_dist[i] = stokes_vector[0]
        return intensity_dist
