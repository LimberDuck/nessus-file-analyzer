# Change Log

This document records all notable changes to [nessus file analyzer by LimberDuck][1].

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.7.0] - 2021-09-06

### Added

- `nessus-file-analyzer` as Python package - from now on you can install it with `pip install nessus-file-analyzer`
- entry point `nessus-file-analyzer` added - from now on, after installation of **nessus file analyzer** you can run it with command `nessus-file-analyzer`, read more in documentation in [Installation instructions](https://nessus-file-analyzer.readthedocs.io/en/latest/nfa-installation.html).

## [0.6.0] - 2021-08-23

### Added

- new columns added to Vulnerabilities report (read more in [documentation](https://nessus-file-analyzer.readthedocs.io/en/latest/nfa-target-file/section-vulnerabilities.html)):
  -  Exploit available,
  -  Exploit code maturity,
  -  Exploit framework metasploit,
  -  Exploitability ease,

## [0.5.1] - 2021-03-27

### Changed

- Requirements updated with newer version of pillow.

## [0.5.0] - 2020-07-25

### Added

- **ZIP Archive support** - now you will have possibility to analyze nessus files just from inside of zip archive files:
    - Go to File > Open file\-s and select "ZIP Archive (*.zip)" extension to see zip archive files and select them.
    - Go to File > Open directory and select directory nessus files and zip archive files containing nessus files will be automatically taken from selected directory and its subdirectories.
    - Simple drag and drop zip archive file or directories on *nessus file analyzer by LimberDuck* window to open zip archive files containing nessus files from dropped directory and its subdirectories.
- **NetBIOS information in host report** - if you turn on debug option for host report type you will have two additional columns with information about:
    - NetBIOS Computer name - if available in Plugin ID 10150 output.
    - NetBIOS Domain name - if available in Plugin ID 10150 output.

## [0.4.0] - 2019-09-09

### Added

- **CVE information in vulnerabilities report** - now you will have two additional columns at the end:
    - CVE counter - with number of all CVE numbers assigned to particular plugin, if there is no CVE assigned cell has value 0
    - CVE number - with list of CVE numbers assigned to particular plugin, if there is no CVE assigned cell is empty


## [0.3.1] - 2019-09-02

### Changed

- **Start button and menu option Start analysis** - will be set to disabled if you do not provide nessus files during the next selection (e.g. cancelling nessus files selection, cancelling source directory selection, selecting directory without nessus files, dropping files with extension different than .nessus, dropping directory without nessus files)
- **List of files to pars** - will be correctly cleared out if you do not provide nessus files during the next selection (e.g. cancelling nessus files selection, cancelling source directory selection, selecting directory without nessus files, dropping files with extension different than .nessus, dropping directory without nessus files)

## [0.3.0] - 2019-08-26

### Added

- **Drag & drop** - now you can drag and drop selected files or directories on *nessus file analyzer by LimberDuck* window to open nessus files.

### Changed

- **Validation of user input for custom suffix** - Settings > Target files > add custom suffix - now you will not be able to put chars like \\/:\*?"<>| which will let you save target file without any problem.


## [0.2.0] - 2019-08-19

### Added

- **skip None results** - Settings > Source files > vulnerabilities > skip None results - now you can skip findings reported by plugins with None Risk Factor, thanks to this, the resulting file size will be smaller.

### Changed

- **custom suffix field works as desired** - Updated option: Settings > Target files > add custom suffix - now input field for custom suffix is disabled by default. If you check this option input field becomes editable. Any text entered will result in automatic suffix change. Suffix will be cleared out if you uncheck this option or delete the entered text.


## [0.1.1] - 2019-07-21

### Changed

- From now on if source file or source directory has been already selected target directory will be set base on path from selected source file or base on path from first file from selected source directory if you use option "set source directory as target directory".
- Typo in tooltip for "Open" button to open target directory fixed.
- Naming convention changed everywhere from "conversion" to "analysis".


## [0.1.0] - 2019-06-23

- Initial release

[0.7.0]: https://github.com/LimberDuck/nessus-file-analyzer/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/LimberDuck/nessus-file-analyzer/compare/v0.5.1...v0.6.0
[0.5.1]: https://github.com/LimberDuck/nessus-file-analyzer/compare/v0.5.0...v0.5.1
[0.5.0]: https://github.com/LimberDuck/nessus-file-analyzer/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/LimberDuck/nessus-file-analyzer/compare/v0.3.1...v0.4.0
[0.3.1]: https://github.com/LimberDuck/nessus-file-analyzer/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/LimberDuck/nessus-file-analyzer/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/LimberDuck/nessus-file-analyzer/compare/v0.1.1...v0.2.0
[0.1.1]: https://github.com/LimberDuck/nessus-file-analyzer/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/LimberDuck/nessus-file-analyzer/releases/tag/v0.1.0

[1]: https://github.com/LimberDuck/nessus-file-analyzer