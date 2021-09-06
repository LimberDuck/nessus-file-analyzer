.. nessus-file-analyzer documentation master file, created by
   sphinx-quickstart on Sat Jul 25 19:08:38 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

####################################
nessus file analyzer's documentation
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

|latest_release| |latest_release_date| |pypi_downloads|

|license| |repo_size| |code_size| |supported_platform| |docs_status|

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

.. toctree::
   :caption: Links
   :hidden:

   LimberDuck.org <https://limberduck.org>
   LimberDuck on GitHub <https://github.com/limberduck>

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
    :alt: Repo size

.. |code_size| image:: https://img.shields.io/github/languages/code-size/LimberDuck/nessus-file-analyzer.svg
    :target: https://github.com/LimberDuck/nessus-file-analyzer
    :alt: Code size

.. |supported_platform| image:: https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey.svg
    :target: https://github.com/LimberDuck/nessus-file-analyzer
    :alt: Supported platform

.. |docs_status| image:: https://readthedocs.org/projects/nessus-file-analyzer/badge/?version=latest
    :target: https://nessus-file-analyzer.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
    :alt: Supported platform

.. |docs_status| image:: https://readthedocs.org/projects/nessus-file-analyzer/badge/?version=latest
    :target: https://nessus-file-analyzer.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |latest_release| image:: https://img.shields.io/github/v/release/LimberDuck/nessus-file-analyzer?label=Latest%20release
    :target: https://github.com/LimberDuck/nessus-file-analyzer/releases
    :alt: Latest Release version

.. |latest_release_date| image:: https://img.shields.io/github/release-date/limberduck/nessus-file-analyzer?label=released&logo=GitHub
    :target: https://github.com/LimberDuck/nessus-file-analyzer/releases
    :alt: GitHub Release Date

.. |pypi_downloads| image:: https://img.shields.io/pypi/dm/nessus-file-analyzer?logo=PyPI   
    :target: https://pypistats.org/packages/nessus-file-analyzer
    :alt: PyPI - Downloads