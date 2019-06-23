nessus file analyzer by LimberDuck
##################################

*nessus file analyzer* by LimberDuck (pronounced *ˈlɪm.bɚ dʌk*) is a GUI
tool which enables you to parse multiple nessus files containing the results
of scans performed by using Nessus by (C) Tenable, Inc. and exports parsed
data to a Microsoft Excel Workbook for effortless analysis.
Operational memory usage will be kept low while parsing even the largest of
files. You can run it on your favourite operating system, whether it is Windows,
macOS or GNU Linux. As a parsing result, you will receive spreadsheets with a
summary view of the whole scan and/or all reported hosts. You will also be
able to generate spreadsheets with a detailed view of all reported
vulnerabilities and/or noncompliance.
It's free and open source tool, which has been created to automate our work,
decrease our workload and focus on data analysis.

|license| |repo_size| |code_size| |supported_platform|

.. image:: https://user-images.githubusercontent.com/9287709/59981677-5fefcf80-9607-11e9-89aa-35e5649e1c7a.png
   :width: 600

.. class:: no-web no-pdf

.. contents::

.. section-numbering::

Main features
=============

* select one or more nessus files at once or select directory to get all nessus files from it and from all its subdirectories
* select one or more of available report types like: scan, host, vulnerabilities, noncompliance
* change target directory for output file to desired one, leave it default (current working directory) or set to be the same as source files
* add suffix for output file with "_YYYYMMDD_HHMMSS" and/or custom text

Usage
=====
1. Go to Menu "File".
2. Choose:

    - "Open file\\-s" if you want to open one or more nessus files at once.

    or

    - "Open directory" if you want to open all nessus files from selected directory and its subdirectories.

3. Select one or more report type:

    - "scan" - if you want to see sum-up from point of view of whole scan
    - "host" - if you want to see sum-up from point of view of particular host from given scan
    - "vulnerabilities" - if you want to see list of vulnerabilities reported in this scan for all scanned hosts
    - "noncompliance" - if you want to see list of noncompliance reported in this scan for all scanned hosts

4. Click "Start" button to initiate analyze of all selected files.

5. Click "Open" button to open target directory where output file has been placed.

Options
=======
"Source files" tab:

* Mark checkbox "add debug data" to get additional columns for selected report type like source file name with path, policy name and more. *Note: Debug columns names are marked in blue color.*
* Mark checkbox "filter out None results" available for vulnerabilities report type to automatically filter out plugins results with None Risk Factor and see only these which Risk Factor is equal Low, Medium, High or Critical. *Note: Plugins results with None Risk Factor are not removed from report, to see them use filter in column Risk Factor.*

"Target files" tab:

* Click "Change" button (next to target directory field) to change target directory and use it for output file.
* Mark checkbox "set source directory as target directory" to automatically change target directory each time when you select new source file/-s and set target directory to be the same as source file/-s directory. *Note: If you use "Open directory" option to open source files this directory will be use as target directory for all files including these from subdirectories.*
* Mark checkbox "add suffix with "_YYYYMMDD_HHMMSS"" to add suffix with "_YYYYMMDD_HHMMSS" into target filename. *Note: Take a look below this checbox to see target filename example received that way.*
* Mark checkbox "add custom suffix" if you want to add suffix taken from field on the right into target filename. *Note: Take a look below this checkbox to see target filename example received that way.*

Build executable file
=====================

Windows
-------
1. If you don't have, install Python 3.6.0 or higher, you can download it via https://www.python.org/downloads
2. If you don't have, install latest version of Git, you can download it via https://git-scm.com/downloads
3. Clone *LimberDuck nessus file analyzer* repository using below command in Git Bash:

.. code-block:: powershell

 git clone https://github.com/LimberDuck/nessus-file-analyzer.git

4. Install requirements using below command

.. code-block:: powershell

 pip install -r .\requirements.txt

5. Run *nessus file analyzer* using below command

.. code-block:: powershell

 python nfa.py

6. Upgrade setuptools using below command

.. code-block:: powershell

 pip install --upgrade setuptools

7. Install PyInstaller

.. code-block:: bash

 pip install PyInstaller

8. Build your own executable file using below command

.. code-block:: powershell

 pyinstaller --onefile --windowed --icon=.\icons\LimberDuck-nessus-file-analyzer.ico nfa.py

9. Go to dist catalog to find executable file *nfa.exe*

Linux (Ubuntu)
--------------
1. Python 3.6.7 should be already installed in Ubuntu 18.04.1 LTS, you can ensure with below command

.. code-block:: bash

 python3 --version

2. If you don't have, install git using below command

.. code-block:: bash

 sudo apt install git

3. Clone *LimberDuck nessus file analyzer* repository using below command

.. code-block:: bash

 git clone https://github.com/LimberDuck/nessus-file-analyzer.git

4. If you don't have, install pip using below command

.. code-block:: bash

 sudo apt install python3-pip

5. Install requirements using below command

.. code-block:: bash

 pip3 install -r .\requirements.txt


6. Run *nessus file analyzer* using below command

.. code-block:: bash

 python3 nfa.py

7. Upgrade setuptools using below command

.. code-block:: bash

 pip3 install --upgrade setuptools

8. Install PyInstaller

.. code-block:: bash

 pip install PyInstaller

9. Build your own executable file using below command

.. code-block:: bash

 ~/.local/bin/pyinstaller --onefile --windowed --icon=./icons/LimberDuck-nessus-file-analyzer.ico nfa.py

10. Go to dist catalog to find executable file *nfa*

MacOS
-----
1. If you don't have, install Python 3.6.0 or higher, you can download it via https://www.python.org/downloads

2. Clone *LimberDuck nessus file analyzer* repository using below command

.. code-block:: bash

 git clone https://github.com/LimberDuck/nessus-file-analyzer.git

3. Install requirements using below command

.. code-block:: bash

 pip3.6 install -r .\requirements.txt

4. Run *nessus file analyzer* using below command

.. code-block:: bash

 python3.6 nfa.py

5. Upgrade setuptools using below command

.. code-block:: bash

 pip3.6 install --upgrade setuptools

6. Install PyInstaller

.. code-block:: bash

 pip install PyInstaller

7. Build your own executable file using below command

.. code-block:: bash

 pyinstaller --onefile --windowed --icon=./icons/LimberDuck-nessus-file-analyzer.ico nfa.py

8. Go to dist catalog to find executable file *nfa*

Meta
====

Change log
----------

See `CHANGELOG`_.


Licence
-------

GNU GPLv3: `LICENSE`_.



Authors
-------

`Damian Krawczyk`_ created *nessus file analyzer* by LimberDuck.

.. _Damian Krawczyk: https://limberduck.org
.. _CHANGELOG: https://github.com/LimberDuck/nessus-file-analyzer/blob/master/CHANGELOG.rst
.. _LICENSE: https://github.com/LimberDuck/nessus-file-analyzer/blob/master/LICENSE


.. |license| image:: https://img.shields.io/github/license/LimberDuck/nessus-file-analyzer.svg
    :target: https://github.com/LimberDuck/nessus-file-analyzer/blob/master/LICENSE
    :alt: License

.. |repo_size| image:: https://img.shields.io/github/repo-size/LimberDuck/nessus-file-analyzer.svg
    :target: https://github.com/LimberDuck/nessus-file-analyzer

.. |code_size| image:: https://img.shields.io/github/languages/code-size/LimberDuck/nessus-file-analyzer.svg
    :target: https://github.com/LimberDuck/nessus-file-analyzer

.. |supported_platform| image:: https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey.svg
    :target: https://github.com/LimberDuck/nessus-file-analyzer
