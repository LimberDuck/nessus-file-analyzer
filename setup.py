import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

about = {}
with open("nessus_file_analyzer/_version.py") as f:
    exec(f.read(), about)

setuptools.setup(
    name="nessus_file_analyzer",
    version=about["__version__"],
    license="LGPLv3",
    author="Damian Krawczyk",
    author_email="damian.krawczyk@limberduck.org",
    description="nessus file analyzer by LimberDuck is a GUI tool which enables you to parse nessus scan files from "
                "Nessus and Tenable.SC by (C) Tenable, Inc. and exports results to a Microsoft Excel Workbook for "
                "effortless analysis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LimberDuck/nessus-file-analyzer",
    packages=setuptools.find_packages(),
    install_requires=required,
    entry_points={
        "gui_scripts": [
            "nessus-file-analyzer = nessus_file_analyzer.__main__:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: X11 Applications :: Qt",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
    ],
)
