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

import base64
import imageio
import os
import chardet
import csv


def file_to_base64(filename):
    """
    Function converts given file into base64.
    :param filename: input file name with path
    :return: base64 string
    """
    with open(filename, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string


def png_to_ico(filename):
    """
    Function converts given png file into ico.
    :param filename: png file name
    :return: ico file name
    """
    filename_without_extension = os.path.splitext(filename)[0]
    target_file_name = filename_without_extension + '.ico'
    img = imageio.imread(filename)
    imageio.imwrite(target_file_name, img)

    # img = Image.open(filename)
    # icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
    # img.save(target_file_name, sizes=icon_sizes)

    return target_file_name


def base64_to_ico(ico_in_base64, filename):
    """
    Function write base64 string as ico file with pointed filename
    :param ico_in_base64:
    :param filename: get filename with extension to use it as target file name
    :return: ico file name
    """
    filename_without_extension = os.path.splitext(filename)[0]
    target_file_name = filename_without_extension + '.ico'
    icondata = base64.b64decode(ico_in_base64)
    iconfile = open(target_file_name, 'wb')
    iconfile.write(icondata)
    iconfile.close()

    return target_file_name


def check_file_encoding(file):
    """
    Function checks encoding for input file.
    :param file: input file path
    :return: file encoding eg. 'ascii', 'utf8'
    """
    raw_data = open(file, 'rb').read()
    result = chardet.detect(raw_data)
    char_enc = result['encoding']

    return char_enc


def size_human(size, suffix='B'):
    """
    Function convert provided size into human readable form
    :param size:  number
    :param suffix: suffix
    :return: file size in human readable form
    """

    for unit in [' b', ' Ki', ' Mi', ' Gi', ' Ti', ' Pi', ' Ei', ' Zi']:
        if abs(size) < 1024.0:
            return '%3.1f%s%s' % (size, unit, suffix)
        size /= 1024.0
    return '%.1f%s%s' % (size, 'Yi', suffix)


def size_of_file_human(file, suffix='B'):
    """
    Function convert size of provided file into human readable form
    :param file:  source file name with path
    :param suffix: suffix
    :return: file size in human readable form
    """
    file_real_size = os.path.getsize(file)
    file_real_size_human = size_human(file_real_size, suffix)

    return file_real_size_human


def size_of_file_inside_zip_human(zip_file, file_inside_zip, suffix='B'):
    """
    Function convert size of file from inside of provided zip file into human readable form
    :param zip_file: source zip file
    :param file_inside_zip:  source file name from inside of provided zip file
    :param suffix: suffix
    :return: file size in human readable form
    """

    file_real_size = zip_file.getinfo(file_inside_zip).file_size
    file_real_size_human = size_human(file_real_size, suffix)

    file_compress_size = zip_file.getinfo(file_inside_zip).compress_size
    file_compress_size_human = size_human(file_compress_size, suffix)

    return f'{file_compress_size_human} [{file_real_size_human}]'


def csv_file_row_counter(file, source_file_delimiter):
    """
    Function counts number of rows for selected input file.
    :param file: input file path
    :param source_file_delimiter: values delimiter
    :return: number of rows
    """
    source_file_encoding = check_file_encoding(file)
    file = open(file, 'r', encoding=source_file_encoding)
    csv.register_dialect('colons', delimiter=source_file_delimiter)
    reader = csv.reader(file, dialect='colons')

    row_count = sum(1 for row in reader)
    return row_count
