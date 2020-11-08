###############
Getting started
###############

.. mermaid::
    :caption: Simple nessus file analyzer's end-user path

    sequenceDiagram
        autonumber
        participant end_user as End User
        participant nfa as nessus file analyzer

        end_user->>nfa: Provide nessus files.

        end_user->>nfa: Select report\-s type.

        end_user-->>nfa: Customize settings.

        end_user->>+nfa: Initialize analyze.
        
        nfa->>-end_user: Return target file. 


************************
Run nessus file analyzer
************************

Run |nfa| using python or prepare executable file as described in :doc:`nfa-installation`.

*****************
Open nessus files
*****************

You have five possibilities to open your nessus files in |nfa|, here they are.

**OPTION 1** - by opening file\\-s

    1. Open |nfa|.
    2. Go to Menu *File*.
    3. Choose *Open file\\-s* if you want to open one or more nessus files at once.

**OPTION 2** - by opening directory

    1. Open |nfa|.
    2. Go to Menu *File*.
    3. Choose *Open directory* if you want to open all nessus files from selected directory and its subdirectories.

**OPTION 3** - by use of OS contextual menu

    1. On |OS| level select one or more nessus files in your |OS| file browser.
    2. Click |RMB| on selected file\\-s and choose from contextual menu option *Open with...*.
    3. Choose |nfa| to open selected file\\-s.

**OPTION 4** - by file\\-s Drag & Drop

    1. On |OS| level select one or more nessus files in your |OS| file browser.
    2. Simple drag and drop selected file\\-s on |nfa| window.

**OPTION 5** - by directory Drag & Drop

    1. On |OS| level select one or more directories containing nessus files in your |OS| file browser. 
    2. Simple drag and drop selected directory or directories on |nfa| window.

******************
Select report type
******************

Select one or more report types: scan, host, vulnerabilities, noncompliance.

1. Select report type:
    - ``scan`` - if you want to see sum-up from point of view of the whole scan. 
        
        .. seealso::
            Check :doc:`nfa-target-file/section-scan` description to get more details.

    - ``host`` - if you want to see sum-up from point of view of particular scanned host. 
    
        .. seealso::
            Check :doc:`nfa-target-file/section-host` description to get more details.

    - ``vulnerabilities`` - if you want to see list of vulnerabilities reported in this scan for all scanned hosts. 
    
        .. seealso::
            Check :doc:`nfa-target-file/section-vulnerabilities` description to get more details.

    - ``noncompliance`` - if you want to see list of noncompliance reported in this scan for all scanned hosts. 
    
        .. seealso::
            Check :doc:`nfa-target-file/section-noncompliance` description to get more details.

2. Play with |nfa| settings to fit target file to your exact needs.

    .. seealso::
        Check :doc:`nfa-settings` to get more details.

******************
Initialize analyze
******************

Click ``Start`` button to initiate analyze of all provided nessus files.

****************
Open target file
****************

Click ``Open`` button to open target directory where output file has been saved.
