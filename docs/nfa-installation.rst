#########################
Installation instructions
#########################

.. note::

    It's advisable to use python virtual environment for below instructions. Read more about python virtual environment in `The Hitchhiker’s Guide to Python! <https://docs.python-guide.org/dev/virtualenvs/>`_
    
    Read about `virtualenvwrapper in The Hitchhiker’s Guide to Python! <https://docs.python-guide.org/dev/virtualenvs/#virtualenvwrapper>`_: `virtualenvwrapper <https://virtualenvwrapper.readthedocs.io>`_ provides a set of commands which makes working with virtual environments much more pleasant.

************
Installation
************

1. Install **nessus file analyzer**
    
   ``pip install nessus-file-analyzer``

   .. note::
       
       To upgrade to newer version run:

       ``pip install -U nessus-file-analyzer``

2. Run **nessus file analyzer**

   ``nessus-file-analyzer``
   
   .. tip::
        
        Optionally for Linux and macOS:
        
        ``nessus-file-analyzer&``
        
        Run with ``&`` at the end to start the process in the background.

3. Make a shortcut for **nessus file analyzer**

   **Windows:**
   
   - Run in cmd ``where nessus-file-analyzer.exe``
   - Copy returned path.
   - Go to e.g. to Desktop.
   - Right click on Desktop and choose ``New > Shortcut``.
   - Paste returned path.
   - Click ``Next``, ``Finish``.
   
   **Linux (Ubuntu) / macOS**

   - Run in Terminal ``which nessus-file-analyzer``
   - Run in Terminal ``ln -s path_returned_in_previous_command ~/Desktop/``

   **macOS**

   - Run in Terminal ``which nessus-file-analyzer``
   - Open ``bin`` folder where ``nessus-file-analyzer`` is located.
   - Right click on ``nessus-file-analyzer`` and choose ``Make alias``.
   - Move your alias e.g. to Desktop.


Additional steps
****************

Linux (Ubuntu)
==============

If you installed without python virtual environment, and you see below error:

.. code-block:: shell

    ~$ nessus-file-analyzer
    nessus-file-analyzer: command not found


Add below to ``~/.bashrc``

.. code-block:: shell

    # set PATH so it includes user's private ~/.local/bin if it exists
    if [ -d "$HOME/.local/bin" ] ; then
        PATH="$HOME/.local/bin:$PATH"
    fi

If you see below error:

.. code-block:: shell

    ~$ nessus-file-analyzer
    qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
    This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

    Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx, webgl, xcb.

    Aborted (core dumped)


Run below to fix the error:

.. code-block:: shell

    sudo apt-get install --reinstall libxcb-xinerama0




*********************
Build executable file
*********************

Windows
*******

1. Clone **nessus file analyzer** repository using below command in Git Bash:

    .. code-block:: none

        git clone https://github.com/LimberDuck/nessus-file-analyzer.git

2. Install requirements using below command

    .. code-block:: none

        pip install -r .\requirements.txt

3. Run **nessus file analyzer** using below command

    .. code-block:: none

        python -m nessus_file_analyzer

4. Upgrade setuptools using below command

    .. code-block:: none

        pip install --upgrade setuptools

5. Install PyInstaller

    .. code-block:: none

        pip install PyInstaller

6. Build your own executable file using below command

    .. code-block:: none

        pyinstaller --onefile --windowed --version-file=.\version.rc --icon=.\icons\LimberDuck-nessus-file-analyzer.ico  --name nessus-file-analyzer nessus_file_analyzer\__main__.py

7. Go to ``dist`` catalog to find executable file ``nessus-file-analyzer.exe``


Linux (Ubuntu)
**************

1. Clone **nessus file analyzer** repository using below command

    .. code-block:: bash

        git clone https://github.com/LimberDuck/nessus-file-analyzer.git

2. Install requirements using below command

    .. code-block:: bash

        pip install -r ./requirements.txt

3. Run **nessus file analyzer** using below command

    .. code-block:: bash

        python -m nessus_file_analyzer

4. Upgrade setuptools using below command

    .. code-block:: bash

        pip install --upgrade setuptools

5. Install PyInstaller

    .. code-block:: bash

        pip install PyInstaller

6. Build your own executable file using below command

    .. code-block:: bash

        ~/.local/bin/pyinstaller --onefile --windowed --icon=./icons/LimberDuck-nessus-file-analyzer.ico --name nessus-file-analyzer nessus_file_analyzer\__main__.py

7. Go to ``dist`` catalog to find executable file ``nessus-file-analyzer``.


macOS
*****

1. Clone **nessus file analyzer** repository using below command

    .. code-block:: bash

        git clone https://github.com/LimberDuck/nessus-file-analyzer.git

2. Install requirements using below command

    .. code-block:: bash

        pip3.6 install -r ./requirements.txt

3. Run **nessus file analyzer** using below command

    .. code-block:: bash

        python -m nessus_file_analyzer

4. Upgrade setuptools using below command

    .. code-block:: bash

        pip install --upgrade setuptools

5. Install PyInstaller

    .. code-block:: bash

        pip install PyInstaller

6. Build your own executable file using below command

    .. code-block:: bash
        
        pyinstaller --onefile --windowed --icon=./icons/LimberDuck-nessus-file-analyzer.ico --name nessus-file-analyzer nessus_file_analyzer\__main__.py

7. Go to ``dist`` catalog to find executable file ``nessus-file-analyzer``.
