################
Settings details
################

Settings are divided into two tabs, separately for source files and target files, as follows.

************
Source files
************

Here are the options available for source files:

All report types:
    - ``add debug data`` - turn on this option to get additional columns for selected report type like source file name with path, policy name and more.

        ..  note::
            Text in debug's columns headers is in blue color in the target file to let you quickly distinguish them from default columns.

        .. seealso::
            Check :doc:`nfa-target-file/index` descriptions to get more details.

Vulnerability report type:
    - ``filter out None results`` - turn on this option to automatically filter out plugins results with None Risk Factor and see in the target file only these which Risk Factor is equal to Low, Medium, High or Critical. 
        
        .. note::
            Plugins results with None Risk Factor are not removed from target file, to see them use filter option in column named *Risk Factor*.
    
    - ``skip None results`` - turn on this option to completely skip plugins results with None Risk Factor and left in the target file only these which Risk Factor is equal to Low, Medium, High or Critical.
    
        .. note::
            To see plugins results with None Risk Factor in target file you need to disable this option and analyse selected files again.

************
Target files
************

Here are the options available for target files:

- ``Change`` button - click to change target directory and use it for generated output files.

    .. note::
        ``Change`` button is placed next to target directory field.

- ``set source directory as target directory`` turn on this option to automatically change target directory each time when you select new source file/-s and set target directory to be the same as source file/-s directory. 
    
    .. note::
        If you use *Open directory* option to open source files this directory will be taken as target directory for all files including these from subdirectories.

- ``add suffix with "_YYYYMMDD_HHMMSS"`` - turn on this option to add suffix into target filename with date and time in format ``_YYYYMMDD_HHMMSS``. 

    .. note::
        Take a look below this option to see example target filename received that way.

        If you already turned on ``add custom suffix`` option, turn it off and on again to change the sequence of these two options in target file name.

- ``add custom suffix`` - turn on this option if you want to add suffix into target filename which will contain text taken from field placed on the right side from this option. 
    
    .. note:: 
        Take a look below this option to see target filename example received that way.

        If you already turned on ``add suffix with "_YYYYMMDD_HHMMSS"`` option, turn it off and on again to change the sequence of these two options in target file name.
