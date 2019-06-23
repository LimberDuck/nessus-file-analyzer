# -*- coding: utf-8 -*-
u"""
nessus file analyzer by LimberDuck (pronounced *ˈlɪm.bɚ dʌk*) is a GUI
tool which enables you to parse multiple nessus files containing the results
of scans performed by using Nessus by (C) Tenable, Inc. and exports parsed
data to a Microsoft Excel Workbook for effortless analysis.
Copyright (C) 2019 Damian Krawczyk

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from nessus_file_analyzer import __about__


class About(QMessageBox):

    def __init__(self, parent=None):
        super(About, self).__init__(parent)

        self.setWindowTitle("About")
        self.appName = __about__.__title__
        self.version = __about__.__version__
        self.release_date = __about__.__release_date__

        website = __about__.__uri__
        email = __about__.__email__
        license_link = __about__.__license_link__
        license_name = __about__.__license_name__
        copyright_info = __about__.__copyright__
        msg_box = QMessageBox()
        msg_box.setWindowTitle(self.tr("About " + self.appName))
        msg_box.setTextFormat(Qt.RichText)
        # msg_box.setIconPixmap(QPixmap(ComicTaggerSettings.getGraphic('about.png')))
        msg_box.setText("<br>"
                        + self.appName + " v" + self.version + " [" + self.release_date + "] <br>"
                        + "Copyright " + copyright_info + "<br><br>"
                        + "<a href='{0}'>{0}</a><br><br>".format(website)
                        + "<a href='mailto:{0}'>{0}</a><br><br>".format(email)
                        + "License: <a href='{0}'>{1}</a>".format(license_link, license_name))

        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()
