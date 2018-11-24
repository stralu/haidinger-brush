"""Main function of the Haidinger brush model"""

# Authors: Lukas Stranger


import sys
from PyQt5.QtWidgets import QApplication, QWidget
import PyQt5.QtCore as QtCore
import design
from plotting import IntensityDistributionCanvas, ColorPlotCanvas, create_yellow_blue_cdict
from eye_optics import EyeOptics


class AppWindow(QWidget):

    @QtCore.pyqtSlot()
    def incident_light_azimuth_changed(self):
        """ Event slot caused by a change of the incident light azimuth.
            Recalculates the light distribution and triggers a figure refresh.
        """
        self.refresh_figures(self.ui.dsb_incident_light.value())

    @QtCore.pyqtSlot()
    def cornea_retardance_changed(self):
        """ Event slot caused by a change of the corneal retardance.
            Recalculates the light distribution and triggers a figure refresh.
        """
        self.Eye.update_cornea_parameter(self.ui.dsb_cornea_retardance.value())
        self.refresh_figures(self.ui.dsb_incident_light.value())

    @QtCore.pyqtSlot()
    def cornea_check_changed(self):
        """ Event slot caused by the de- or selection of the cornea.
            Recalculates the light distribution and triggers a figure refresh.
        """
        if self.ui.cbCornea.isChecked():
            self.ui.dsb_cornea_retardance.setEnabled(True)
            retardance = self.ui.dsb_cornea_retardance.value()
        else:
            self.ui.dsb_cornea_retardance.setEnabled(False)
            retardance = 0

        self.Eye.update_cornea_parameter(retardance)
        self.refresh_figures(self.ui.dsb_incident_light.value())

    @QtCore.pyqtSlot()
    def macula_check_changed(self):
        """ Event slot caused by the de- or selection of the macula.
            Recalculates the light distribution and triggers a figure refresh.
        """
        if self.ui.cbMacula.isChecked():
            self.Eye.macula_exists = True
        else:
            self.Eye.macula_exists = False

        self.refresh_figures(self.ui.dsb_incident_light.value())

    def refresh_figures(self, incident_light_azimuth):
        """ Refreshes the handing the actual intensities over to the figures
            Parameters
            ----------
            incident_light_azimuth : float
                The current azimuth of incoming light.
        """
        current_view = self.Eye.get_view(incident_light_azimuth,
                                         self.fig_haidinger.angular_grid)
        self.fig_haidinger.update_figure(current_view)
        self.fig_intensity.update_figure(current_view)

    def __init__(self):
        """ Initializes the GUI, event slots and the eye model.
        """
        super().__init__()
        self.ui = design.Ui_Form()
        self.ui.setupUi(self)
        self.ui.dsb_cornea_retardance.valueChanged.connect(self.cornea_retardance_changed)
        self.ui.dsb_incident_light.valueChanged.connect(self.incident_light_azimuth_changed)
        self.ui.cbCornea.stateChanged.connect(self.cornea_check_changed)
        self.ui.cbMacula.stateChanged.connect(self.macula_check_changed)

        self.Eye = EyeOptics(self.ui.dsb_cornea_retardance.value())

        self.fig_haidinger = ColorPlotCanvas()
        self.fig_intensity = IntensityDistributionCanvas()

        self.refresh_figures(self.ui.dsb_incident_light.value())

        self.ui.grid.addWidget(self.fig_haidinger, 0, 0)
        self.ui.grid.addWidget(self.fig_intensity, 0, 1)
        self.show()


def main():
    """ Entry point for the Haidinger-Brush simulation.
        Creates a Blue-yellowish color map and calls the main application.
        Parameters
        ----------
        incident_light_azimuth : float
            The current azimuth of incoming light.
    """
    create_yellow_blue_cdict()
    app = QApplication(sys.argv)
    win = AppWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
