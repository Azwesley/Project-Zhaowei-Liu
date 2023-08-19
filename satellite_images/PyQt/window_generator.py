from satellite_Qt import Ui_Form
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QProgressBar
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.Qt import *

from predict import predict_images

from tqdm import tqdm_notebook as tqdm
import os
import shutil
# from PyQt.test_code import predict


class CamShow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(CamShow, self).__init__(parent)
        self.setupUi(self)

        self.fileBtn.clicked.connect(lambda: self.loadImage('single_image'))

        self.img_file_btn.clicked.connect(lambda: self.loadImage('image_file'))

    def loadImage(self, opt):
        if opt == 'single_image':
            image_absPath, _ = QFileDialog.getOpenFileName(self, 'select a image', '.', 'image type(*.jpg *.jpeg *.png )')
            if image_absPath:
                print(image_absPath)
                self.Infolabel.setText("🫡 Upload Image Successed")
                self.Infolabel.setStyleSheet("color:white")


                jpg = QPixmap(image_absPath).scaled(self.pre_imag_label.width(), self.pre_imag_label.height())
                self.pre_imag_label.setPixmap(jpg)

                self.check_Button.clicked.connect(lambda: self.start_check(image_absPath, 'single_image'))

        if opt  == 'image_file':
            image_file_path = QFileDialog.getExistingDirectory(self, 'OpenImageFile')
            image_list = []
            for i_path in os.listdir(image_file_path):
                img_path = image_file_path+'/'+i_path
                image_list.append(img_path)

            self.Infolabel.setText("🫡 Upload ImageFile successed")
            self.check_Button.clicked.connect(lambda: self.start_check(image_list,'image_file'))
            self.check_Button.clicked.connect(self.startProgress)
            self.timer = QBasicTimer()
            self.step = 0

    def startProgress(self):
        if self.timer.isActive():
            self.timer.stop()
            self.check_Button('processing')
        else:
            self.timer.start(100,self)
            self.check_Button.setText('finished')

    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            self.check_Button.setText('Finished')
            return
        self.step = self.step+1
        self.progressBar.setValue(self.step)


    def start_check(self, f_path, flag):

        cloud_file = './cloud_file'
        desert_file = './desert_file'
        green_area_file = './green_area_file'
        water_file = './water_file'
        agricultural_file = './agricultural'
        airplane_file = './airplane'
        baseballdiamond_file = './baseballdiamond'
        beach_file = './beach'
        buildings_file = './buildings'
        chaparral_file = './chaparral'
        denseresidential_file = './denseresidential'
        forest_file = './forest'
        freeway_file = './freeway'
        golfcourse_file = './golfcourse'
        harbor_file = './harbor'
        intersection_file = './intersection'
        mediumresidential_file = './mediumresidential'
        mobilehomepark_file = './mobilehomepark'
        overpass_file = './overpass'
        parkinglot_file = './parkinglot'
        river_file = './river'
        runway_file = './runway'
        sparseresidential_file = './sparseresidential'
        storagetanks_file = 'sparseresidential'
        tenniscourt_file = 'tenniscourt'


        if flag == 'single_image':

            result, image_path = predict_images(f_path)
            print(result)

            if result:
                if result == 'agricultural' :
                    if not os.path.exists(agricultural_file):
                        os.makedirs(agricultural_file)
                        shutil.copy(image_path,agricultural_file)
                    else:
                        shutil.copy(image_path, agricultural_file)
                if result == 'airplane' :
                    if not os.path.exists(airplane_file):
                        os.makedirs(airplane_file)
                        shutil.copy(image_path,airplane_file)
                    else:
                        shutil.copy(image_path, airplane_file)
                if result == 'beach' :
                    if not os.path.exists(beach_file):
                        os.makedirs(beach_file)
                        shutil.copy(image_path,beach_file)
                    else:
                        shutil.copy(image_path, beach_file)
                if result == 'river' :
                    if not os.path.exists(river_file):
                        os.makedirs(river_file)
                        shutil.copy(image_path,river_file)
                    else:
                        shutil.copy(image_path, river_file)
                if result == 'baseballdiamond' :
                    if not os.path.exists(baseballdiamond_file):
                        os.makedirs(baseballdiamond_file)
                        shutil.copy(image_path, baseballdiamond_file)
                    else:
                        shutil.copy(image_path, baseballdiamond_file)
                if result == 'buildings' :
                    if not os.path.exists(buildings_file):
                        os.makedirs(buildings_file)
                        shutil.copy(image_path,buildings_file)
                    else:
                        shutil.copy(image_path, buildings_file)
                if result == 'chaparral' :
                    if not os.path.exists(chaparral_file):
                        os.makedirs(chaparral_file)
                        shutil.copy(image_path,chaparral_file)
                    else:
                        shutil.copy(image_path, chaparral_file)
                if result == 'denseresidential' :
                    if not os.path.exists(denseresidential_file):
                        os.makedirs(denseresidential_file)
                        shutil.copy(image_path,denseresidential_file)
                    else:
                        shutil.copy(image_path, denseresidential_file)
                if result == 'forest' :
                    if not os.path.exists(forest_file):
                        os.makedirs(forest_file)
                        shutil.copy(image_path,forest_file)
                    else:
                        shutil.copy(image_path, forest_file)
                if result == 'freeway' :
                    if not os.path.exists(freeway_file):
                        os.makedirs(freeway_file)
                        shutil.copy(image_path,freeway_file)
                    else:
                        shutil.copy(image_path, freeway_file)
                if result == 'golfcourse' :
                    if not os.path.exists(golfcourse_file):
                        os.makedirs(golfcourse_file)
                        shutil.copy(image_path,golfcourse_file)
                    else:
                        shutil.copy(image_path, golfcourse_file)
                if result == 'harbor' :
                    if not os.path.exists(harbor_file):
                        os.makedirs(harbor_file)
                        shutil.copy(image_path,harbor_file)
                    else:
                        shutil.copy(image_path, harbor_file)
                if result == 'intersection' :
                    if not os.path.exists(intersection_file):
                        os.makedirs(intersection_file)
                        shutil.copy(image_path,intersection_file)
                    else:
                        shutil.copy(image_path, intersection_file)
                if result == 'mediumresidential' :
                    if not os.path.exists(mediumresidential_file):
                        os.makedirs(mediumresidential_file)
                        shutil.copy(image_path,mediumresidential_file)
                    else:
                        shutil.copy(image_path, mediumresidential_file)
                if result == 'mobilehomepark' :
                    if not os.path.exists(mobilehomepark_file):
                        os.makedirs(mobilehomepark_file)
                        shutil.copy(image_path,mobilehomepark_file)
                    else:
                        shutil.copy(image_path, mobilehomepark_file)
                if result == 'overpass' :
                    if not os.path.exists(overpass_file):
                        os.makedirs(overpass_file)
                        shutil.copy(image_path,overpass_file)
                    else:
                        shutil.copy(image_path, overpass_file)
                if result == 'parkinglot' :
                    if not os.path.exists(parkinglot_file):
                        os.makedirs(parkinglot_file)
                        shutil.copy(image_path,parkinglot_file)
                    else:
                        shutil.copy(image_path, parkinglot_file)
                if result == 'runway' :
                    if not os.path.exists(runway_file):
                        os.makedirs(runway_file)
                        shutil.copy(image_path,runway_file)
                    else:
                        shutil.copy(image_path, runway_file)
                if result == 'sparseresidential' :
                    if not os.path.exists(sparseresidential_file):
                        os.makedirs(sparseresidential_file)
                        shutil.copy(image_path,sparseresidential_file)
                    else:
                        shutil.copy(image_path, sparseresidential_file)
                if result == 'sparseresidential' :
                    if not os.path.exists(sparseresidential_file):
                        os.makedirs(sparseresidential_file)
                        shutil.copy(image_path,sparseresidential_file)
                    else:
                        shutil.copy(image_path, sparseresidential_file)
                if result == 'storagetanks' :
                    if not os.path.exists(storagetanks_file):
                        os.makedirs(storagetanks_file)
                        shutil.copy(image_path,storagetanks_file)
                    else:
                        shutil.copy(image_path, storagetanks_file)
                if result == 'tenniscourt' :
                    if not os.path.exists(tenniscourt_file):
                        os.makedirs(tenniscourt_file)
                        shutil.copy(image_path,tenniscourt_file)
                    else:
                        shutil.copy(image_path, tenniscourt_file)


                if result == 'cloud' :
                    if not os.path.exists(cloud_file):
                        os.makedirs(cloud_file)
                        shutil.copy(image_path, cloud_file)
                    else:
                        shutil.copy(image_path, cloud_file)

                if result == 'desert' :
                    if not os.path.exists(desert_file):
                        os.makedirs(desert_file)
                        shutil.copy(image_path, desert_file)
                    else:
                        shutil.copy(image_path, desert_file)

                if result == 'green_area' :
                    if not os.path.exists(green_area_file):
                        os.makedirs(green_area_file)
                        shutil.copy(image_path, green_area_file)
                    else:
                        shutil.copy(image_path, cloud_file)

                if result == 'water' :
                    if not os.path.exists(water_file):
                        os.makedirs(water_file)
                        shutil.copy(image_path, water_file)
                    else:
                        shutil.copy(image_path, water_file)

                self.result_label.setText(result+'️  💯')
                self.result_label.setStyleSheet('font-size:40px; color:white')


        if flag == 'image_file':
            for abs_pth in tqdm(f_path):
                result, image_path = predict_images(abs_pth)
                print(result)
                if result:
                    if result == 'agricultural' :
                        if not os.path.exists(agricultural_file):
                            os.makedirs(agricultural_file)
                            shutil.copy(image_path,agricultural_file)
                        else:
                            shutil.copy(image_path, agricultural_file)
                    if result == 'airplane' :
                        if not os.path.exists(airplane_file):
                            os.makedirs(airplane_file)
                            shutil.copy(image_path,airplane_file)
                        else:
                            shutil.copy(image_path, airplane_file)
                    if result == 'beach' :
                        if not os.path.exists(beach_file):
                            os.makedirs(beach_file)
                            shutil.copy(image_path,beach_file)
                        else:
                            shutil.copy(image_path, beach_file)
                    if result == 'river' :
                        if not os.path.exists(river_file):
                            os.makedirs(river_file)
                            shutil.copy(image_path,river_file)
                        else:
                            shutil.copy(image_path, river_file)
                    if result == 'baseballdiamond' :
                        if not os.path.exists(baseballdiamond_file):
                            os.makedirs(baseballdiamond_file)
                            shutil.copy(image_path, baseballdiamond_file)
                        else:
                            shutil.copy(image_path, baseballdiamond_file)
                    if result == 'buildings' :
                        if not os.path.exists(buildings_file):
                            os.makedirs(buildings_file)
                            shutil.copy(image_path,buildings_file)
                        else:
                            shutil.copy(image_path, buildings_file)
                    if result == 'chaparral' :
                        if not os.path.exists(chaparral_file):
                            os.makedirs(chaparral_file)
                            shutil.copy(image_path,chaparral_file)
                        else:
                            shutil.copy(image_path, chaparral_file)
                    if result == 'denseresidential' :
                        if not os.path.exists(denseresidential_file):
                            os.makedirs(denseresidential_file)
                            shutil.copy(image_path,denseresidential_file)
                        else:
                            shutil.copy(image_path, denseresidential_file)
                    if result == 'forest' :
                        if not os.path.exists(forest_file):
                            os.makedirs(forest_file)
                            shutil.copy(image_path,forest_file)
                        else:
                            shutil.copy(image_path, forest_file)
                    if result == 'freeway' :
                        if not os.path.exists(freeway_file):
                            os.makedirs(freeway_file)
                            shutil.copy(image_path,freeway_file)
                        else:
                            shutil.copy(image_path, freeway_file)
                    if result == 'golfcourse' :
                        if not os.path.exists(golfcourse_file):
                            os.makedirs(golfcourse_file)
                            shutil.copy(image_path,golfcourse_file)
                        else:
                            shutil.copy(image_path, golfcourse_file)
                    if result == 'harbor' :
                        if not os.path.exists(harbor_file):
                            os.makedirs(harbor_file)
                            shutil.copy(image_path,harbor_file)
                        else:
                            shutil.copy(image_path, harbor_file)
                    if result == 'intersection' :
                        if not os.path.exists(intersection_file):
                            os.makedirs(intersection_file)
                            shutil.copy(image_path,intersection_file)
                        else:
                            shutil.copy(image_path, intersection_file)
                    if result == 'mediumresidential' :
                        if not os.path.exists(mediumresidential_file):
                            os.makedirs(mediumresidential_file)
                            shutil.copy(image_path,mediumresidential_file)
                        else:
                            shutil.copy(image_path, mediumresidential_file)
                    if result == 'mobilehomepark' :
                        if not os.path.exists(mobilehomepark_file):
                            os.makedirs(mobilehomepark_file)
                            shutil.copy(image_path,mobilehomepark_file)
                        else:
                            shutil.copy(image_path, mobilehomepark_file)
                    if result == 'overpass' :
                        if not os.path.exists(overpass_file):
                            os.makedirs(overpass_file)
                            shutil.copy(image_path,overpass_file)
                        else:
                            shutil.copy(image_path, overpass_file)
                    if result == 'parkinglot' :
                        if not os.path.exists(parkinglot_file):
                            os.makedirs(parkinglot_file)
                            shutil.copy(image_path,parkinglot_file)
                        else:
                            shutil.copy(image_path, parkinglot_file)
                    if result == 'runway' :
                        if not os.path.exists(runway_file):
                            os.makedirs(runway_file)
                            shutil.copy(image_path,runway_file)
                        else:
                            shutil.copy(image_path, runway_file)
                    if result == 'sparseresidential' :
                        if not os.path.exists(sparseresidential_file):
                            os.makedirs(sparseresidential_file)
                            shutil.copy(image_path,sparseresidential_file)
                        else:
                            shutil.copy(image_path, sparseresidential_file)
                    if result == 'sparseresidential' :
                        if not os.path.exists(sparseresidential_file):
                            os.makedirs(sparseresidential_file)
                            shutil.copy(image_path,sparseresidential_file)
                        else:
                            shutil.copy(image_path, sparseresidential_file)
                    if result == 'storagetanks' :
                        if not os.path.exists(storagetanks_file):
                            os.makedirs(storagetanks_file)
                            shutil.copy(image_path,storagetanks_file)
                        else:
                            shutil.copy(image_path, storagetanks_file)
                    if result == 'tenniscourt' :
                        if not os.path.exists(tenniscourt_file):
                            os.makedirs(tenniscourt_file)
                            shutil.copy(image_path,tenniscourt_file)
                        else:
                            shutil.copy(image_path, tenniscourt_file)


                    if result == 'cloud' :
                        if not os.path.exists(cloud_file):
                            os.makedirs(cloud_file)
                            shutil.copy(image_path, cloud_file)
                        else:
                            shutil.copy(image_path, cloud_file)

                    if result == 'desert' :
                        if not os.path.exists(desert_file):
                            os.makedirs(desert_file)
                            shutil.copy(image_path, desert_file)
                        else:
                            shutil.copy(image_path, desert_file)

                    if result == 'green_area' :
                        if not os.path.exists(green_area_file):
                            os.makedirs(green_area_file)
                            shutil.copy(image_path, green_area_file)
                        else:
                            shutil.copy(image_path, cloud_file)

                    if result == 'water' :
                        if not os.path.exists(water_file):
                            os.makedirs(water_file)
                            shutil.copy(image_path, water_file)
                        else:
                            shutil.copy(image_path, water_file)




    # def use_palette(self):
    #     self.setWindowTitle("")
    #     window_pale = QPalette()
    #     window_pale.setBrush(self.backgroundRole(),
    #                          QBrush(QPixmap("./1131665048665_.pic.jpg").scaled(
    #                              self.width(),self.height()
    #                          )))
    #     self.setPalette(window_pale)


if __name__ == '__main__':


    app = QApplication(sys.argv)
    ui = CamShow()
    # ui.use_palette()
    ui.show()
    sys.exit(app.exec())