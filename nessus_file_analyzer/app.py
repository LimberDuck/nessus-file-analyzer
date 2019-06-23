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

import datetime
import glob
import os
import time
import traceback
import xlsxwriter
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import subprocess
import platform
import nessus_file_reader as nfr
import nessus_file_analyzer as nfa


class MainWindow(QMainWindow, nfa.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.__files_to_pars = []
        self.__parsing_settings = {}
        self.__target_directory = ''
        self.__target_directory_changed = False
        self.__file_conversion_counter = 0
        self.__suffix = ''
        self.update_parsing_settings('suffix', self.__suffix)
        self.__suffix_template = ''
        self.update_parsing_settings('suffix_template', self.__suffix_template)
        self.__target_file_name_prefix = 'security_report'
        self.update_parsing_settings('target_file_name_prefix', self.__target_file_name_prefix)

        # reports
        self.__report_scan_enabled = False
        self.update_parsing_settings('report_scan_enabled', self.__report_scan_enabled)
        self.__report_host_enabled = False
        self.update_parsing_settings('report_host_enabled', self.__report_host_enabled)
        self.__report_vulnerabilities_enabled = False
        self.update_parsing_settings('report_vulnerabilities_enabled', self.__report_vulnerabilities_enabled)
        self.__report_noncompliance_enabled = False
        self.update_parsing_settings('report_noncompliance_enabled', self.__report_noncompliance_enabled)

        # reports settings
        self.__report_scan_setting_debug_data_enabled = False
        self.update_parsing_settings('report_scan_debug_data_enabled',
                                     self.__report_scan_setting_debug_data_enabled)
        self.__report_host_setting_debug_data_enabled = False
        self.update_parsing_settings('report_host_debug_data_enabled',
                                     self.__report_host_setting_debug_data_enabled)
        self.__report_vulnerabilities_setting_debug_data_enabled = False
        self.update_parsing_settings('report_vulnerabilities_debug_data_enabled',
                                     self.__report_vulnerabilities_setting_debug_data_enabled)
        self.__report_vulnerabilities_setting_none_filter_out = False
        self.update_parsing_settings('report_vulnerabilities_none_filter_out',
                                     self.__report_vulnerabilities_setting_none_filter_out)
        self.__report_noncompliance_setting_debug_data_enabled = False
        self.update_parsing_settings('report_noncompliance_debug_data_enabled',
                                     self.__report_noncompliance_enabled)
        self.__report_set_source_directory_as_target_directory_enabled = False
        self.update_parsing_settings('set_source_directory_as_target_directory_enabled',
                                     self.__report_set_source_directory_as_target_directory_enabled)

        self.parsing_thread = ParsingThread(files_to_pars=self.__files_to_pars,
                                            target_directory=self.__target_directory,
                                            target_directory_changed=self.__target_directory_changed,
                                            parsing_settings=self.__parsing_settings)

        self.actionOpen_file.triggered.connect(self.open_files)
        self.actionOpen_directory.triggered.connect(self.open_directory)
        self.actionExit.triggered.connect(self.exit_application)

        self.actionStart_conversion.triggered.connect(self.parsing_thread_start)
        self.actionChange_target_directory.triggered.connect(self.change_target_directory)
        self.actionOpen_target_directory.triggered.connect(self.open_target_directory)
        self.actionAbout.triggered.connect(self.open_dialog_about)

        self.checkBox_report_scan.stateChanged.connect(self.report_scan_changed)
        self.checkBox_debug_data_scan.stateChanged.connect(self.report_scan_setting_debug_changed)
        self.checkBox_report_host.stateChanged.connect(self.report_host_changed)
        self.checkBox_debug_data_host.stateChanged.connect(self.report_host_setting_debug_changed)
        self.checkBox_report_vulnerabilities.stateChanged.connect(self.report_vulnerabilities_changed)
        self.checkBox_vulnerabilities_none_filter_out.stateChanged.connect(
            self.report_vulnerabilities_setting_none_filter_out_changed)
        self.checkBox_debug_data_vulnerabilities.stateChanged.connect(
            self.report_vulnerabilities_setting_debug_changed)
        self.checkBox_report_noncompliance.stateChanged.connect(self.report_noncompliance_changed)
        self.checkBox_debug_data_noncompliance.stateChanged.connect(self.report_noncompliance_setting_debug_changed)

        self.checkBox_set_source_directory_as_target_directory.stateChanged.connect(
            self.set_source_directory_as_target_directory_changed)
        self.checkBox_suffix_timestamp.stateChanged.connect(self.suffix_timestamp_changed)
        self.checkBox_suffix_custom.stateChanged.connect(self.suffix_custom_changed)

        self.pushButton_start.clicked.connect(self.parsing_thread_start)
        self.pushButton_target_dir_change.clicked.connect(self.change_target_directory)
        self.pushButton_target_dir_open.clicked.connect(self.open_target_directory)

        self.checkBox_suffix_timestamp.setChecked(True)
        self.groupBox_options_scan.setDisabled(True)
        self.groupBox_options_host.setDisabled(True)
        self.groupBox_options_vulnerabilities.setDisabled(True)
        self.groupBox_options_noncompliance.setDisabled(True)
        self.pushButton_start.setDisabled(True)
        self.actionStart_conversion.setDisabled(True)
        self.progressBar.setHidden(True)

        cwd = os.getcwd()
        self.set_target_directory(cwd)
        self.get_target_directory_from_file()

        files = sys.argv[1:]
        if len(files) > 0:
            self.list_of_files_to_pars(files)
            source_file_path = os.path.dirname(os.path.abspath(files[0]))
            self.set_target_directory(source_file_path)
            self.get_target_directory_from_file()

        self.progressBar.setRange(0, 10)

        self.print_log('If you don\'t know how to use particular options '
                       'hover mouse pointer on option for which you have any doubts to see tooltip. '
                       'Hover mouse pointer here, to see tooltip for progress preview.',
                       'red')

    def print_settings(self):
        """
        Function prints all settings specified by user.
        """
        print('>>>')
        for setting, value in self.__parsing_settings.items():
            if value:
                print(setting, value, '++++++++++++++++++++++++++++')
            else:
                print(setting, value)
        print('<<<')

    def report_scan_changed(self):
        """
        Function enables or disables setting which allow generation of spreadsheet with scan sum-up.
        """
        if self.checkBox_report_scan.isChecked():
            info = 'Scan report enabled.'
            self.__report_scan_enabled = True
            self.groupBox_options_scan.setEnabled(True)
        else:
            info = 'Scan report disabled.'
            self.__report_scan_enabled = False
            self.groupBox_options_scan.setDisabled(True)
        color = 'green'
        self.print_log(info, color)
        self.update_parsing_settings('report_scan_enabled', self.__report_scan_enabled)
        # self.print_settings()

        if (self.__report_scan_enabled
            or self.__report_host_enabled
            or self.__report_vulnerabilities_enabled
            or self.__report_noncompliance_enabled) \
                and self.__files_to_pars:
            self.pushButton_start.setEnabled(True)
            self.actionStart_conversion.setEnabled(True)

        if not self.__report_scan_enabled \
                and not self.__report_host_enabled \
                and not self.__report_vulnerabilities_enabled \
                and not self.__report_noncompliance_enabled:
            self.pushButton_start.setDisabled(True)
            self.actionStart_conversion.setDisabled(True)

    def report_scan_setting_debug_changed(self):
        """
        Function enables or disables setting which allow generation of spreadsheet with scan sum-up with additional
        data.
        """
        if self.checkBox_debug_data_scan.isChecked():
            info = 'Scan report debug data enabled.'
            self.__report_scan_setting_debug_data_enabled = True
        else:
            info = 'Scan report debug data disabled.'
            self.__report_scan_setting_debug_data_enabled = False
        color = 'green'
        self.print_log(info, color)
        self.update_parsing_settings('report_scan_debug_data_enabled', self.__report_scan_setting_debug_data_enabled)
        # self.print_settings()

    def report_host_changed(self):
        """
        Function enables or disables setting which allow generation of spreadsheet with host sum-up.
        """
        if self.checkBox_report_host.isChecked():
            info = 'Host report enabled.'
            self.__report_host_enabled = True
            self.groupBox_options_host.setEnabled(True)
        else:
            info = 'Host report disabled.'
            self.__report_host_enabled = False
            self.groupBox_options_host.setDisabled(True)
        color = 'green'
        self.print_log(info, color)
        self.update_parsing_settings('report_host_enabled', self.__report_host_enabled)
        # self.print_settings()

        if (self.__report_scan_enabled
            or self.__report_host_enabled
            or self.__report_vulnerabilities_enabled
            or self.__report_noncompliance_enabled) \
                and self.__files_to_pars:
            self.pushButton_start.setEnabled(True)
            self.actionStart_conversion.setEnabled(True)

        if not self.__report_scan_enabled \
                and not self.__report_host_enabled \
                and not self.__report_vulnerabilities_enabled \
                and not self.__report_noncompliance_enabled:
            self.pushButton_start.setDisabled(True)
            self.actionStart_conversion.setDisabled(True)

    def report_host_setting_debug_changed(self):
        """
        Function enables or disables setting which allow generation of spreadsheet with host sum-up with additional
        data.
        """
        if self.checkBox_debug_data_host.isChecked():
            info = 'Host report debug data enabled.'
            self.__report_host_setting_debug_data_enabled = True
        else:
            info = 'Host report debug data disabled.'
            self.__report_host_setting_debug_data_enabled = False
        color = 'green'
        self.print_log(info, color)
        self.update_parsing_settings('report_host_debug_data_enabled', self.__report_host_setting_debug_data_enabled)
        # self.print_settings()

    def report_vulnerabilities_changed(self):
        """
        Function enables or disables setting which allow generation of spreadsheet with vulnerabilities sum-up.
        """
        if self.checkBox_report_vulnerabilities.isChecked():
            info = 'Vulnerabilities report enabled.'
            self.__report_vulnerabilities_enabled = True
            self.groupBox_options_vulnerabilities.setEnabled(True)
        else:
            info = 'Vulnerabilities report disabled.'
            self.__report_vulnerabilities_enabled = False
            self.groupBox_options_vulnerabilities.setDisabled(True)
        color = 'green'
        self.print_log(info, color)
        self.update_parsing_settings('report_vulnerabilities_enabled', self.__report_vulnerabilities_enabled)
        # self.print_settings()

        if (self.__report_scan_enabled
            or self.__report_host_enabled
            or self.__report_vulnerabilities_enabled
            or self.__report_noncompliance_enabled) \
                and self.__files_to_pars:
            self.pushButton_start.setEnabled(True)
            self.actionStart_conversion.setEnabled(True)

        if not self.__report_scan_enabled \
                and not self.__report_host_enabled \
                and not self.__report_vulnerabilities_enabled \
                and not self.__report_noncompliance_enabled:
            self.pushButton_start.setDisabled(True)
            self.actionStart_conversion.setDisabled(True)

    def report_vulnerabilities_setting_debug_changed(self):
        """
        Function enables or disables setting which allow generation of spreadsheet with vulnerabilities sum-up with
        additional data.
        """
        if self.checkBox_debug_data_vulnerabilities.isChecked():
            info = 'Vulnerabilities report debug data enabled.'
            self.__report_vulnerabilities_setting_debug_data_enabled = True
        else:
            info = 'Vulnerabilities report debug data disabled.'
            self.__report_vulnerabilities_setting_debug_data_enabled = False
        color = 'green'
        self.print_log(info, color)
        self.update_parsing_settings('report_vulnerabilities_debug_data_enabled',
                                     self.__report_vulnerabilities_setting_debug_data_enabled)
        # self.print_settings()

    def report_vulnerabilities_setting_none_filter_out_changed(self):
        """
        Function enables or disables setting which allow generation of spreadsheet with vulnerabilities sum-up with
        filtered out vulnerabilities with Risk Factor equal None.
        """
        if self.checkBox_vulnerabilities_none_filter_out.isChecked():
            info = 'Vulnerabilities report None filter out enabled.'
            self.__report_vulnerabilities_setting_none_filter_out = True
        else:
            info = 'Vulnerabilities report None filter out data disabled.'
            self.__report_vulnerabilities_setting_none_filter_out = False
        color = 'green'
        self.print_log(info, color)
        self.update_parsing_settings('report_vulnerabilities_none_filter_out',
                                     self.__report_vulnerabilities_setting_none_filter_out)
        # self.print_settings()

    def report_noncompliance_changed(self):
        """
        Function enables or disables setting which allow generation of spreadsheet with noncompliance sum-up.
        """
        if self.checkBox_report_noncompliance.isChecked():
            info = 'Noncompliance report enabled.'
            self.__report_noncompliance_enabled = True
            self.groupBox_options_noncompliance.setEnabled(True)
        else:
            info = 'Noncompliance report disabled.'
            self.__report_noncompliance_enabled = False
            self.groupBox_options_noncompliance.setDisabled(True)
        color = 'green'
        self.print_log(info, color)
        self.update_parsing_settings('report_noncompliance_enabled', self.__report_noncompliance_enabled)
        # self.print_settings()

        if (self.__report_scan_enabled
            or self.__report_host_enabled
            or self.__report_vulnerabilities_enabled
            or self.__report_noncompliance_enabled) \
                and self.__files_to_pars:
            self.pushButton_start.setEnabled(True)
            self.actionStart_conversion.setEnabled(True)

        if not self.__report_scan_enabled \
                and not self.__report_host_enabled \
                and not self.__report_vulnerabilities_enabled \
                and not self.__report_noncompliance_enabled:
            self.pushButton_start.setDisabled(True)
            self.actionStart_conversion.setDisabled(True)

    def report_noncompliance_setting_debug_changed(self):
        """
        Function enables or disables setting which allow generation of spreadsheet with noncompliance sum-up with
        additional data.
        """
        if self.checkBox_debug_data_noncompliance.isChecked():
            info = 'noncompliance report debug data enabled.'
            self.__report_noncompliance_setting_debug_data_enabled = True
        else:
            info = 'noncompliance report debug data disabled.'
            self.__report_noncompliance_setting_debug_data_enabled = False
        color = 'green'
        self.print_log(info, color)
        self.update_parsing_settings('report_noncompliance_debug_data_enabled',
                                     self.__report_noncompliance_setting_debug_data_enabled)
        # self.print_settings()

    def set_source_directory_as_target_directory_changed(self):
        """
        Function enables or disables setting which inform about target directory which is set based on selected source
        directory.
        """
        if self.checkBox_set_source_directory_as_target_directory.isChecked():
            info = 'Target directory based on selected source enabled.'
            self.__report_set_source_directory_as_target_directory_enabled = True
        else:
            info = 'Target directory based on selected source disabled.'
            self.__report_set_source_directory_as_target_directory_enabled = False

        color = 'green'
        self.print_log(info, color)
        self.update_parsing_settings('report_set_source_directory_as_target_directory_enabled',
                                     self.__report_set_source_directory_as_target_directory_enabled)

    def suffix_timestamp_changed(self):
        """
        Function sets suffix appropriately if checkBox_suffix_timestamp has changed.
        """
        if self.checkBox_suffix_timestamp.isChecked() and not self.checkBox_suffix_custom.isChecked():
            time_now = datetime.datetime.now()
            time_now_formatted = time_now.strftime('%Y%m%d_%H%M%S')
            suffix = '_' + time_now_formatted
            self.change_suffix(suffix)
            self.label_target_file_name_value.setText(self.__target_file_name_prefix + suffix + '.xlsx')
            self.__suffix_template = 'suffix_timestamp'

        elif not self.checkBox_suffix_timestamp.isChecked() and self.checkBox_suffix_custom.isChecked():
            suffix_custom_value = self.lineEdit_suffix_custom_value.text()
            if suffix_custom_value:
                space = '_'
                self.__suffix_template = 'suffix_custom'
            else:
                space = ''
                self.__suffix_template = 'suffix_custom_empty'
            suffix = space + suffix_custom_value
            self.change_suffix(suffix)
            self.label_target_file_name_value.setText(self.__target_file_name_prefix + suffix + '.xlsx')

        elif self.checkBox_suffix_timestamp.isChecked() and self.checkBox_suffix_custom.isChecked():
            time_now = datetime.datetime.now()
            time_now_formatted = time_now.strftime('%Y%m%d_%H%M%S')
            suffix_custom_value = self.lineEdit_suffix_custom_value.text()
            if suffix_custom_value:
                space = '_'
                self.__suffix_template = 'suffix_custom_timestamp'
            else:
                space = ''
                self.__suffix_template = 'suffix_custom_empty_timestamp'
            suffix = space + suffix_custom_value + '_' + time_now_formatted
            self.change_suffix(suffix)
            self.label_target_file_name_value.setText(self.__target_file_name_prefix + suffix + '.xlsx')

        else:
            self.change_suffix('')
            self.label_target_file_name_value.setText(self.__target_file_name_prefix + '.xlsx')
            self.__suffix_template = 'empty'

    def suffix_custom_changed(self):
        """
        Function sets suffix appropriately if checkBox_suffix_custom has changed.
        """
        if self.checkBox_suffix_custom.isChecked() and not self.checkBox_suffix_timestamp.isChecked():
            suffix_custom_value = self.lineEdit_suffix_custom_value.text()
            if suffix_custom_value:
                space = '_'
                self.__suffix_template = 'suffix_custom'
            else:
                space = ''
                self.__suffix_template = 'suffix_custom_empty'
            suffix = space + suffix_custom_value
            self.change_suffix(suffix)
            self.label_target_file_name_value.setText(self.__target_file_name_prefix + suffix + '.xlsx')

        elif not self.checkBox_suffix_custom.isChecked() and self.checkBox_suffix_timestamp.isChecked():
            time_now = datetime.datetime.now()
            time_now_formatted = time_now.strftime('%Y%m%d_%H%M%S')
            suffix = '_' + time_now_formatted
            self.change_suffix(suffix)
            self.__suffix_template = 'suffix_timestamp'
            self.label_target_file_name_value.setText(self.__target_file_name_prefix + suffix + '.xlsx')

        elif self.checkBox_suffix_custom.isChecked() and self.checkBox_suffix_timestamp.isChecked():
            time_now = datetime.datetime.now()
            time_now_formatted = time_now.strftime('%Y%m%d_%H%M%S')
            suffix_custom_value = self.lineEdit_suffix_custom_value.text()
            if suffix_custom_value:
                space = '_'
                self.__suffix_template = 'suffix_timestamp_custom'
            else:
                space = ''
                self.__suffix_template = 'suffix_timestamp_custom_empty'
            suffix = '_' + time_now_formatted + space + suffix_custom_value
            self.change_suffix(suffix)
            self.label_target_file_name_value.setText(self.__target_file_name_prefix + suffix + '.xlsx')

        else:
            self.change_suffix('')
            self.label_target_file_name_value.setText(self.__target_file_name_prefix + '.xlsx')
            self.__suffix_template = 'empty'

    @staticmethod
    def open_dialog_about():
        """
        Function opens About dialog.
        """
        nfa.About()

    def parsing_thread_start(self):
        """
        Function starts separate thread to pars selected files.
        """
        self.__file_conversion_counter = 0
        self.statusbar.clearMessage()
        self.progressBar.setVisible(True)

        info = 'Conversion started.'
        color = 'blue'
        self.print_log(info, color=color)
        try:
            if self.__suffix_template == 'suffix_timestamp':
                time_now = datetime.datetime.now()
                time_now_formatted = time_now.strftime('%Y%m%d_%H%M%S')
                self.update_parsing_settings('suffix', '_' + time_now_formatted)

            elif self.__suffix_template == 'suffix_custom':
                suffix_custom_value = self.lineEdit_suffix_custom_value.text()
                self.update_parsing_settings('suffix', '_' + suffix_custom_value)

            elif self.__suffix_template == 'suffix_custom_empty':
                self.update_parsing_settings('suffix', '')

            elif self.__suffix_template == 'suffix_custom_timestamp':
                time_now = datetime.datetime.now()
                time_now_formatted = time_now.strftime('%Y%m%d_%H%M%S')
                suffix_custom_value = self.lineEdit_suffix_custom_value.text()
                self.update_parsing_settings('suffix', '_' + suffix_custom_value + '_' + time_now_formatted)

            elif self.__suffix_template == 'suffix_custom_empty_timestamp':
                time_now = datetime.datetime.now()
                time_now_formatted = time_now.strftime('%Y%m%d_%H%M%S')
                self.update_parsing_settings('suffix', '_' + time_now_formatted)

            elif self.__suffix_template == 'suffix_timestamp_custom':
                time_now = datetime.datetime.now()
                time_now_formatted = time_now.strftime('%Y%m%d_%H%M%S')
                suffix_custom_value = self.lineEdit_suffix_custom_value.text()
                self.update_parsing_settings('suffix', '_' + time_now_formatted + '_' + suffix_custom_value)

            elif self.__suffix_template == 'suffix_timestamp_custom_empty':
                time_now = datetime.datetime.now()
                time_now_formatted = time_now.strftime('%Y%m%d_%H%M%S')
                self.update_parsing_settings('suffix', '_' + time_now_formatted)

            elif self.__suffix_template == 'empty':
                self.update_parsing_settings('suffix', '')

            self.parsing_thread = ParsingThread(files_to_pars=self.__files_to_pars,
                                                target_directory=self.__target_directory,
                                                target_directory_changed=self.__target_directory_changed,
                                                parsing_settings=self.__parsing_settings)
            self.parsing_thread.start()
            self.parsing_thread.signal.connect(self.parsing_thread_done)

            self.parsing_thread.progress.connect(self.conversion_progress)
            self.parsing_thread.print_status_bar_info.connect(self.print_status_bar_info)

        except Exception as e:
            color = 'red'
            self.print_log('\nUps... ERROR occurred. \n\n' + str(e), color=color)
            traceback.print_exc()
            print('>>>', e, '<<<')

    def print_status_bar_info(self, text):
        """
        Function sends notification via status bar about progress of conversion for each input file.
        :param text: text send to status bar
        """
        self.statusbar.clearMessage()
        self.statusbar.showMessage(text)
        self.statusbar.repaint()

    def conversion_progress(self, host_number, all_hosts_number):
        """
        Function shows conversion progress for each input file.
        Input parameters are used to set progress bar values.
        :param host_number: number of currently processed host in input file currently processed
        :param all_hosts_number: number of all hosts in input file currently processed
        """
        self.progressBar.setRange(0, all_hosts_number)
        self.progressBar.setValue(host_number)

    def parsing_thread_done(self, info):
        """
        Function shows information from parsing threads.
        :param info: information to display
        """
        if '[action=start]' in info:
            color = 'blue'
            self.print_log(info, color)
        elif '[action=end  ]' in info:
            color = 'green'
            self.print_log(info, color)
        else:
            color = 'black'
            self.print_log(info, color)

    def update_parsing_settings(self, setting_name, setting_value):
        """
        Function gets current parsing setting and updates dictionary containing all parsing settings.
        :param setting_name: setting key name
        :param setting_value: setting value
        """
        self.__parsing_settings[setting_name] = setting_value

    def set_suffix(self, suffix_value):
        """
        Function sets given suffix into private variable __suffix and update parsing settings.
        :param suffix_value: input suffix
        """
        self.__suffix = suffix_value
        self.update_parsing_settings('suffix', suffix_value)

    def change_suffix(self, suffix_value):
        """
        Function changes given suffix in private variable.
        Confirmation is send to GUI into progress preview.
        :param suffix_value: new suffix value
        """
        old_suffix = self.__suffix
        new_suffix = suffix_value

        self.set_suffix(new_suffix)

        color = 'green'
        info = 'Suffix changed from "' + old_suffix + '" to "' + new_suffix + '"'
        self.print_log(info, color)

    def set_target_directory(self, target_directory_value):
        """
        Function sets given target directory into private variable __target_directory.
        :param target_directory_value: target directory
        """
        self.__target_directory = target_directory_value

    def get_target_directory_from_file(self):
        """
        Function gets target directory from private variable __target_directory
        and set it into lineEdit_target_directory.
        Works only if user used selection by one or more files.
        """
        self.lineEdit_target_directory.setText(self.__target_directory)

    def get_target_directory_from_directory(self):
        """
        Function gets target directory from private variable __target_directory
        and set it into lineEdit_target_directory.
        Works only if user used selection by directory.
        """
        self.lineEdit_target_directory.setText(self.__target_directory)

    def change_target_directory(self):
        """
        Function changes target directory and set it in private variable __target_directory.
        Confirmation is send to GUI into progress preview.
        """
        old_target_directory = self.__target_directory

        title = 'Choose new target directory'
        starting_directory = ''
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly

        file_dialog = QFileDialog()

        directories = file_dialog.getExistingDirectory(None, title, starting_directory, options=options)

        if directories:
            directories = nfr.file.nessus_scan_file_name_with_path(directories)
            self.set_target_directory(directories)
            self.get_target_directory_from_file()

            color = 'green'
            info = 'Target directory changed from "' + old_target_directory + '" to "' + self.__target_directory + '"'
            self.print_log(info, color)
            self.__target_directory_changed = True
        else:
            info = 'Target directory not changed.'
            color = 'black'
            self.print_log(info, color=color)
            self.__target_directory_changed = False

    def open_files(self):
        """
        Function get list of files via dialog window.
        Possible to select one or more files.
        """
        info = 'File\-s opening.'
        color = 'black'
        self.print_log(info, color=color)

        extension = '*.nessus'

        title = 'Open {0} files'.format(extension)
        starting_directory = ''
        file_filter = 'nessus ({0})'.format(extension)
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)

        files = file_dialog.getOpenFileNames(self, title, starting_directory, filter=file_filter, options=options)
        files_only = files[0]
        # print(len(files_only),files_only)
        if len(files_only):
            if self.checkBox_set_source_directory_as_target_directory.isChecked():
                for file_name in files_only:
                    # print(file_name)
                    target_directory = os.path.dirname(os.path.abspath(file_name))
                    self.set_target_directory(target_directory)
                    # print(target_directory)

                self.get_target_directory_from_file()

            self.list_of_files_to_pars(files_only)

            if (self.__report_scan_enabled
                    or self.__report_host_enabled
                    or self.__report_vulnerabilities_enabled
                    or self.__report_noncompliance_enabled):
                self.pushButton_start.setEnabled(True)
                self.actionStart_conversion.setEnabled(True)
        else:
            number_of_files = 0
            info = 'Selected {0} files.'.format(str(number_of_files))
            color = 'black'
            self.print_log(info, color=color)

    @staticmethod
    def check_if_subdirectory_exist(main_directory):
        """
        Function verifies whether provided directory has any subdirectories.
        :param main_directory: path to selected directory
        :return: 0 if there is no subdirectories
                 number_of_directories > 0 if there is any subdirectory, where number_of_directories is information
                 about number of subdirectories.
        """
        pattern = os.path.join(main_directory, '*')
        number_of_directories = 0
        for candidate in glob.glob(pattern):
            if os.path.isdir(candidate):
                number_of_directories += 1
                break
        return number_of_directories

    def open_directory(self):
        """
        Function gets list of files via dialog window.
        Possible to get files from selected directory and subdirectories.
        """
        info = 'Files from directory and subdirectories opening.'
        color = 'black'
        self.print_log(info, color=color)

        extension = '*.nessus'

        title = 'Open {0} files directory'.format(extension)
        starting_directory = ''
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly

        file_dialog = QFileDialog()
        directories = file_dialog.getExistingDirectory(None, title, starting_directory, options=options)
        os_separator = os.path.sep
        target_directory = os.path.abspath(directories)

        if directories:
            if self.checkBox_set_source_directory_as_target_directory.isChecked():
                self.set_target_directory(target_directory)
                self.get_target_directory_from_directory()
                # print(target_directory)

            files = glob.glob(target_directory + os_separator + '**' + os_separator + extension, recursive=True)
            # print(files)
            self.list_of_files_to_pars(files)

            if (self.__report_scan_enabled
                    or self.__report_host_enabled
                    or self.__report_vulnerabilities_enabled
                    or self.__report_noncompliance_enabled):
                self.pushButton_start.setEnabled(True)
                self.actionStart_conversion.setEnabled(True)
        else:
            number_of_files = 0
            info = 'Selected {0} files.'.format(str(number_of_files))
            color = 'black'
            self.print_log(info, color=color)

    def open_target_directory(self):
        """
        Function open target directory taking into account Operating system:
        Linux: Linux
        Mac: Darwin
        Windows: Windows
        """

        os_name = platform.system()
        if os_name == 'Darwin':
            subprocess.call(['open', self.__target_directory])
        elif os_name == 'Windows':
            subprocess.call(['explorer', self.__target_directory])
        elif os_name == 'Linux':
            subprocess.call(['nautilus', self.__target_directory])
        else:
            info = 'Can\'t open directory, your Operating System {0} is not supported. Please report it to us.'.format(
                os_name)
            color = 'red'
            self.print_log(info, color=color)

    def print_log(self, log_value, color):
        """
        Function displays actions information in GUI in Progress preview.
        :param log_value: information to display
        :param color: color for given information
        """
        if color == 'black':
            color_set = QColor(0, 0, 0)
        elif color == 'red':
            color_set = QColor(230, 30, 30)
        elif color == 'green':
            color_set = QColor(60, 160, 60)
        elif color == 'blue':
            color_set = QColor(0, 0, 255)
        else:
            color_set = QColor(0, 0, 0)

        log_output = '[' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + '] ' + log_value

        self.textEdit_progress.setTextColor(color_set)
        self.textEdit_progress.append(log_output)
        self.textEdit_progress.moveCursor(QTextCursor.End)
        self.textEdit_progress.repaint()

    def exit_application(self):
        """
        Function to exit from application.
        """
        info = 'Exit application'
        print(info)
        color = 'black'
        self.print_log(info, color=color)
        self.close()

    def list_of_files_to_pars(self, files):
        """
        Function sets private variables:
        __files_to_pars with list of selected files,
        __file_conversion_counter reset to 0
        :param files: list of selected files.
        """
        number_of_files = len(files)
        if number_of_files == 1:
            suffix = ''
        else:
            suffix = 's'
        info = 'Selected {0} file{1}.'.format(str(number_of_files), suffix)
        color = 'black'
        self.print_log(info, color=color)
        self.print_status_bar_info(info)
        self.__files_to_pars = files

        color = 'black'
        for file_to_pars in self.__files_to_pars:
            file_to_pars = nfr.file.nessus_scan_file_name_with_path(file_to_pars)
            action_name = 'info '
            notification_info = '[action={0}] [source_file={1}]'.format(action_name, file_to_pars)
            self.print_log(notification_info, color=color)

        self.__file_conversion_counter = 0


class ParsingThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')
    progress = pyqtSignal(int, int)
    file_conversion_started = pyqtSignal(int)
    print_status_bar_info = pyqtSignal('QString')

    def __init__(self, files_to_pars, target_directory, target_directory_changed, parsing_settings, parent=None):
        super(ParsingThread, self).__init__(parent)

        self.files_to_pars = files_to_pars
        self.target_directory_changed = target_directory_changed
        self.target_directory = target_directory
        self.parsing_settings = parsing_settings

        self.report_counter = 0
        self.number_of_selected_reports = 0

        # target file name
        self.target_file_name_prefix = self.parsing_settings['target_file_name_prefix']

        # reports
        self.report_scan_enabled = self.parsing_settings['report_scan_enabled']
        self.report_host_enabled = self.parsing_settings['report_host_enabled']
        self.report_vulnerabilities_enabled = self.parsing_settings['report_vulnerabilities_enabled']
        self.report_noncompliance_enabled = self.parsing_settings['report_noncompliance_enabled']

        # reports settings:
        self.report_scan_debug_data_enabled = self.parsing_settings['report_scan_debug_data_enabled']
        self.report_host_debug_data_enabled = self.parsing_settings['report_host_debug_data_enabled']
        self.report_vulnerabilities_debug_data_enabled = self.parsing_settings[
            'report_vulnerabilities_debug_data_enabled']
        self.report_vulnerabilities_none_filter_out = self.parsing_settings['report_vulnerabilities_none_filter_out']
        self.report_noncompliance_debug_data_enabled = self.parsing_settings[
            'report_noncompliance_debug_data_enabled']

    def run(self):
        files_to_pars = self.files_to_pars
        target_directory = self.target_directory

        target_file_name_prefix = self.target_file_name_prefix

        suffix = self.parsing_settings['suffix']

        target_file_name = target_file_name_prefix + suffix + '.xlsx'
        final_path_to_save = target_directory + '/' + target_file_name
        workbook = xlsxwriter.Workbook(final_path_to_save, {'constant_memory': True})

        if self.report_scan_enabled and not \
                self.report_host_enabled and not \
                self.report_vulnerabilities_enabled and not \
                self.report_noncompliance_enabled:
            self.number_of_selected_reports = 1
            self.create_worksheet_for_scans(workbook, files_to_pars)
        elif not self.report_scan_enabled and \
                self.report_host_enabled and not \
                self.report_vulnerabilities_enabled and not \
                self.report_noncompliance_enabled:
            self.number_of_selected_reports = 1
            self.create_worksheet_for_hosts(workbook, files_to_pars)
        elif not self.report_scan_enabled and not \
                self.report_host_enabled and \
                self.report_vulnerabilities_enabled and not \
                self.report_noncompliance_enabled:
            self.number_of_selected_reports = 1
            self.create_worksheet_for_vulnerabilities(workbook, files_to_pars)
        elif not self.report_scan_enabled and not \
                self.report_host_enabled and not \
                self.report_vulnerabilities_enabled and \
                self.report_noncompliance_enabled:
            self.number_of_selected_reports = 1
            self.create_worksheet_for_noncompliance(workbook, files_to_pars)
        elif self.report_scan_enabled and \
                self.report_host_enabled and not \
                self.report_vulnerabilities_enabled and not \
                self.report_noncompliance_enabled:
            self.number_of_selected_reports = 2
            self.create_worksheet_for_scans(workbook, files_to_pars)
            self.create_worksheet_for_hosts(workbook, files_to_pars)
        elif self.report_scan_enabled and not \
                self.report_host_enabled and \
                self.report_vulnerabilities_enabled and not \
                self.report_noncompliance_enabled:
            self.number_of_selected_reports = 2
            self.create_worksheet_for_scans(workbook, files_to_pars)
            self.create_worksheet_for_vulnerabilities(workbook, files_to_pars)
        elif self.report_scan_enabled and not \
                self.report_host_enabled and not \
                self.report_vulnerabilities_enabled and \
                self.report_noncompliance_enabled:
            self.number_of_selected_reports = 2
            self.create_worksheet_for_scans(workbook, files_to_pars)
            self.create_worksheet_for_noncompliance(workbook, files_to_pars)
        elif not self.report_scan_enabled and \
                self.report_host_enabled and \
                self.report_vulnerabilities_enabled and not \
                self.report_noncompliance_enabled:
            self.number_of_selected_reports = 2
            self.create_worksheet_for_hosts(workbook, files_to_pars)
            self.create_worksheet_for_vulnerabilities(workbook, files_to_pars)
        elif not self.report_scan_enabled and \
                self.report_host_enabled and not \
                self.report_vulnerabilities_enabled and \
                self.report_noncompliance_enabled:
            self.number_of_selected_reports = 2
            self.create_worksheet_for_hosts(workbook, files_to_pars)
            self.create_worksheet_for_noncompliance(workbook, files_to_pars)
        elif not self.report_scan_enabled and not \
                self.report_host_enabled and \
                self.report_vulnerabilities_enabled and \
                self.report_noncompliance_enabled:
            self.number_of_selected_reports = 2
            self.create_worksheet_for_vulnerabilities(workbook, files_to_pars)
            self.create_worksheet_for_noncompliance(workbook, files_to_pars)
        elif self.report_scan_enabled and \
                self.report_host_enabled and \
                self.report_vulnerabilities_enabled and not \
                self.report_noncompliance_enabled:
            self.number_of_selected_reports = 3
            self.create_worksheet_for_scans(workbook, files_to_pars)
            self.create_worksheet_for_hosts(workbook, files_to_pars)
            self.create_worksheet_for_vulnerabilities(workbook, files_to_pars)
        elif self.report_scan_enabled and \
                self.report_host_enabled and not \
                self.report_vulnerabilities_enabled and \
                self.report_noncompliance_enabled:
            self.number_of_selected_reports = 3
            self.create_worksheet_for_scans(workbook, files_to_pars)
            self.create_worksheet_for_hosts(workbook, files_to_pars)
            self.create_worksheet_for_noncompliance(workbook, files_to_pars)
        elif self.report_scan_enabled and not \
                self.report_host_enabled and \
                self.report_vulnerabilities_enabled and \
                self.report_noncompliance_enabled:
            self.number_of_selected_reports = 3
            self.create_worksheet_for_scans(workbook, files_to_pars)
            self.create_worksheet_for_vulnerabilities(workbook, files_to_pars)
            self.create_worksheet_for_noncompliance(workbook, files_to_pars)
        elif not self.report_scan_enabled and \
                self.report_host_enabled and \
                self.report_vulnerabilities_enabled and \
                self.report_noncompliance_enabled:
            self.number_of_selected_reports = 3
            self.create_worksheet_for_hosts(workbook, files_to_pars)
            self.create_worksheet_for_vulnerabilities(workbook, files_to_pars)
            self.create_worksheet_for_noncompliance(workbook, files_to_pars)
        elif self.report_scan_enabled and \
                self.report_host_enabled and \
                self.report_vulnerabilities_enabled and \
                self.report_noncompliance_enabled:
            self.number_of_selected_reports = 4
            self.create_worksheet_for_scans(workbook, files_to_pars)
            self.create_worksheet_for_hosts(workbook, files_to_pars)
            self.create_worksheet_for_vulnerabilities(workbook, files_to_pars)
            self.create_worksheet_for_noncompliance(workbook, files_to_pars)

        else:
            info = 'You did not choose any report type to generate. Select at least one.'
            print(info)

        workbook.close()

    def create_worksheet_for_scans(self, workbook, list_of_source_files):
        """
        Function create spreadsheet with scan sum-up in given workbook for selected files.
        :param workbook: workbook where spreadsheet are created
        :param list_of_source_files: list of selected files
        """
        report_name = 'scans'
        self.report_counter += 1
        info_report = 'Report: ' + str(self.report_counter) + '/' + str(self.number_of_selected_reports)

        worksheet = workbook.add_worksheet(report_name)

        cell_format_bold = workbook.add_format({'bold': True})
        worksheet.set_row(0, None, cell_format_bold)

        # print('>>>>>>>>>>>>>>>> ', self.report_scan_debug_data_enabled)

        if not self.report_scan_debug_data_enabled:
            headers = [
                'Target hosts',
                'Target hosts (without duplicates)',
                'Scanned hosts',
                'Scanned hosts with credentialed checks',
                'Unreachable hosts',
                'Scan started',
                'Scan ended',
                'Elapsed time per scan',
                'Login used',
                'DB SID',
                'DB port',
                'ALL plugins',
                'Critical plugins',
                'High plugins',
                'Medium plugins',
                'Low plugins',
                'None plugins',
                'ALL compliance',
                'Passed compliance',
                'Failed compliance',
                'Warning compliance'
            ]
        else:
            headers = [
                'Nessus scan name',
                'Nessus file name',
                'nessus file size',
                'Target hosts',
                'Target hosts (without duplicates)',
                'Scanned hosts',
                'Scanned hosts with credentialed checks',
                'Unreachable hosts',
                'Scan started',
                'Scan ended',
                'Elapsed time per scan',
                'Policy name',
                'Login used',
                'DB SID',
                'DB port',
                'Reverse lookup',
                'Max hosts',
                'Max checks',
                'Network timeout',
                'Used plugins',
                'ALL plugins',
                'Critical plugins',
                'High plugins',
                'Medium plugins',
                'Low plugins',
                'None plugins',
                'ALL compliance',
                'Passed compliance',
                'Failed compliance',
                'Warning compliance'
            ]

        number_of_columns = len(headers)
        # print('Number of columns: ' + str(number_of_columns))

        worksheet.set_column(0, number_of_columns - 1, 18)

        debug_columns_list = [0, 1, 2, 11, 15, 16, 17, 18, 19]

        for column_index, header in enumerate(headers):
            if self.report_scan_debug_data_enabled and column_index in debug_columns_list:
                cell_format_bold_blue = workbook.add_format()
                cell_format_bold_blue.set_bold()
                cell_format_bold_blue.set_font_color('blue')
                worksheet.write(0, column_index, header, cell_format_bold_blue)
            else:
                worksheet.write(0, column_index, header)

        worksheet.freeze_panes(1, 0)  # Freeze the first row.

        nessus_scan_file_number = 0
        number_of_files_with_errors = 0

        number_of_rows = 0
        for row_index, nessus_scan_file in enumerate(list_of_source_files):
            row_index += 1
            number_of_rows += 1
            nessus_scan_file_number = nessus_scan_file_number + 1

            info_file = ', File: ' + str(row_index) + '/' + str(len(list_of_source_files))

            try:
                root = nfr.file.nessus_scan_file_root_element(nessus_scan_file)

                nessus_scan_file = nfr.file.nessus_scan_file_name_with_path(nessus_scan_file)
                start_time = time.time()
                self.log_emitter('start', nessus_scan_file)
                self.file_conversion_started.emit(1)

                source_file_size = nfa.utilities.size_of_file_human(nessus_scan_file)
                self.log_emitter('info ', nessus_scan_file, '[source_file_size={0}]'.format(source_file_size))
                self.log_emitter('info ', nessus_scan_file, '[report_type={0}]'.format(report_name))
                self.log_emitter('info ', nessus_scan_file,
                                 '[number_of_target_hosts={0}]'.format(nfr.scan.number_of_target_hosts(root)))
                self.log_emitter('info ', nessus_scan_file,
                                 '[number_of_scanned_hosts={0}]'.format(nfr.scan.number_of_scanned_hosts(root)))
                self.log_emitter('info ', nessus_scan_file, '[number_of_scanned_hosts_with_credentials={0}]'.format(
                    nfr.scan.number_of_scanned_hosts_with_credentialed_checks_yes(root)))

                date_format = workbook.add_format({'num_format': 'yyyy-mm-dd hh:mm:ss'})

                login_used = None
                number_of_plugins = 0
                number_of_plugins_critical = 0
                number_of_plugins_high = 0
                number_of_plugins_medium = 0
                number_of_plugins_low = 0
                number_of_plugins_none = 0
                number_of_compliance_plugins = 0
                number_of_compliance_plugins_passed = 0
                number_of_compliance_plugins_failed = 0
                number_of_compliance_plugins_warning = 0

                policy_max_hosts = int(nfr.scan.policy_max_hosts(root))
                policy_max_checks = int(nfr.scan.policy_max_checks(root))
                policy_checks_read_timeout = int(nfr.scan.policy_checks_read_timeout(root))

                report_host_counter = 0
                number_of_report_hosts = nfr.scan.number_of_scanned_hosts(root)

                info_host = ', Host: ' + str(report_host_counter) + '/' + str(number_of_report_hosts)
                info_final = info_report + info_file + info_host
                self.print_status_bar_info.emit(info_final)

                for report_host in nfr.scan.report_hosts(root):
                    report_host_counter += 1
                    self.progress.emit(report_host_counter, number_of_report_hosts)

                    info_host = ', Host: ' + str(report_host_counter) + '/' + str(number_of_report_hosts)
                    info_final = info_report + info_file + info_host
                    self.print_status_bar_info.emit(info_final)

                    login_used = nfr.host.login_used(report_host)

                    number_of_plugins += nfr.host.number_of_plugins(report_host)
                    number_of_plugins_critical += nfr.host.number_of_plugins_per_risk_factor(report_host, 'Critical')
                    number_of_plugins_high += nfr.host.number_of_plugins_per_risk_factor(report_host, 'High')
                    number_of_plugins_medium += nfr.host.number_of_plugins_per_risk_factor(report_host, 'Medium')
                    number_of_plugins_low += nfr.host.number_of_plugins_per_risk_factor(report_host, 'Low')
                    number_of_plugins_none += nfr.host.number_of_plugins_per_risk_factor(report_host, 'None')
                    number_of_compliance_plugins += nfr.host.number_of_compliance_plugins(report_host)
                    number_of_compliance_plugins_passed += \
                        nfr.host.number_of_compliance_plugins_per_result(report_host, 'PASSED')
                    number_of_compliance_plugins_failed += \
                        nfr.host.number_of_compliance_plugins_per_result(report_host, 'FAILED')
                    number_of_compliance_plugins_warning += nfr.host.number_of_compliance_plugins_per_result(
                        report_host, 'WARNING')

                if not self.report_scan_debug_data_enabled:
                    worksheet.write(row_index, 0, nfr.scan.number_of_target_hosts(root))
                    worksheet.write(row_index, 1, nfr.scan.number_of_target_hosts_without_duplicates(root))
                    worksheet.write(row_index, 2, nfr.scan.number_of_scanned_hosts(root))
                    worksheet.write(row_index, 3, nfr.scan.number_of_scanned_hosts_with_credentialed_checks_yes(root))
                    worksheet.write(row_index, 4, nfr.scan.number_of_not_scanned_hosts(root))

                    scan_start_time = nfr.scan.scan_time_start(root)
                    if scan_start_time is not None:
                        worksheet.write_datetime(row_index, 5, scan_start_time, date_format)
                    else:
                        worksheet.write_blank(row_index, 5, None)

                    scan_end_time = nfr.scan.scan_time_end(root)
                    if scan_end_time is not None:
                        worksheet.write_datetime(row_index, 6, scan_end_time, date_format)
                    else:
                        worksheet.write_blank(row_index, 6, None)

                    worksheet.write(row_index, 7, nfr.scan.scan_time_elapsed(root))
                    worksheet.write(row_index, 8, login_used)
                    worksheet.write(row_index, 9, nfr.scan.policy_db_sid(root))
                    worksheet.write(row_index, 10, nfr.scan.policy_db_port(root))
                    worksheet.write(row_index, 11, number_of_plugins)
                    worksheet.write(row_index, 12, number_of_plugins_critical)
                    worksheet.write(row_index, 13, number_of_plugins_high)
                    worksheet.write(row_index, 14, number_of_plugins_medium)
                    worksheet.write(row_index, 15, number_of_plugins_low)
                    worksheet.write(row_index, 16, number_of_plugins_none)
                    worksheet.write(row_index, 17, number_of_compliance_plugins)
                    worksheet.write(row_index, 18, number_of_compliance_plugins_passed)
                    worksheet.write(row_index, 19, number_of_compliance_plugins_failed)
                    worksheet.write(row_index, 20, number_of_compliance_plugins_warning)
                else:
                    worksheet.write(row_index, 0, nfr.scan.report_name(root))
                    worksheet.write(row_index, 1, nfr.file.nessus_scan_file_name_with_path(nessus_scan_file))
                    worksheet.write(row_index, 2, nfr.file.nessus_scan_file_size_human(nessus_scan_file))
                    worksheet.write(row_index, 3, nfr.scan.number_of_target_hosts(root))
                    worksheet.write(row_index, 4, nfr.scan.number_of_target_hosts_without_duplicates(root))
                    worksheet.write(row_index, 5, nfr.scan.number_of_scanned_hosts(root))
                    worksheet.write(row_index, 6, nfr.scan.number_of_scanned_hosts_with_credentialed_checks_yes(root))
                    worksheet.write(row_index, 7, nfr.scan.number_of_not_scanned_hosts(root))

                    scan_start_time = nfr.scan.scan_time_start(root)
                    if scan_start_time is not None:
                        worksheet.write_datetime(row_index, 8, scan_start_time, date_format)
                    else:
                        worksheet.write_blank(row_index, 8, None)

                    scan_end_time = nfr.scan.scan_time_end(root)
                    if scan_end_time is not None:
                        worksheet.write_datetime(row_index, 9, scan_end_time, date_format)
                    else:
                        worksheet.write_blank(row_index, 9, None)

                    worksheet.write(row_index, 10, nfr.scan.scan_time_elapsed(root))
                    worksheet.write(row_index, 11, nfr.scan.policy_name(root))
                    worksheet.write(row_index, 12, login_used)
                    worksheet.write(row_index, 13, nfr.scan.policy_db_sid(root))
                    worksheet.write(row_index, 14, nfr.scan.policy_db_port(root))
                    worksheet.write(row_index, 15, nfr.scan.reverse_lookup(root))
                    worksheet.write(row_index, 16, policy_max_hosts)
                    worksheet.write(row_index, 17, policy_max_checks)
                    worksheet.write(row_index, 18, policy_checks_read_timeout)
                    worksheet.write(row_index, 19, len(nfr.scan.plugin_set(root)))
                    worksheet.write(row_index, 20, number_of_plugins)
                    worksheet.write(row_index, 21, number_of_plugins_critical)
                    worksheet.write(row_index, 22, number_of_plugins_high)
                    worksheet.write(row_index, 23, number_of_plugins_medium)
                    worksheet.write(row_index, 24, number_of_plugins_low)
                    worksheet.write(row_index, 25, number_of_plugins_none)
                    worksheet.write(row_index, 26, number_of_compliance_plugins)
                    worksheet.write(row_index, 27, number_of_compliance_plugins_passed)
                    worksheet.write(row_index, 28, number_of_compliance_plugins_failed)
                    worksheet.write(row_index, 29, number_of_compliance_plugins_warning)

                end_time = time.time()
                elapsed_time = end_time - start_time
                elapsed_time_parsed = time.strftime('%H:%M:%S', time.gmtime(elapsed_time))

                self.log_emitter('info ', nessus_scan_file, '[elapsed_time={0}]'.format(elapsed_time_parsed))
                self.log_emitter('end  ', nessus_scan_file)

            except Exception as e:
                number_of_files_with_errors += 1
                traceback.print_exc()
                self.log_emitter('info',
                                 "ERROR Parsing [" + str(nessus_scan_file_number) + "/" +
                                 str(len(list_of_source_files)) + "] nessus files")
                self.log_emitter('info', e)

        if number_of_rows > 0:
            worksheet.autofilter(0, 0, number_of_rows, number_of_columns - 1)

    def create_worksheet_for_hosts(self, workbook, list_of_source_files):
        """
        Function create spreadsheet with host sum-up in given workbook for selected files.
        :param workbook: workbook where spreadsheet are created
        :param list_of_source_files: list of selected files
        """
        report_name = 'hosts'
        self.report_counter += 1
        info_report = 'Report: ' + str(self.report_counter) + '/' + str(self.number_of_selected_reports)

        worksheet = workbook.add_worksheet(report_name)

        cell_format_bold = workbook.add_format({'bold': True})
        worksheet.set_row(0, None, cell_format_bold)

        # print('>>>>>>>>>>>>>>>> ', self.report_host_debug_data_enabled)

        if not self.report_host_debug_data_enabled:
            headers = [
                # 'Nessus scanner IP',
                # 'Nessus scan name',
                # 'Nessus file name',
                'Target',
                'Hostname',
                'FQDN',
                'IP',
                'Scanned',
                'Credentialed checks',
                'Scan started',
                'Scan ended',
                'Elapsed time per host',
                'Elapsed time per scan',
                # 'Policy name',
                'Login used',
                'DB SID',
                'DB port',
                # 'Max hosts',
                # 'Max checks',
                # 'Network timeout',
                'Operating System',
                'ALL plugins',
                'Critical plugins',
                'High plugins',
                'Medium plugins',
                'Low plugins',
                'None plugins',
                'ALL compliance',
                'Passed compliance',
                'Failed compliance',
                'Warning compliance'
                # '10180: Ping to remote host',
                # '10287: Traceroute Information',
                # '11936: OS Identification',
                # '45590: Common Platform Enumeration (CPE)',
                # '54615: Device Type',
                # '21745: Authentication Failure - Local Checks Not Run',
                # '12634: Authenticated Check : OS Name and Installed Package Enumeration',
                # '110385: Authentication Success Insufficient Access',
                # '102094: SSH Commands Require Privilege Escalation',
                # '10394: Microsoft Windows SMB Log In Possible',
                # '24786: Nessus Windows Scan Not Performed with Admin Privileges',
                # '24269: Windows Management Instrumentation (WMI) Available',
                # '11011: Microsoft Windows SMB Service Detection',
                # '10400: Microsoft Windows SMB Registry Remotely Accessible',
                # '26917: Microsoft Windows SMB Registry : Nessus Cannot Access the Windows Registry',
                # '42897: SMB Registry : Start the Registry Service during the scan (WMI)',
                # '20811: Microsoft Windows Installed Software Enumeration (credentialed check)',
                # '91825: Oracle DB Login Possible',
                # '91827: Microsoft SQL Server Login Possible',
                # '47864: Cisco IOS Version',
                # '67217: Cisco IOS XE Version'
            ]
        else:
            headers = [
                'Nessus scanner IP',
                'Nessus scan name',
                'Nessus file name',
                'Target',
                'Hostname',
                'FQDN',
                'IP',
                'Scanned',
                'Credentialed checks',
                'Scan started',
                'Scan ended',
                'Elapsed time per host',
                'Elapsed time per scan',
                'Policy name',
                'Login used',
                'DB SID',
                'DB port',
                'Reverse lookup',
                'Max hosts',
                'Max checks',
                'Network timeout',
                'Operating System',
                'ALL plugins',
                'Critical plugins',
                'High plugins',
                'Medium plugins',
                'Low plugins',
                'None plugins',
                'ALL compliance',
                'Passed compliance',
                'Failed compliance',
                'Warning compliance',
                '10180: Ping to remote host',
                '10287: Traceroute Information',
                '11936: OS Identification',
                '45590: Common Platform Enumeration (CPE)',
                '54615: Device Type',
                '21745: Authentication Failure - Local Checks Not Run',
                '12634: Authenticated Check : OS Name and Installed Package Enumeration',
                '110385: Authentication Success Insufficient Access',
                '102094: SSH Commands Require Privilege Escalation',
                '10394: Microsoft Windows SMB Log In Possible',
                '24786: Nessus Windows Scan Not Performed with Admin Privileges',
                '24269: Windows Management Instrumentation (WMI) Available',
                '11011: Microsoft Windows SMB Service Detection',
                '10400: Microsoft Windows SMB Registry Remotely Accessible',
                '26917: Microsoft Windows SMB Registry : Nessus Cannot Access the Windows Registry',
                '42897: SMB Registry : Start the Registry Service during the scan (WMI)',
                '20811: Microsoft Windows Installed Software Enumeration (credentialed check)',
                '91825: Oracle DB Login Possible',
                '91827: Microsoft SQL Server Login Possible',
                '47864: Cisco IOS Version',
                '67217: Cisco IOS XE Version'
            ]
        number_of_columns = len(headers)
        # print('Number of columns: ' + str(number_of_columns))

        worksheet.set_column(0, number_of_columns - 1, 18)

        debug_columns_list = [0, 1, 2, 13, 17, 18, 19, 20, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46,
                              47, 48, 49, 50, 51, 52]

        for column_index, header in enumerate(headers):
            if self.report_host_debug_data_enabled and column_index in debug_columns_list:
                cell_format_bold_blue = workbook.add_format()
                cell_format_bold_blue.set_bold()
                cell_format_bold_blue.set_font_color('blue')
                worksheet.write(0, column_index, header, cell_format_bold_blue)
            else:
                worksheet.write(0, column_index, header)

        worksheet.freeze_panes(1, 0)  # Freeze the first row.

        nessus_scan_file_number = 0
        number_of_files_with_errors = 0

        number_of_rows = 0
        row_index = 0
        row_index_per_file = 0
        for nessus_scan_file in list_of_source_files:
            row_index_per_file += 1
            nessus_scan_file_number = nessus_scan_file_number + 1
            info_file = ', File: ' + str(row_index_per_file) + '/' + str(len(list_of_source_files))

            try:
                root = nfr.file.nessus_scan_file_root_element(nessus_scan_file)

                nessus_scan_file = nfr.file.nessus_scan_file_name_with_path(nessus_scan_file)
                start_time = time.time()
                self.log_emitter('start', nessus_scan_file)
                self.file_conversion_started.emit(1)

                source_file_size = nfa.utilities.size_of_file_human(nessus_scan_file)
                self.log_emitter('info ', nessus_scan_file, '[source_file_size={0}]'.format(source_file_size))
                self.log_emitter('info ', nessus_scan_file, '[report_type={0}]'.format(report_name))
                self.log_emitter('info ', nessus_scan_file,
                                 '[number_of_target_hosts={0}]'.format(nfr.scan.number_of_target_hosts(root)))
                self.log_emitter('info ', nessus_scan_file,
                                 '[number_of_scanned_hosts={0}]'.format(nfr.scan.number_of_scanned_hosts(root)))
                self.log_emitter('info ', nessus_scan_file, '[number_of_scanned_hosts_with_credentials={0}]'.format(
                    nfr.scan.number_of_scanned_hosts_with_credentialed_checks_yes(root)))

                date_format = workbook.add_format({'num_format': 'yyyy-mm-dd hh:mm:ss'})
                policy_max_hosts = int(nfr.scan.policy_max_hosts(root))
                policy_max_checks = int(nfr.scan.policy_max_checks(root))
                policy_checks_read_timeout = int(nfr.scan.policy_checks_read_timeout(root))
                scan_report_name = nfr.scan.report_name(root)
                nessus_scan_file_name_with_path = nfr.file.nessus_scan_file_name_with_path(nessus_scan_file)
                scan_time_elapsed = nfr.scan.scan_time_elapsed(root)
                scan_policy_name = nfr.scan.policy_name(root)
                scan_policy_db_sid = nfr.scan.policy_db_sid(root)
                scan_policy_db_port = nfr.scan.policy_db_port(root)
                scan_reverse_lookup = nfr.scan.reverse_lookup(root)
                scan_policy_login_specified = nfr.scan.policy_login_specified(root)

                report_host_counter = 0
                number_of_report_hosts = nfr.scan.number_of_scanned_hosts(root)

                info_host = ', Host: ' + str(report_host_counter) + '/' + str(number_of_report_hosts)
                info_final = info_report + info_file + info_host
                self.print_status_bar_info.emit(info_final)

                for report_host in nfr.scan.report_hosts(root):
                    row_index += 1
                    number_of_rows += 1

                    report_host_counter += 1
                    self.progress.emit(report_host_counter, number_of_report_hosts)

                    info_host = ', Host: ' + str(report_host_counter) + '/' + str(number_of_report_hosts)
                    info_final = info_report + info_file + info_host
                    self.print_status_bar_info.emit(info_final)

                    login_used = nfr.host.login_used(report_host)
                    if login_used is None:
                        login_used = scan_policy_login_specified

                    number_of_plugins = nfr.host.number_of_plugins(report_host)
                    number_of_plugins_critical = nfr.host.number_of_plugins_per_risk_factor(report_host, 'Critical')
                    number_of_plugins_high = nfr.host.number_of_plugins_per_risk_factor(report_host, 'High')
                    number_of_plugins_medium = nfr.host.number_of_plugins_per_risk_factor(report_host, 'Medium')
                    number_of_plugins_low = nfr.host.number_of_plugins_per_risk_factor(report_host, 'Low')
                    number_of_plugins_none = nfr.host.number_of_plugins_per_risk_factor(report_host, 'None')
                    number_of_compliance_plugins = nfr.host.number_of_compliance_plugins(report_host)
                    number_of_compliance_plugins_passed = \
                        nfr.host.number_of_compliance_plugins_per_result(report_host, 'PASSED')
                    number_of_compliance_plugins_failed = \
                        nfr.host.number_of_compliance_plugins_per_result(report_host, 'FAILED')
                    number_of_compliance_plugins_warning = \
                        nfr.host.number_of_compliance_plugins_per_result(report_host, 'WARNING')
                    if not self.report_host_debug_data_enabled:
                        worksheet.write(row_index, 0, nfr.host.report_host_name(report_host))
                        worksheet.write(row_index, 1, nfr.host.resolved_hostname(report_host))
                        worksheet.write(row_index, 2, nfr.host.resolved_fqdn(report_host))
                        worksheet.write(row_index, 3, nfr.host.resolved_ip(report_host))
                        worksheet.write(row_index, 4, 'yes')
                        worksheet.write(row_index, 5, nfr.host.credentialed_checks(root, report_host))

                        host_start_time = nfr.host.host_time_start(report_host)
                        if host_start_time is not None:
                            worksheet.write_datetime(row_index, 6, host_start_time, date_format)
                        else:
                            worksheet.write_blank(row_index, 6, None)

                        host_end_time = nfr.host.host_time_end(report_host)
                        if host_end_time is not None:
                            worksheet.write_datetime(row_index, 7, host_end_time, date_format)
                        else:
                            worksheet.write_blank(row_index, 7, None)

                        worksheet.write(row_index, 8, nfr.host.host_time_elapsed(report_host))
                        worksheet.write(row_index, 9, scan_time_elapsed)
                        worksheet.write(row_index, 10, login_used)
                        worksheet.write(row_index, 11, scan_policy_db_sid)
                        worksheet.write(row_index, 12, scan_policy_db_port)
                        worksheet.write(row_index, 13, nfr.host.detected_os(report_host))
                        worksheet.write(row_index, 14, number_of_plugins)
                        worksheet.write(row_index, 15, number_of_plugins_critical)
                        worksheet.write(row_index, 16, number_of_plugins_high)
                        worksheet.write(row_index, 17, number_of_plugins_medium)
                        worksheet.write(row_index, 18, number_of_plugins_low)
                        worksheet.write(row_index, 19, number_of_plugins_none)
                        worksheet.write(row_index, 20, number_of_compliance_plugins)
                        worksheet.write(row_index, 21, number_of_compliance_plugins_passed)
                        worksheet.write(row_index, 22, number_of_compliance_plugins_failed)
                        worksheet.write(row_index, 23, number_of_compliance_plugins_warning)

                    else:
                        worksheet.write(row_index, 0, nfr.host.scanner_ip(root, report_host))
                        worksheet.write(row_index, 1, scan_report_name)
                        worksheet.write(row_index, 2, nessus_scan_file_name_with_path)
                        worksheet.write(row_index, 3, nfr.host.report_host_name(report_host))
                        worksheet.write(row_index, 4, nfr.host.resolved_hostname(report_host))
                        worksheet.write(row_index, 5, nfr.host.resolved_fqdn(report_host))
                        worksheet.write(row_index, 6, nfr.host.resolved_ip(report_host))
                        worksheet.write(row_index, 7, 'yes')
                        worksheet.write(row_index, 8, nfr.host.credentialed_checks(root, report_host))

                        host_start_time = nfr.host.host_time_start(report_host)
                        if host_start_time is not None:
                            worksheet.write_datetime(row_index, 9, host_start_time, date_format)
                        else:
                            worksheet.write_blank(row_index, 9, None)

                        host_end_time = nfr.host.host_time_end(report_host)
                        if host_end_time is not None:
                            worksheet.write_datetime(row_index, 10, host_end_time, date_format)
                        else:
                            worksheet.write_blank(row_index, 10, None)

                        worksheet.write(row_index, 11, nfr.host.host_time_elapsed(report_host))
                        worksheet.write(row_index, 12, scan_time_elapsed)
                        worksheet.write(row_index, 13, scan_policy_name)
                        worksheet.write(row_index, 14, login_used)
                        worksheet.write(row_index, 15, scan_policy_db_sid)
                        worksheet.write(row_index, 16, scan_policy_db_port)
                        worksheet.write(row_index, 17, scan_reverse_lookup)
                        worksheet.write(row_index, 18, policy_max_hosts)
                        worksheet.write(row_index, 19, policy_max_checks)
                        worksheet.write(row_index, 20, policy_checks_read_timeout)
                        worksheet.write(row_index, 21, nfr.host.detected_os(report_host))
                        worksheet.write(row_index, 22, number_of_plugins)
                        worksheet.write(row_index, 23, number_of_plugins_critical)
                        worksheet.write(row_index, 24, number_of_plugins_high)
                        worksheet.write(row_index, 25, number_of_plugins_medium)
                        worksheet.write(row_index, 26, number_of_plugins_low)
                        worksheet.write(row_index, 27, number_of_plugins_none)
                        worksheet.write(row_index, 28, number_of_compliance_plugins)
                        worksheet.write(row_index, 29, number_of_compliance_plugins_passed)
                        worksheet.write(row_index, 30, number_of_compliance_plugins_failed)
                        worksheet.write(row_index, 31, number_of_compliance_plugins_warning)
                        # '10180: Ping to remote host'
                        worksheet.write(row_index, 32, nfr.plugin.plugin_output(root, report_host, '10180'))
                        # '10287: Traceroute Information'
                        worksheet.write(row_index, 33, nfr.plugin.plugin_output(root, report_host, '10287'))
                        # '11936: OS Identification'
                        worksheet.write(row_index, 34, nfr.plugin.plugin_output(root, report_host, '11936'))
                        # '45590: Common Platform Enumeration (CPE)'
                        worksheet.write(row_index, 35, nfr.plugin.plugin_output(root, report_host, '45590'))
                        # '54615: Device Type'
                        worksheet.write(row_index, 36, nfr.plugin.plugin_output(root, report_host, '54615'))
                        # '21745: Authentication Failure - Local Checks Not Run'
                        worksheet.write(row_index, 37, nfr.plugin.plugin_output(root, report_host, '21745'))
                        # '12634: Authenticated Check : OS Name and Installed Package Enumeration'
                        worksheet.write(row_index, 38, nfr.plugin.plugin_output(root, report_host, '12634'))
                        # '110385: Authentication Success Insufficient Access'
                        worksheet.write(row_index, 39, nfr.plugin.plugin_output(root, report_host, '110385'))
                        # '102094: SSH Commands Require Privilege Escalation'
                        worksheet.write(row_index, 40, nfr.plugin.plugin_output(root, report_host, '102094'))
                        # '10394: Microsoft Windows SMB Log In Possible'
                        worksheet.write(row_index, 41, nfr.plugin.plugin_output(root, report_host, '10394'))
                        # '24786: Nessus Windows Scan Not Performed with Admin Privileges'
                        worksheet.write(row_index, 42, nfr.plugin.plugin_output(root, report_host, '24786'))
                        # '24269: Windows Management Instrumentation (WMI) Available'
                        worksheet.write(row_index, 43, nfr.plugin.plugin_output(root, report_host, '24269'))
                        # '11011: Microsoft Windows SMB Service Detection'
                        worksheet.write(row_index, 44, nfr.plugin.plugin_outputs(root, report_host, '11011'))
                        # '10400: Microsoft Windows SMB Registry Remotely Accessible'
                        worksheet.write(row_index, 45, nfr.plugin.plugin_output(root, report_host, '10400'))
                        # '26917: Microsoft Windows SMB Registry : Nessus Cannot Access the Windows Registry'
                        worksheet.write(row_index, 46, nfr.plugin.plugin_output(root, report_host, '26917'))
                        # '42897: SMB Registry : Start the Registry Service during the scan (WMI)'
                        worksheet.write(row_index, 47, nfr.plugin.plugin_output(root, report_host, '42897'))
                        # '20811: Microsoft Windows Installed Software Enumeration (credentialed check)'
                        worksheet.write(row_index, 48, nfr.plugin.plugin_output(root, report_host, '20811'))
                        # '91825: Oracle DB Login Possible'
                        worksheet.write(row_index, 49, nfr.plugin.plugin_output(root, report_host, '91825'))
                        # '91827: Microsoft SQL Server Login Possible'
                        worksheet.write(row_index, 50, nfr.plugin.plugin_output(root, report_host, '91827'))
                        # '47864: Cisco IOS Version'
                        worksheet.write(row_index, 51, nfr.plugin.plugin_output(root, report_host, '47864'))
                        # '67217: Cisco IOS XE Version'
                        worksheet.write(row_index, 52, nfr.plugin.plugin_output(root, report_host, '67217'))

                number_of_not_scanned_hosts = nfr.scan.number_of_not_scanned_hosts(root)
                if number_of_not_scanned_hosts > 0:
                    not_scanned_hosts = nfr.scan.list_of_not_scanned_hosts(root)
                    not_scanned_host_counter = 0

                    file_source = nfr.scan.source_of_file(root)
                    if file_source == 'Tenable.sc':
                        targets_sc = nfr.scan.list_of_target_hosts_sc_fqdn_ip(root)

                        for target in not_scanned_hosts:
                            row_index += 1
                            not_scanned_host_counter += 1
                            self.progress.emit(not_scanned_host_counter, number_of_not_scanned_hosts)

                            target_fqdn = ''
                            target_hostname = ''
                            target_ip = ''
                            for target_sc in targets_sc:
                                if target == target_sc['target_fqdn']:
                                    target_fqdn = target_sc['target_fqdn']
                                    target_hostname = target_fqdn.split('.')[0]
                                    target_ip = target_sc['target_ip']

                            if not self.report_host_debug_data_enabled:
                                worksheet.write(row_index, 0, target)
                                worksheet.write(row_index, 1, target_hostname)
                                worksheet.write(row_index, 2, target_fqdn)
                                worksheet.write(row_index, 3, target_ip)
                                worksheet.write(row_index, 4, 'no')
                                worksheet.write(row_index, 5, 'no')
                                worksheet.write_blank(row_index, 6, None)
                                worksheet.write_blank(row_index, 7, None)
                                worksheet.write(row_index, 8, '0:00:00')
                                worksheet.write(row_index, 9, scan_time_elapsed)
                                worksheet.write(row_index, 10, scan_policy_login_specified)
                                worksheet.write(row_index, 11, scan_policy_db_sid)
                                worksheet.write(row_index, 12, scan_policy_db_port)
                                worksheet.write_blank(row_index, 13, None)
                                worksheet.write_blank(row_index, 14, None)
                                worksheet.write_blank(row_index, 15, None)
                                worksheet.write_blank(row_index, 16, None)
                                worksheet.write_blank(row_index, 17, None)
                                worksheet.write_blank(row_index, 18, None)
                                worksheet.write_blank(row_index, 19, None)
                                worksheet.write_blank(row_index, 20, None)
                                worksheet.write_blank(row_index, 21, None)
                                worksheet.write_blank(row_index, 22, None)
                            else:
                                # worksheet.write_blank(row_index, 0, None)
                                worksheet.write(row_index, 1, scan_report_name)
                                worksheet.write(row_index, 2, nessus_scan_file_name_with_path)
                                worksheet.write(row_index, 3, target)
                                worksheet.write(row_index, 4, target_hostname)
                                worksheet.write(row_index, 5, target_fqdn)
                                worksheet.write(row_index, 6, target_ip)
                                worksheet.write(row_index, 7, 'no')
                                worksheet.write(row_index, 8, 'no')
                                # worksheet.write_blank(row_index, 9, None)
                                # worksheet.write_blank(row_index, 10, None)
                                worksheet.write(row_index, 11, '0:00:00')
                                worksheet.write(row_index, 12, scan_time_elapsed)
                                worksheet.write(row_index, 13, scan_policy_name)
                                worksheet.write(row_index, 14, scan_policy_login_specified)
                                worksheet.write(row_index, 15, scan_policy_db_sid)
                                worksheet.write(row_index, 16, scan_policy_db_port)
                                worksheet.write(row_index, 17, scan_reverse_lookup)
                                worksheet.write(row_index, 18, policy_max_hosts)
                                worksheet.write(row_index, 19, policy_max_checks)
                                # worksheet.write_blank(row_index, 20, None)
                                # worksheet.write_blank(row_index, 21, None)
                                # worksheet.write_blank(row_index, 22, None)
                                # worksheet.write_blank(row_index, 23, None)
                                # worksheet.write_blank(row_index, 24, None)
                                # worksheet.write_blank(row_index, 25, None)
                                # worksheet.write_blank(row_index, 26, None)
                                # worksheet.write_blank(row_index, 27, None)
                                # worksheet.write_blank(row_index, 28, None)
                                # worksheet.write_blank(row_index, 29, None)
                                # worksheet.write_blank(row_index, 30, None)
                                # # '10180: Ping to remote host'
                                # worksheet.write_blank(row_index, 31, None)
                                # # '10287: Traceroute Information'
                                # worksheet.write_blank(row_index, 32, None)
                                # # '11936: OS Identification'
                                # worksheet.write_blank(row_index, 33, None)
                                # # '45590: Common Platform Enumeration (CPE)'
                                # worksheet.write_blank(row_index, 34, None)
                                # # '54615: Device Type'
                                # worksheet.write_blank(row_index, 35, None)
                                # # '21745: Authentication Failure - Local Checks Not Run'
                                # worksheet.write_blank(row_index, 36, None)
                                # # '12634: Authenticated Check : OS Name and Installed Package Enumeration'
                                # worksheet.write_blank(row_index, 37, None)
                                # # '110385: Authentication Success Insufficient Access'
                                # worksheet.write_blank(row_index, 38, None)
                                # # '102094: SSH Commands Require Privilege Escalation'
                                # worksheet.write_blank(row_index, 39, None)
                                # # '10394: Microsoft Windows SMB Log In Possible'
                                # worksheet.write_blank(row_index, 40, None)
                                # # '24786: Nessus Windows Scan Not Performed with Admin Privileges'
                                # worksheet.write_blank(row_index, 41, None)
                                # # '24269: Windows Management Instrumentation (WMI) Available'
                                # worksheet.write_blank(row_index, 42, None)
                                # # '11011: Microsoft Windows SMB Service Detection'
                                # worksheet.write_blank(row_index, 43, None)
                                # # '10400: Microsoft Windows SMB Registry Remotely Accessible'
                                # worksheet.write_blank(row_index, 44, None)
                                # # '26917: Microsoft Windows SMB Registry : Nessus Cannot Access the Windows Registry'
                                # worksheet.write_blank(row_index, 45, None)
                                # # '42897: SMB Registry : Start the Registry Service during the scan (WMI)'
                                # worksheet.write_blank(row_index, 46, None)
                                # # '20811: Microsoft Windows Installed Software Enumeration (credentialed check)'
                                # worksheet.write_blank(row_index, 47, None)
                                # # '91825: Oracle DB Login Possible'
                                # worksheet.write_blank(row_index, 48, None)
                                # # '91827: Microsoft SQL Server Login Possible'
                                # worksheet.write_blank(row_index, 49, None)
                                # # '47864: Cisco IOS Version'
                                # worksheet.write_blank(row_index, 50, None)
                                # # '67217: Cisco IOS XE Version'
                                # worksheet.write_blank(row_index, 51, None)

                    else:
                        for target in not_scanned_hosts:
                            row_index += 1
                            not_scanned_host_counter += 1
                            self.progress.emit(not_scanned_host_counter, number_of_not_scanned_hosts)

                            if not self.report_host_debug_data_enabled:
                                worksheet.write(row_index, 0, target)
                                worksheet.write_blank(row_index, 1, None)
                                worksheet.write_blank(row_index, 2, None)
                                worksheet.write_blank(row_index, 3, None)
                                worksheet.write(row_index, 4, 'no')
                                worksheet.write(row_index, 5, 'no')
                                worksheet.write_blank(row_index, 6, None)
                                worksheet.write_blank(row_index, 7, None)
                                worksheet.write(row_index, 8, '0:00:00')
                                worksheet.write(row_index, 9, scan_time_elapsed)
                                worksheet.write(row_index, 10, scan_policy_login_specified)
                                worksheet.write(row_index, 11, scan_policy_db_sid)
                                worksheet.write(row_index, 12, scan_policy_db_port)
                                worksheet.write_blank(row_index, 13, None)
                                worksheet.write_blank(row_index, 14, None)
                                worksheet.write_blank(row_index, 15, None)
                                worksheet.write_blank(row_index, 16, None)
                                worksheet.write_blank(row_index, 17, None)
                                worksheet.write_blank(row_index, 18, None)
                                worksheet.write_blank(row_index, 19, None)
                                worksheet.write_blank(row_index, 20, None)
                                worksheet.write_blank(row_index, 21, None)
                                worksheet.write_blank(row_index, 22, None)
                            else:
                                # worksheet.write_blank(row_index, 0, None)
                                worksheet.write(row_index, 1, scan_report_name)
                                worksheet.write(row_index, 2, nessus_scan_file_name_with_path)
                                worksheet.write(row_index, 3, target)
                                # worksheet.write_blank(row_index, 4, None)
                                # worksheet.write_blank(row_index, 5, None)
                                # worksheet.write_blank(row_index, 6, None)
                                worksheet.write(row_index, 7, 'no')
                                worksheet.write(row_index, 8, 'no')
                                # worksheet.write_blank(row_index, 9, None)
                                # worksheet.write_blank(row_index, 10, None)
                                worksheet.write(row_index, 11, '0:00:00')
                                worksheet.write(row_index, 12, scan_time_elapsed)
                                worksheet.write(row_index, 13, scan_policy_name)
                                worksheet.write(row_index, 14, scan_policy_login_specified)
                                worksheet.write(row_index, 15, scan_policy_db_sid)
                                worksheet.write(row_index, 16, scan_policy_db_port)
                                worksheet.write(row_index, 17, scan_reverse_lookup)
                                worksheet.write(row_index, 18, policy_max_hosts)
                                worksheet.write(row_index, 19, policy_max_checks)
                                # worksheet.write_blank(row_index, 20, None)
                                # worksheet.write_blank(row_index, 21, None)
                                # worksheet.write_blank(row_index, 22, None)
                                # worksheet.write_blank(row_index, 23, None)
                                # worksheet.write_blank(row_index, 24, None)
                                # worksheet.write_blank(row_index, 25, None)
                                # worksheet.write_blank(row_index, 26, None)
                                # worksheet.write_blank(row_index, 27, None)
                                # worksheet.write_blank(row_index, 28, None)
                                # worksheet.write_blank(row_index, 29, None)
                                # worksheet.write_blank(row_index, 30, None)
                                # # '10180: Ping to remote host'
                                # worksheet.write_blank(row_index, 31, None)
                                # # '10287: Traceroute Information'
                                # worksheet.write_blank(row_index, 32, None)
                                # # '11936: OS Identification'
                                # worksheet.write_blank(row_index, 33, None)
                                # # '45590: Common Platform Enumeration (CPE)'
                                # worksheet.write_blank(row_index, 34, None)
                                # # '54615: Device Type'
                                # worksheet.write_blank(row_index, 35, None)
                                # # '21745: Authentication Failure - Local Checks Not Run'
                                # worksheet.write_blank(row_index, 36, None)
                                # # '12634: Authenticated Check : OS Name and Installed Package Enumeration'
                                # worksheet.write_blank(row_index, 37, None)
                                # # '110385: Authentication Success Insufficient Access'
                                # worksheet.write_blank(row_index, 38, None)
                                # # '102094: SSH Commands Require Privilege Escalation'
                                # worksheet.write_blank(row_index, 39, None)
                                # # '10394: Microsoft Windows SMB Log In Possible'
                                # worksheet.write_blank(row_index, 40, None)
                                # # '24786: Nessus Windows Scan Not Performed with Admin Privileges'
                                # worksheet.write_blank(row_index, 41, None)
                                # # '24269: Windows Management Instrumentation (WMI) Available'
                                # worksheet.write_blank(row_index, 42, None)
                                # # '11011: Microsoft Windows SMB Service Detection'
                                # worksheet.write_blank(row_index, 43, None)
                                # # '10400: Microsoft Windows SMB Registry Remotely Accessible'
                                # worksheet.write_blank(row_index, 44, None)
                                # # '26917: Microsoft Windows SMB Registry : Nessus Cannot Access the Windows Registry'
                                # worksheet.write_blank(row_index, 45, None)
                                # # '42897: SMB Registry : Start the Registry Service during the scan (WMI)'
                                # worksheet.write_blank(row_index, 46, None)
                                # # '20811: Microsoft Windows Installed Software Enumeration (credentialed check)'
                                # worksheet.write_blank(row_index, 47, None)
                                # # '91825: Oracle DB Login Possible'
                                # worksheet.write_blank(row_index, 48, None)
                                # # '91827: Microsoft SQL Server Login Possible'
                                # worksheet.write_blank(row_index, 49, None)
                                # # '47864: Cisco IOS Version'
                                # worksheet.write_blank(row_index, 50, None)
                                # # '67217: Cisco IOS XE Version'
                                # worksheet.write_blank(row_index, 51, None)

                end_time = time.time()
                elapsed_time = end_time - start_time
                elapsed_time_parsed = time.strftime('%H:%M:%S', time.gmtime(elapsed_time))

                self.log_emitter('info ', nessus_scan_file, '[elapsed_time={0}]'.format(elapsed_time_parsed))
                self.log_emitter('end  ', nessus_scan_file)

            except Exception as e:
                number_of_files_with_errors += 1
                traceback.print_exc()
                self.log_emitter('info',
                                 "ERROR Parsing [" + str(nessus_scan_file_number) + "/" +
                                 str(len(list_of_source_files)) + "] nessus files")
                self.log_emitter('info', e)

        if number_of_rows > 0:
            worksheet.autofilter(0, 0, number_of_rows, number_of_columns - 1)

    def create_worksheet_for_vulnerabilities(self, workbook, list_of_source_files):
        """
        Function create spreadsheet with vulnerabilities sum-up in given workbook for selected files.
        :param workbook: workbook where spreadsheet are created
        :param list_of_source_files: list of selected files
        """
        report_name = 'vulnerabilities'
        self.report_counter += 1
        info_report = 'Report: ' + str(self.report_counter) + '/' + str(self.number_of_selected_reports)

        worksheet = workbook.add_worksheet(report_name)

        cell_format_bold = workbook.add_format({'bold': True})
        worksheet.set_row(0, None, cell_format_bold)

        # print('>>>>>>>>>>>>>>>> ', self.report_vulnerabilities_debug_data_enabled)

        if not self.report_vulnerabilities_debug_data_enabled:
            headers = [
                # 'Nessus scanner IP',
                # 'Nessus scan name',
                # 'Nessus file name',
                'Target',
                'Hostname',
                'FQDN',
                'IP',
                'Scanned',
                'Credentialed checks',
                # 'Policy name',
                'Protocol',
                'Service Name',
                'Port',
                'Plugin ID',
                'Plugin name',
                'Plugin type',
                'Risk Factor',
                'Plugin family',
                # 'Plugin file name',
                'Plugin version',
                'Plugin publication date',
                'Plugin modification date',
                'Plugin description',
                'Solution',
                'Plugin output'
            ]
        else:
            headers = [
                'Nessus scanner IP',
                'Nessus scan name',
                'Nessus file name',
                'Target',
                'Hostname',
                'FQDN',
                'IP',
                'Scanned',
                'Credentialed checks',
                'Policy name',
                'Protocol',
                'Service Name',
                'Port',
                'Plugin ID',
                'Plugin name',
                'Plugin type',
                'Risk Factor',
                'Plugin family',
                'Plugin file name',
                'Plugin version',
                'Plugin publication date',
                'Plugin modification date',
                'Plugin description',
                'Solution',
                'Plugin output'
            ]
        number_of_columns = len(headers)
        # print('Number of columns: ' + str(number_of_columns))

        worksheet.set_column(0, number_of_columns - 1, 18)

        debug_columns_list = [0, 1, 2, 9, 18]

        for column_index, header in enumerate(headers):
            if self.report_vulnerabilities_debug_data_enabled and column_index in debug_columns_list:
                cell_format_bold_blue = workbook.add_format()
                cell_format_bold_blue.set_bold()
                cell_format_bold_blue.set_font_color('blue')
                worksheet.write(0, column_index, header, cell_format_bold_blue)
            else:
                worksheet.write(0, column_index, header)

        worksheet.freeze_panes(1, 0)  # Freeze the first row.

        nessus_scan_file_number = 0
        number_of_files_with_errors = 0

        number_of_rows = 0
        row_index = 0
        row_index_per_file = 0
        for nessus_scan_file in list_of_source_files:
            row_index_per_file += 1
            nessus_scan_file_number = nessus_scan_file_number + 1
            info_file = ', File: ' + str(row_index_per_file) + '/' + str(len(list_of_source_files))

            try:
                root = nfr.file.nessus_scan_file_root_element(nessus_scan_file)

                nessus_scan_file = nfr.file.nessus_scan_file_name_with_path(nessus_scan_file)

                start_time = time.time()
                self.log_emitter('start', nessus_scan_file)
                self.file_conversion_started.emit(1)

                source_file_size = nfa.utilities.size_of_file_human(nessus_scan_file)
                self.log_emitter('info ', nessus_scan_file, '[source_file_size={0}]'.format(source_file_size))
                self.log_emitter('info ', nessus_scan_file, '[report_type={0}]'.format(report_name))
                self.log_emitter('info ', nessus_scan_file,
                                 '[number_of_target_hosts={0}]'.format(nfr.scan.number_of_target_hosts(root)))
                self.log_emitter('info ', nessus_scan_file,
                                 '[number_of_scanned_hosts={0}]'.format(nfr.scan.number_of_scanned_hosts(root)))
                self.log_emitter('info ', nessus_scan_file, '[number_of_scanned_hosts_with_credentials={0}]'.format(
                    nfr.scan.number_of_scanned_hosts_with_credentialed_checks_yes(root)))

                date_format = workbook.add_format({'num_format': 'yyyy-mm-dd'})

                scan_report_name = nfr.scan.report_name(root)
                nessus_scan_file_name_with_path = nfr.file.nessus_scan_file_name_with_path(nessus_scan_file)
                scan_policy_name = nfr.scan.policy_name(root)

                report_host_counter = 0
                number_of_report_hosts = nfr.scan.number_of_scanned_hosts(root)

                info_host = ', Host: ' + str(report_host_counter) + '/' + str(number_of_report_hosts)
                info_final = info_report + info_file + info_host
                self.print_status_bar_info.emit(info_final)

                for report_host in nfr.scan.report_hosts(root):

                    report_host_counter += 1
                    self.progress.emit(report_host_counter, number_of_report_hosts)

                    info_host = ', Host: ' + str(report_host_counter) + '/' + str(number_of_report_hosts)
                    info_final = info_report + info_file + info_host
                    self.print_status_bar_info.emit(info_final)

                    report_items_per_host = nfr.host.report_items(report_host)

                    host_scanner_ip = nfr.host.scanner_ip(root, report_host)
                    host_report_host_name = nfr.host.report_host_name(report_host)
                    host_resolved_hostname = nfr.host.resolved_hostname(report_host)
                    host_resolved_fqdn = nfr.host.resolved_fqdn(report_host)
                    host_resolved_ip = nfr.host.resolved_ip(report_host)
                    host_credentialed_checks = nfr.host.credentialed_checks(root, report_host)

                    for report_item in report_items_per_host:
                        number_of_rows += 1
                        row_index += 1
                        protocol = nfr.plugin.report_item_value(report_item, 'protocol')
                        service_name = nfr.plugin.report_item_value(report_item, 'svc_name')
                        port = int(nfr.plugin.report_item_value(report_item, 'port'))
                        plugin_id = int(nfr.plugin.report_item_value(report_item, 'pluginID'))
                        plugin_name = nfr.plugin.report_item_value(report_item, 'pluginName')
                        plugin_type = nfr.plugin.report_item_value(report_item, 'plugin_type')
                        risk_factor = nfr.plugin.report_item_value(report_item, 'risk_factor')
                        plugin_family = nfr.plugin.report_item_value(report_item, 'pluginFamily')
                        plugin_file_name = nfr.plugin.report_item_value(report_item, 'fname')
                        plugin_version = nfr.plugin.report_item_value(report_item, 'script_version')
                        plugin_publication_date = nfr.plugin.report_item_value(report_item, 'plugin_publication_date')
                        plugin_modification_date = nfr.plugin.report_item_value(report_item, 'plugin_modification_date')
                        plugin_description = nfr.plugin.report_item_value(report_item, 'description')
                        solution = nfr.plugin.report_item_value(report_item, 'solution')
                        plugin_output = nfr.plugin.report_item_value(report_item, 'plugin_output')

                        if not self.report_vulnerabilities_debug_data_enabled:
                            worksheet.write(row_index, 0, host_report_host_name)
                            worksheet.write(row_index, 1, host_resolved_hostname)
                            worksheet.write(row_index, 2, host_resolved_fqdn)
                            worksheet.write(row_index, 3, host_resolved_ip)
                            worksheet.write(row_index, 4, 'yes')
                            worksheet.write(row_index, 5, host_credentialed_checks)
                            worksheet.write(row_index, 6, protocol)
                            worksheet.write(row_index, 7, service_name)
                            worksheet.write(row_index, 8, port)
                            worksheet.write(row_index, 9, plugin_id)
                            worksheet.write(row_index, 10, plugin_name)
                            worksheet.write(row_index, 11, plugin_type)
                            if self.report_vulnerabilities_none_filter_out:
                                if risk_factor == 'None':
                                    worksheet.set_row(row_index, options={'hidden': True})
                            worksheet.write(row_index, 12, risk_factor)
                            worksheet.write(row_index, 13, plugin_family)
                            worksheet.write(row_index, 14, plugin_version)
                            if plugin_publication_date is not None:
                                worksheet.write_datetime(row_index, 15,
                                                         nfr.plugin.plugin_date(plugin_publication_date), date_format)
                            else:
                                worksheet.write_blank(row_index, 15, None)
                            if plugin_modification_date is not None:
                                worksheet.write_datetime(row_index, 16,
                                                         nfr.plugin.plugin_date(plugin_modification_date), date_format)
                            else:
                                worksheet.write_blank(row_index, 16, None)
                            worksheet.write(row_index, 17, plugin_description)
                            worksheet.write(row_index, 18, solution)
                            if plugin_output is not None:
                                worksheet.write_string(row_index, 19, plugin_output)
                            else:
                                worksheet.write_blank(row_index, 19, None)
                        else:
                            worksheet.write(row_index, 0, host_scanner_ip)
                            worksheet.write(row_index, 1, scan_report_name)
                            worksheet.write(row_index, 2, nessus_scan_file_name_with_path)
                            worksheet.write(row_index, 3, host_report_host_name)
                            worksheet.write(row_index, 4, host_resolved_hostname)
                            worksheet.write(row_index, 5, host_resolved_fqdn)
                            worksheet.write(row_index, 6, host_resolved_ip)
                            worksheet.write(row_index, 7, 'yes')
                            worksheet.write(row_index, 8, host_credentialed_checks)
                            worksheet.write(row_index, 9, scan_policy_name)
                            worksheet.write(row_index, 10, protocol)
                            worksheet.write(row_index, 11, service_name)
                            worksheet.write(row_index, 12, port)
                            worksheet.write(row_index, 13, plugin_id)
                            worksheet.write(row_index, 14, plugin_name)
                            worksheet.write(row_index, 15, plugin_type)
                            if self.report_vulnerabilities_none_filter_out:
                                if risk_factor == 'None':
                                    worksheet.set_row(row_index, options={'hidden': True})
                            worksheet.write(row_index, 16, risk_factor)
                            worksheet.write(row_index, 17, plugin_family)
                            worksheet.write(row_index, 18, plugin_file_name)
                            worksheet.write(row_index, 19, plugin_version)
                            if plugin_publication_date is not None:
                                worksheet.write_datetime(row_index, 20,
                                                         nfr.plugin.plugin_date(plugin_publication_date), date_format)
                            else:
                                worksheet.write_blank(row_index, 20, None)
                            if plugin_modification_date is not None:
                                worksheet.write_datetime(row_index, 21,
                                                         nfr.plugin.plugin_date(plugin_modification_date), date_format)
                            else:
                                worksheet.write_blank(row_index, 21, None)
                            worksheet.write(row_index, 22, plugin_description)
                            worksheet.write(row_index, 23, solution)
                            if plugin_output is not None:
                                worksheet.write_string(row_index, 24, plugin_output)
                            else:
                                worksheet.write_blank(row_index, 24, None)

                end_time = time.time()
                elapsed_time = end_time - start_time
                elapsed_time_parsed = time.strftime('%H:%M:%S', time.gmtime(elapsed_time))

                self.log_emitter('info ', nessus_scan_file, '[elapsed_time={0}]'.format(elapsed_time_parsed))
                self.log_emitter('end  ', nessus_scan_file)

            except Exception as e:
                number_of_files_with_errors += 1
                traceback.print_exc()
                self.log_emitter('info',
                                 "ERROR Parsing [" + str(nessus_scan_file_number) + "/" +
                                 str(len(list_of_source_files)) + "] nessus files")
                self.log_emitter('info', e)

        if number_of_rows > 0:
            worksheet.autofilter(0, 0, number_of_rows, number_of_columns - 1)

            if self.report_vulnerabilities_none_filter_out:
                risk_factors = ['Critical', 'High', 'Medium', 'Low']
                if not self.report_vulnerabilities_debug_data_enabled:
                    worksheet.filter_column_list(12, risk_factors)
                else:
                    worksheet.filter_column_list(16, risk_factors)

    def create_worksheet_for_noncompliance(self, workbook, list_of_source_files):
        """
        Function create spreadsheet with noncompliance sum-up in given workbook for selected files.
        :param workbook: workbook where spreadsheet are created
        :param list_of_source_files: list of selected files
        """
        report_name = 'noncompliance'
        self.report_counter += 1
        info_report = 'Report: ' + str(self.report_counter) + '/' + str(self.number_of_selected_reports)

        worksheet = workbook.add_worksheet(report_name)

        cell_format_bold = workbook.add_format({'bold': True})
        worksheet.set_row(0, None, cell_format_bold)

        # print('>>>>>>>>>>>>>>>> ', self.report_noncompliance_debug_data_enabled)

        if not self.report_noncompliance_debug_data_enabled:
            headers = [
                # 'Nessus scanner IP',
                # 'Nessus scan name',
                # 'Nessus file name',
                'Target',
                'Hostname',
                'FQDN',
                'IP',
                'Scanned',
                'Credentialed checks',
                # 'Policy name',
                'Plugin ID',
                'Plugin name',
                'Plugin type',
                # 'Risk Factor',
                'Plugin family',
                # 'Compliance plugin file',
                # 'Plugin file name',
                'Plugin version',
                'Plugin publication date',
                'Plugin modification date',
                'Check name',
                'Audit file name',
                # 'Check ID',
                'Current value',
                # 'Uname',
                'Description',
                'Check status',
                'Reference',
                'Error'
            ]
        else:
            headers = [
                'Nessus scanner IP',
                'Nessus scan name',
                'Nessus file name',
                'Target',
                'Hostname',
                'FQDN',
                'IP',
                'Scanned',
                'Credentialed checks',
                'Policy name',
                'Plugin ID',
                'Plugin name',
                'Plugin type',
                'Risk Factor',
                'Plugin family',
                'Compliance plugin file',
                'Plugin file name',
                'Plugin version',
                'Plugin publication date',
                'Plugin modification date',
                'Check name',
                'Audit file name',
                'Check ID',
                'Current value',
                'Uname',
                'Description',
                'Check status',
                'Reference',
                'Error'
            ]
        number_of_columns = len(headers)
        # print('Number of columns: ' + str(number_of_columns))

        worksheet.set_column(0, number_of_columns - 1, 18)

        debug_columns_list = [0, 1, 2, 9, 13, 15, 16, 22, 24]

        for column_index, header in enumerate(headers):
            if self.report_noncompliance_debug_data_enabled and column_index in debug_columns_list:
                cell_format_bold_blue = workbook.add_format()
                cell_format_bold_blue.set_bold()
                cell_format_bold_blue.set_font_color('blue')
                worksheet.write(0, column_index, header, cell_format_bold_blue)
            else:
                worksheet.write(0, column_index, header)

        worksheet.freeze_panes(1, 0)  # Freeze the first row.

        nessus_scan_file_number = 0
        number_of_files_with_errors = 0

        number_of_rows = 0
        row_index = 0
        row_index_per_file = 0
        for nessus_scan_file in list_of_source_files:
            row_index_per_file += 1
            nessus_scan_file_number = nessus_scan_file_number + 1
            info_file = ', File: ' + str(row_index_per_file) + '/' + str(len(list_of_source_files))

            try:
                root = nfr.file.nessus_scan_file_root_element(nessus_scan_file)

                nessus_scan_file = nfr.file.nessus_scan_file_name_with_path(nessus_scan_file)

                start_time = time.time()
                self.log_emitter('start', nessus_scan_file)
                self.file_conversion_started.emit(1)

                source_file_size = nfa.utilities.size_of_file_human(nessus_scan_file)
                self.log_emitter('info ', nessus_scan_file, '[source_file_size={0}]'.format(source_file_size))
                self.log_emitter('info ', nessus_scan_file, '[report_type={0}]'.format(report_name))
                self.log_emitter('info ', nessus_scan_file,
                                 '[number_of_target_hosts={0}]'.format(nfr.scan.number_of_target_hosts(root)))
                self.log_emitter('info ', nessus_scan_file,
                                 '[number_of_scanned_hosts={0}]'.format(nfr.scan.number_of_scanned_hosts(root)))
                self.log_emitter('info ', nessus_scan_file, '[number_of_scanned_hosts_with_credentials={0}]'.format(
                    nfr.scan.number_of_scanned_hosts_with_credentialed_checks_yes(root)))

                date_format = workbook.add_format({'num_format': 'yyyy-mm-dd hh:mm:ss'})

                scan_report_name = nfr.scan.report_name(root)
                nessus_scan_file_name_with_path = nfr.file.nessus_scan_file_name_with_path(nessus_scan_file)
                scan_policy_name = nfr.scan.policy_name(root)

                report_host_counter = 0
                number_of_report_hosts = nfr.scan.number_of_scanned_hosts(root)

                info_host = ', Host: ' + str(report_host_counter) + '/' + str(number_of_report_hosts)
                info_final = info_report + info_file + info_host
                self.print_status_bar_info.emit(info_final)

                for report_host in nfr.scan.report_hosts(root):
                    report_host_counter += 1
                    self.progress.emit(report_host_counter, number_of_report_hosts)

                    info_host = ', Host: ' + str(report_host_counter) + '/' + str(number_of_report_hosts)
                    info_final = info_report + info_file + info_host
                    self.print_status_bar_info.emit(info_final)

                    report_items_per_host = nfr.host.report_items(report_host)
                    host_scanner_ip = nfr.host.scanner_ip(root, report_host)
                    host_report_host_name = nfr.host.report_host_name(report_host)
                    host_resolved_hostname = nfr.host.resolved_hostname(report_host)
                    host_resolved_fqdn = nfr.host.resolved_fqdn(report_host)
                    host_resolved_ip = nfr.host.resolved_ip(report_host)
                    host_credentialed_checks = nfr.host.credentialed_checks(root, report_host)

                    for report_item in report_items_per_host:
                        if nfr.plugin.compliance_plugin(report_item):
                            compliance_plugin = 'true'
                            row_index += 1
                            number_of_rows += 1
                            compliance_check_name = \
                                nfr.plugin.compliance_check_item_value(report_item, 'cm:compliance-check-name')
                            compliance_check_audit_file = \
                                nfr.plugin.compliance_check_item_value(report_item, 'cm:compliance-audit-file')
                            compliance_check_check_id = \
                                nfr.plugin.compliance_check_item_value(report_item, 'cm:compliance-check-id')
                            compliance_check_actual_value = \
                                nfr.plugin.compliance_check_item_value(report_item, 'cm:compliance-actual-value')
                            compliance_check_uname = \
                                nfr.plugin.compliance_check_item_value(report_item, 'cm:compliance-uname')
                            compliance_check_info = \
                                nfr.plugin.compliance_check_item_value(report_item, 'cm:compliance-info')
                            compliance_check_result = \
                                nfr.plugin.compliance_check_item_value(report_item, 'cm:compliance-result')
                            compliance_check_reference = \
                                nfr.plugin.compliance_check_item_value(report_item, 'cm:compliance-reference')
                            compliance_check_error = \
                                nfr.plugin.compliance_check_item_value(report_item, 'cm:compliance-error')

                            plugin_id = int(nfr.plugin.report_item_value(report_item, 'pluginID'))
                            plugin_name = nfr.plugin.report_item_value(report_item, 'pluginName')
                            plugin_type = nfr.plugin.report_item_value(report_item, 'plugin_type')
                            risk_factor = nfr.plugin.report_item_value(report_item, 'risk_factor')
                            plugin_family = nfr.plugin.report_item_value(report_item, 'pluginFamily')
                            plugin_file_name = nfr.plugin.report_item_value(report_item, 'fname')
                            plugin_version = nfr.plugin.report_item_value(report_item, 'script_version')
                            plugin_publication_date = \
                                nfr.plugin.report_item_value(report_item, 'plugin_publication_date')
                            plugin_modification_date = \
                                nfr.plugin.report_item_value(report_item, 'plugin_modification_date')

                            if not self.report_noncompliance_debug_data_enabled:
                                worksheet.write(row_index, 0, host_report_host_name)
                                worksheet.write(row_index, 1, host_resolved_hostname)
                                worksheet.write(row_index, 2, host_resolved_fqdn)
                                worksheet.write(row_index, 3, host_resolved_ip)
                                worksheet.write(row_index, 4, 'yes')
                                worksheet.write(row_index, 5, host_credentialed_checks)
                                worksheet.write(row_index, 6, plugin_id)
                                worksheet.write(row_index, 7, plugin_name)
                                worksheet.write(row_index, 8, plugin_type)
                                worksheet.write(row_index, 9, plugin_family)
                                worksheet.write(row_index, 10, plugin_version)
                                worksheet.write_datetime(row_index, 11, nfr.plugin.plugin_date(plugin_publication_date),
                                                         date_format)
                                worksheet.write_datetime(row_index, 12,
                                                         nfr.plugin.plugin_date(plugin_modification_date),
                                                         date_format)
                                worksheet.write(row_index, 13, compliance_check_name)
                                worksheet.write(row_index, 14, compliance_check_audit_file)
                                worksheet.write(row_index, 15, compliance_check_actual_value)
                                worksheet.write(row_index, 16, compliance_check_info)
                                worksheet.write(row_index, 17, compliance_check_result)
                                worksheet.write(row_index, 18, compliance_check_reference)
                                worksheet.write(row_index, 19, compliance_check_error)
                            else:
                                worksheet.write(row_index, 0, host_scanner_ip)
                                worksheet.write(row_index, 1, scan_report_name)
                                worksheet.write(row_index, 2, nessus_scan_file_name_with_path)
                                worksheet.write(row_index, 3, host_report_host_name)
                                worksheet.write(row_index, 4, host_resolved_hostname)
                                worksheet.write(row_index, 5, host_resolved_fqdn)
                                worksheet.write(row_index, 6, host_resolved_ip)
                                worksheet.write(row_index, 7, 'yes')
                                worksheet.write(row_index, 8, host_credentialed_checks)
                                worksheet.write(row_index, 9, scan_policy_name)
                                worksheet.write(row_index, 10, plugin_id)
                                worksheet.write(row_index, 11, plugin_name)
                                worksheet.write(row_index, 12, plugin_type)
                                worksheet.write(row_index, 13, risk_factor)
                                worksheet.write(row_index, 14, plugin_family)
                                worksheet.write(row_index, 15, compliance_plugin)
                                worksheet.write(row_index, 16, plugin_file_name)
                                worksheet.write(row_index, 17, plugin_version)
                                worksheet.write_datetime(row_index, 18, nfr.plugin.plugin_date(plugin_publication_date),
                                                         date_format)
                                worksheet.write_datetime(row_index, 19,
                                                         nfr.plugin.plugin_date(plugin_modification_date),
                                                         date_format)
                                worksheet.write(row_index, 20, compliance_check_name)
                                worksheet.write(row_index, 21, compliance_check_audit_file)
                                worksheet.write(row_index, 22, compliance_check_check_id)
                                worksheet.write(row_index, 23, compliance_check_actual_value)
                                worksheet.write(row_index, 24, compliance_check_uname)
                                worksheet.write(row_index, 25, compliance_check_info)
                                worksheet.write(row_index, 26, compliance_check_result)
                                worksheet.write(row_index, 27, compliance_check_reference)
                                worksheet.write(row_index, 28, compliance_check_error)

                end_time = time.time()
                elapsed_time = end_time - start_time
                elapsed_time_parsed = time.strftime('%H:%M:%S', time.gmtime(elapsed_time))

                self.log_emitter('info ', nessus_scan_file, '[elapsed_time={0}]'.format(elapsed_time_parsed))
                self.log_emitter('end  ', nessus_scan_file)

            except Exception as e:
                number_of_files_with_errors += 1
                traceback.print_exc()
                self.log_emitter('info',
                                 "ERROR Parsing [" + str(nessus_scan_file_number) + "/" +
                                 str(len(list_of_source_files)) + "] nessus files")
                self.log_emitter('info', e)

        if number_of_rows > 0:
            worksheet.autofilter(0, 0, number_of_rows, number_of_columns - 1)

    def log_emitter(self, action_name, source_file_name, additional_info=''):
        """
        Function emits information from thread to display it in GUI.

        :param action_name: information about action name
        :param source_file_name: information about related source file
        :param additional_info: add more information if needed
        """
        notification = '[action={0}] [source_file_name={1}] {2}'.format(action_name, source_file_name,
                                                                        additional_info)
        self.signal.emit(notification)


def main():
    app = QApplication(sys.argv)
    form = MainWindow()

    app_name = nfa.__about__.__title__
    app_version = nfa.__about__.__version__
    app_version_release_date = nfa.__about__.__release_date__
    app.setApplicationName(app_name)
    app.setApplicationVersion(app_version)
    name = app.applicationName()
    # version = app.applicationVersion()

    app_window_title = name
    form.setWindowTitle(app_window_title)
    print(app_name, app_version, app_version_release_date)

    # app_icon_file_name_png = 'LimberDuck-nessus-file-analyzer.png'
    # app_icon_file_name_png_to_ico = nfa.utilities.png_to_ico(app_icon_file_name_png)
    # app_icon_file_name_ico_to_base64 = nfa.utilities.file_to_base64(app_icon_file_name_png_to_ico)
    # app_icon_file_name_ico = nfa.utilities.base64_to_ico(app_icon_file_name_ico_to_base64,app_icon_file_name_png)
    # app_icon_file_name_ico = 'LimberDuck-nessus-file-analyzer.ico'

    icon_file_name = nfa.__about__.__icon__
    nfa.utilities.base64_to_ico(nfa.ico, icon_file_name)

    app.setWindowIcon(QIcon(icon_file_name))

    os.remove(icon_file_name)

    form.show()
    sys.exit(app.exec_())
