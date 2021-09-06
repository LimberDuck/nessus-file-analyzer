# nessus file analyzer

**nessus file analyzer** by LimberDuck (pronounced *ˈlɪm.bɚ dʌk*) is a GUI
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

[![Latest Release version](https://img.shields.io/github/v/release/LimberDuck/nessus-file-analyzer?label=Latest%20release)](https://github.com/LimberDuck/nessus-file-analyzer/releases) 
[![GitHub Release Date](https://img.shields.io/github/release-date/limberduck/nessus-file-analyzer?label=released&logo=GitHub)](https://github.com/LimberDuck/nessus-file-analyzer/releases) 
[![PyPI - Downloads](https://img.shields.io/pypi/dm/nessus-file-analyzer?logo=PyPI)](https://pypistats.org/packages/nessus-file-analyzer)

[![License](https://img.shields.io/github/license/LimberDuck/nessus-file-analyzer.svg)](https://github.com/LimberDuck/nessus-file-analyzer/blob/master/LICENSE)
[![Repo size](https://img.shields.io/github/repo-size/LimberDuck/nessus-file-analyzer.svg)](https://github.com/LimberDuck/nessus-file-analyzer)
[![Code size](https://img.shields.io/github/languages/code-size/LimberDuck/nessus-file-analyzer.svg)](https://github.com/LimberDuck/nessus-file-analyzer)
[![Supported platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey.svg)](https://github.com/LimberDuck/nessus-file-analyzer)
[![Documentation Status](https://readthedocs.org/projects/nessus-file-analyzer/badge/?version=latest)](https://nessus-file-analyzer.readthedocs.io/en/latest/?badge=latest)

![](https://user-images.githubusercontent.com/9287709/59981677-5fefcf80-9607-11e9-89aa-35e5649e1c7a.png)

## Main features

* select one or more nessus files at once or select directory to get all nessus files from it and from all its subdirectories
* select one or more of available report types like: 
  * scan, 
  * host, 
  * vulnerabilities,
  * noncompliance
* change target directory for output file to desired one, leave it default (current working directory) or set to be the same as source files
* add suffix for output file with `_YYYYMMDD_HHMMSS` and/or custom text

## Documentation

Visit https://nessus-file-analyzer.readthedocs.io to find out more.

## Installation

> **Note:**
> It's advisable to use python virtual environment for below instructions. Read more about python virtual environment in [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/dev/virtualenvs/)
> 
>Read about [virtualenvwrapper in The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/dev/virtualenvs/#virtualenvwrapper): [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io) provides a set of commands which makes working with virtual environments much more pleasant.


1. Install **nessus file analyzer**
    
   `pip install nessus-file-analyzer`

   > To upgrade to newer version run:
   > 
   > `pip install -U nessus-file-analyzer`

2. Run **nessus file analyzer**

   `nessus-file-analyzer`
   
   > Optionally for Linux and macOS:
   > 
   > `nessus-file-analyzer&`
   > 
   > Run with `&` at the end to start the process in the background.

3. Make a shortcut for **nessus file analyzer**

   **Windows:**
   
   - Run in cmd `where nessus-file-analyzer.exe`
   - Copy returned path.
   - Go to e.g. to Desktop.
   - Right click on Desktop and choose `New > Shortcut`.
   - Paste returned path.
   - Click `Next`, `Finish`.
   
   **Linux (Ubuntu) / macOS**
   - Run in Terminal `which nessus-file-analyzer`
   - Run in Terminal `ln -s path_returned_in_previous_command ~/Desktop/`

   **macOS**

   - Run in Terminal `which nessus-file-analyzer`
   - Open `bin` folder where `nessus-file-analyzer` is located.
   - Right click on `nessus-file-analyzer` and choose `Make alias`.
   - Move your alias e.g. to Desktop.

## Meta

### Change log

See [CHANGELOG].


### Licence

GNU GPLv3: [LICENSE].


### Authors

[Damian Krawczyk] created **[nessus file analyzer]** by [LimberDuck].

[nessus file analyzer]: https://limberduck.org/en/latest/nessus-file-analyzer
[Damian Krawczyk]: https://damiankrawczyk.com
[LimberDuck]: https://limberduck.org
[CHANGELOG]: https://github.com/LimberDuck/nessus-file-analyzer/blob/master/CHANGELOG.md
[LICENSE]: https://github.com/LimberDuck/nessus-file-analyzer/blob/master/LICENSE
