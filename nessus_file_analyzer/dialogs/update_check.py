# -*- coding: utf-8 -*-
"""
nessus file analyzer (NFA) by LimberDuck (pronounced *ˈlɪm.bɚ dʌk*) is a GUI
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

import requests
from packaging import version

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from nessus_file_analyzer import __about__

PACKAGE_NAME = __about__.__package_name__


class UpdateCheck(QMessageBox):
    def __init__(self, parent=None):
        super(UpdateCheck, self).__init__(parent)

        self.appName = __about__.__title__
        self.current_version = __about__.__version__
        self.release_date = __about__.__release_date__

        self.setWindowTitle(self.tr(f"Update Check - {self.appName}"))
        self.setTextFormat(Qt.RichText)
        self.setStandardButtons(QMessageBox.Ok)

        latest_version, message = self.check_for_update()

        self.setText(message)
        self.exec_()

    def check_for_update(self):
        try:
            response = requests.get(
                f"https://pypi.org/pypi/{PACKAGE_NAME}/json", timeout=1.5
            )
            response.raise_for_status()
            latest = response.json()["info"]["version"]
            read_more = (
                f"Read more:<br>"
                f"<a href='https://limberduck.org/en/latest/tools/{PACKAGE_NAME}'>Documentation</a><br>"
                f"<a href='https://github.com/LimberDuck/{PACKAGE_NAME}'>GitHub</a><br>"
                f"<a href='https://github.com/LimberDuck/{PACKAGE_NAME}/releases'>Releases</a>"
            )
            if version.parse(latest) > version.parse(self.current_version):
                message = (
                    f"<b> A new version of {self.appName} is available!</b><br><br>"
                    f"Latest: <b>{latest}</b><br>"
                    f"You have: <b>{self.current_version}</b><br><br>"
                    f"Update with:<br>"
                    f"<code>pip install -U {PACKAGE_NAME}</code><br><br>"
                    f"{read_more}"
                )
            elif version.parse(latest) == version.parse(self.current_version):
                message = (
                    f"You are using the latest version of {self.appName}: <b>{self.current_version}</b><br><br>"
                    f"{read_more}"
                )

            else:
                message = (
                    f"You are using a <b>pre-release</b> version of {self.appName}: {self.current_version}<br><br>"
                    f"Latest released version: {latest}<br><br>"
                    f"{read_more}"
                )
            return latest, message

        except requests.exceptions.ConnectionError as e:
            return (
                None,
                f"Could not check for updates: <br><br><i>Connection error</i><br><br>{e}",
            )
        except Exception as e:
            return None, f"Could not check for updates:<br><br>{e}"
