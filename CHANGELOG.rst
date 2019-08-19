==========
Change Log
==========

This document records all notable changes to `nessus file analyzer by LimberDuck <https://github.com/LimberDuck/nessus-file-analyzer>`_.
This project adheres to `Semantic Versioning <http://semver.org/>`_.


0.2.0 (2019-08-19)
---------------------

* New option: Settings > Source files > vulnerabilities > skip None results - now you can skip findings reported by plugins with None Risk Factor, thanks to this, the resulting file size will be smaller.
* Updated option: Settings > Target files > add custom suffix - now input field for custom suffix is disabled by default. If you check this option input field becomes editable. Any text entered will result in automatic suffix change. Suffix will be cleared out if you uncheck this option or delete the entered text.


0.1.1 (2019-07-21)
---------------------

* From now on if source file or source directory has been already selected target directory will be set base on path from selected source file or base on path from first file from selected source directory if you use option "set source directory as target directory".
* Typo in tooltip for "Open" button to open target directory fixed.
* Naming convention changed everywhere from "conversion" to "analysis".


0.1.0 (2019-06-23)
---------------------

* Initial release