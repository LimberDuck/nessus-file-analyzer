#########################
Installation instructions
#########################

.. note::

    It's advisable to use python virtual environment for below instructions. Read more about python virtual environment in `The Hitchhiker’s Guide to Python! <https://docs.python-guide.org/dev/virtualenvs/>`_
    
    Read about `virtualenvwrapper in The Hitchhiker’s Guide to Python! <https://docs.python-guide.org/dev/virtualenvs/#virtualenvwrapper>`_: `virtualenvwrapper <https://virtualenvwrapper.readthedocs.io>`_ provides a set of commands which makes working with virtual environments much more pleasant.

*******
Windows
*******

1. If you don't have, install Python 3.6.0 or higher, you can download it via https://www.python.org/downloads
2. If you don't have, install latest version of Git, you can download it via https://git-scm.com/downloads
3. Clone |nfa| repository using below command in Git Bash:

    .. code-block:: bash

        git clone https://github.com/LimberDuck/nessus-file-analyzer.git

4. Install requirements using below command

    .. code-block:: bash

        pip install -r .\requirements.txt

5. Run |nfa| using below command

    .. code-block:: bash

        python nfa.py

6. Upgrade setuptools using below command

    .. code-block:: bash

        pip install --upgrade setuptools

7. Install PyInstaller

    .. code-block:: bash

        pip install PyInstaller

8. Build your own executable file using below command

    .. code-block:: bash

        pyinstaller --onefile --windowed --version-file=.\version.rc --icon=.\icons\LimberDuck-nessus-file-analyzer.ico nfa.py

9. Go to dist catalog to find executable file *nfa.exe*

**************
Linux (Ubuntu)
**************

1. Python 3.6.7 should be already installed in Ubuntu 18.04.1 LTS, you can ensure with below command

    .. code-block:: bash

        python3 --version

2. If you don't have, install git using below command

    .. code-block:: bash

        sudo apt install git

3. Clone |nfa| repository using below command

    .. code-block:: bash

        git clone https://github.com/LimberDuck/nessus-file-analyzer.git

4. If you don't have, install pip using below command

    .. code-block:: bash

        sudo apt install python3-pip

5. Install requirements using below command

    .. code-block:: bash

        pip3 install -r .\requirements.txt

6. Run |nfa| using below command

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

*****
MacOS
*****

1. If you don't have, install Python 3.6.0 or higher, you can download it via https://www.python.org/downloads

2. Clone |nfa| repository using below command

    .. code-block:: bash

        git clone https://github.com/LimberDuck/nessus-file-analyzer.git

3. Install requirements using below command

    .. code-block:: bash

        pip3.6 install -r .\requirements.txt

4. Run |nfa| using below command

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
