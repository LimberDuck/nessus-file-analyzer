.. nessus-file-analyzer documentation master file, created by
   sphinx-quickstart on Sat Jul 25 19:08:38 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

####################################
nessus-file-analyzer's documentation
####################################

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


Go through the first steps to quickly start using |nfa|.

.. toctree::
   :caption: Table of contents
   :maxdepth: 4
   :hidden:

.. toctree::
   :maxdepth: 2
   :caption: First steps

   nfa-first-steps

.. toctree::
   :maxdepth: 2
   :caption: Settings

   nfa-settings

.. toctree::
   :maxdepth: 2
   :caption: Installation
   
   nfa-installation

.. toctree::
   :maxdepth: 2
   :caption: Target file
   
   nfa-target-file/index

Meta
====

Changelog
---------

See `CHANGELOG`_.


Licence
-------

GNU GPLv3: `LICENSE`_.

Authors
-------

`Damian Krawczyk`_ created *nessus file analyzer* by LimberDuck.

.. _Damian Krawczyk: https://limberduck.org
.. _CHANGELOG: https://github.com/LimberDuck/nessus-file-analyzer/blob/master/CHANGELOG.md
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
