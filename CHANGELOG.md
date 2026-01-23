# Changelog

This document records all notable changes to [nessus file analyzer (NFA) by LimberDuck][1].

Visit [LimberDuck.org][2] to find out more!

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.12.5] - 2026-01-23

### Fixed

- Fixed an issue (`unsupported operand type(s) for +=: 'NoneType' and 'int'`) that occurred when results for plugin 19506 were missing for some hosts in scan results.

### Changed

- Requirements update
  - from:
    - nessus-file-reader>=0.7.0
  - to:
    - nessus-file-reader>=0.7.2

## [0.12.4] - 2026-01-22

### Fixed

-  `--hidden-import=nfa_plugin_software_enumeration.software_enumeration` added to PyInstaller build commands for Windows, macOS and Linux to include Software Enumeration plugin in the built application.

## [0.12.3] - 2026-01-22

### Fixed

- Pillow added to build pipeline for macOS.

## [0.12.2] - 2026-01-22

### Fixed

- The Software Enumeration plugin is now visible in the **Advanced reports** tab when using LimberDuck NFA downloaded from [GitHub Releases](https://github.com/LimberDuck/nessus-file-analyzer/releases).

## [0.12.1] - 2026-01-19

### Changed

- Requirements update
  - from:
    - nfa-plugin-software-enumeration>=0.1.1
  - to:
    - nfa-plugin-software-enumeration>=0.1.2
  - removed:
    - imageio>=2.37.0

## [0.12.0] - 2026-01-18

### Added

- **Settings** > **Advanced reports** tab added which allows to enable/disable additional reports provided by NFA plugins.
- **Software enumeration** v0.1.1 advanced report added, this report provides a list of all software detected on the hosts, along with their versions and installation dates. Red more at https://limberduck.org/en/latest/tools/nessus-file-analyzer/advanced-reports/index.html

### Changed

- **Settings** > **Source files** tab renamed to **Standard reports** tab.
- **Settings** > **Standard reports** > **vulnerabilities** report
  - If large file is processed and number of vulnerabilities exceeds 1 048 576 ([maximum number of rows in Excel worksheet](https://support.microsoft.com/en-us/office/excel-specifications-and-limits-1672b34d-7043-467e-8e27-269d656771c3)), a new worksheet named "vulnerabilities_2" is created. Note that working with very large files is not effective, so it is recommended to split scan targets into smaller batches before you even run the scan.

## [0.11.0] - 2025-10-10

### Added

- **Announcements** are now displayed in the Progress Preview window - either automatically upon opening or manually via `Help > Check Announcements`.

### Changed

- **Check for Updates** now automatically notifies you of a new version immediately after opening the application.

### Fixed

- Fixed an issue that prevented spreadsheets from saving when parsing files larger than 4 GB.

## [0.10.0] - 2025-09-08

### Added

- `File > Open file\-s` - default extension filter set to both Nessus scan file & ZIP Archive (`*.nessus` `*.zip`)
- Generated report has set document properties:
  - "title": "Security report",
  - "subject": "Vulnerability Assessment results",
  - "category": "Report",
  - "keywords": "Vulnerabilities, VA, VM, Nessus",
  - "comments": "Report generated with nessus file analyzer (NFA) by LimberDuck. Check https://limberduck.org for more details.",
- Pipeline with Build and Release for Windows, macOS and Linux.

### Changed

- Icon file renamed from `LimberDuck-nessus-file-analyzer` to `LimberDuck-NFA`.
- Default target directory changed from *current directory* to *user’s home directory*.
- Fix for app build on macOS.
- Update check directing to GitHub Releases as well.
- `version.rc` file info updated.

## [0.9.0] - 2025-09-01

### Added

- New options:
  - `Help > Check for Update` - will return confirmation if you are using the latest version of NFA.
  - `Help > Documentation` - will open NFA documentation at LimberDuck.org.
  - `Help > GitHub` - will open NFA GitHub page.
  - `Help > Releases` - will open NFA GitHub Releases page.

- Requirements update
  - from:
    - nessus-file-reader>=0.6.0
  - to:
    - nessus-file-reader>=0.7.0
  - new:
    - packaging>=25.0
    - requests>=2.32.5

## [0.8.0] - 2025-06-29

### Added

- Vulnerabilities report with new columns:
  - Severity Number (only in debug mode)
  - Severity
  - CVSSv2 Base Score (only in debug mode)
  - CVSSv2
  - CVSSv3 Base Score (only in debug mode)
  - CVSSv3
  - CVSSv4 Base Score (only in debug mode)
  - CVSSv4
  - VPR Score (only in debug mode)
  - VPR
  - EPSS (only in debug mode)
  - EPSS %


### Changed

- Progress preview with font color suited to dark and light modes.
- Vulnerabilities report - some columns width changed to save space on the screen.
- requirements update
  - from:
    - nessus-file-reader>=0.4.3
    - XlsxWriter>=3.2.2
  - to:
    - nessus-file-reader>=0.6.0
    - XlsxWriter>=3.2.5
- build tests for python
  - removed: 3.9


## [0.7.3] - 2025-02-20

### Changed

- code formatted with [black](https://black.readthedocs.io)
- requirements update
  - from:
    - chardet>=4.0.0
    - imageio>=2.9.0
    - nessus-file-reader>=0.4.1
    - PyQt5>=5.15.4
    - XlsxWriter>=3.0.1
  - to:
    - chardet>=5.2.0
    - imageio>=2.37.0
    - nessus-file-reader>=0.4.3
    - PyQt5>=5.15.11
    - XlsxWriter>=3.2.2

- build tests for python
  - added: 3.10, 3.11, 3.12, 3.13
  - removed: 3.7, 3.8

## [0.7.2] - 2022-05-13

### Added

- **Tenable.io files support** - initial support to pars nessus files coming from Tenable.io 
- **information about source tool** - information about `scan_file_source` added in `Progress preview`. Now you will see information like `Nessus`, `Tenable.sc`, `Tenable.io`

## [0.7.1] - 2021-10-06

### Fixed

- Concatenated column's headers `CVE numberExploit available` in Vulnerabilities tab report with unchecked option `add debug data` fixed by moving following column's headers one column to the right:
  -  Exploit available,
  -  Exploit code maturity,
  -  Exploit framework metasploit,
  -  Exploitability ease,

## [0.7.0] - 2021-09-06

### Added

- `nessus-file-analyzer` as Python package - from now on you can install it with `pip install nessus-file-analyzer`
- entry point `nessus-file-analyzer` added - from now on, after installation of **nessus file analyzer (NFA)** you can run it with command `nessus-file-analyzer`, read more in documentation in [Installation instructions](https://nessus-file-analyzer.readthedocs.io/en/latest/nfa-installation.html).

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
    - Simple drag and drop zip archive file or directories on *nessus file analyzer (NFA) by LimberDuck* window to open zip archive files containing nessus files from dropped directory and its subdirectories.
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

- **Drag & drop** - now you can drag and drop selected files or directories on *nessus file analyzer (NFA) by LimberDuck* window to open nessus files.

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

[0.12.5]: https://github.com/LimberDuck/nessus-file-analyzer/compare/v0.12.4...v0.12.5
[0.12.4]: https://github.com/LimberDuck/nessus-file-analyzer/compare/v0.12.3...v0.12.4
[0.12.3]: https://github.com/LimberDuck/nessus-file-analyzer/compare/v0.12.2...v0.12.3
[0.12.2]: https://github.com/LimberDuck/nessus-file-analyzer/compare/v0.12.1...v0.12.2
[0.12.1]: https://github.com/LimberDuck/nessus-file-analyzer/compare/v0.12.0...v0.12.1
[0.12.0]: https://github.com/LimberDuck/nessus-file-analyzer/compare/v0.11.0...v0.12.0
[0.11.0]: https://github.com/LimberDuck/nessus-file-analyzer/compare/v0.10.0...v0.11.0
[0.10.0]: https://github.com/LimberDuck/nessus-file-analyzer/compare/v0.9.0...v0.10.0
[0.9.0]: https://github.com/LimberDuck/nessus-file-analyzer/compare/v0.8.0...v0.9.0
[0.8.0]: https://github.com/LimberDuck/nessus-file-analyzer/compare/v0.7.3...v0.8.0
[0.7.3]: https://github.com/LimberDuck/nessus-file-analyzer/compare/v0.7.2...v0.7.3
[0.7.2]: https://github.com/LimberDuck/nessus-file-analyzer/compare/v0.7.1...v0.7.2
[0.7.1]: https://github.com/LimberDuck/nessus-file-analyzer/compare/v0.7.0...v0.7.1
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
[2]: https://limberduck.org