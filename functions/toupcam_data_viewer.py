import os
import sys
sys.path.append('..')
sys.path.append('../instruments/toupcam')
import time
# from ui.toupcam_data_viewer_UI import Ui_toupcam_data_viewer
from ui.beam_location_viewer_UI import Ui_beam_location
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.QtGui import QPixmap
from instruments.toupcam.camera import ToupCamCamera

class ToupAccquire(QDialog, Ui_beam_location):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent=parent)
        self.setupUi(self)
        self.cam = ToupCamCamera()
        self.cam.open()
        time.sleep(2)
        self.counts = 0
    def __del__(self):
        self.cam.close()
        time.sleep(2)
    def acquire(self, path):
        filename = str(self.counts).zfill(5)+'.tif'
        self.cam.save_tiff(path+'\\'+filename)
        time.sleep(2)
        self.counts = self.counts + 1
        if os.path.exists(path+'\\'+filename):
            self.label_2.setPixmap(QPixmap(path+'\\'+filename).scaled(self.label_2.size()))
            self.label_2.repaint()
            return path
        else:
            print('No file in {path}'.format(path=path+'\\'+filename))
            return 'No file'
    def clean(self):
        self.counts = 0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = ToupAccquire()
    mainWindow.show()
    sys.exit(app.exec())