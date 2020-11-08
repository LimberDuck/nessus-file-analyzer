############
Scan section
############

Here you will find all details about data visible in target file in *Scan* section.

    .. list-table:: Column details explanation
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Column name.

        * - Description
          - Short description for particular data.

        * - Source
          - Information about exact source from where data is being taken.

        * - Post-processing
          - Information how the gathered data is processed, if post-processed at all.

        * - Column type
          - 
            ``default`` - column always appears in report.
                
            ``debug`` - column appears in report only if ``add debug data`` option has been enabled.

.. note::
    Some of the columns are visible only if you use ``add debug data`` option for analysis (see :doc:`../nfa-settings` to adhere more information about this option). 
    For all of these columns you will find below information **Column type** : ``debug``.


****************
Nessus scan name
****************

    .. list-table:: Nessus scan name - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Nessus scan name

        * - Description
          - Scan name given by user during scan setting up.

        * - Source
          - nessus file > ``Report/name``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``

****************
Nessus file name
****************

    .. list-table:: Nessus file name - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Nessus file name

        * - Description
          - Nessus file name assigned during the file downloading.

        * - Source
          - nessus file

        * - Post-processing
          - Absolute path of the given file.

        * - Column type
          - ``debug``

****************
nessus file size
****************

    .. list-table:: nessus file size - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - nessus file size

        * - Description
          - Nessus file size in human readable format, e.g. b, B, KiB, MiB, GiB.

        * - Source
          - nessus file

        * - Post-processing
          - Converting from bytes to human readable format.

        * - Column type
          - ``debug``

.. _target-hosts:

************
Target hosts
************

    .. list-table:: Target hosts - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Target hosts

        * - Description
          - Number of target hosts given by user during scan setting up.

        * - Source
          - nessus file > ``Preferences/ServerPreferences/preference/[name='TARGET']/value``

        * - Post-processing
          -
            1. Value split by comma ``,``.
            2. Text changed to lowercase.
            3. If nessus file comes from Tenable.sc string ``[ip]`` is removed from corresponding target.
            4. If nessus file comes from Tenable.sc IP ranges in corresponding target is converted into separate IP addresses.

        * - Column type
          - ``debug``, ``default``

*********************************
Target hosts (without duplicates)
*********************************

    .. list-table:: Target hosts (without duplicates) - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Target hosts (without duplicates)

        * - Description
          - Number of distinct values from the list of target hosts.

        * - Source
          - nessus file > ``Preferences/ServerPreferences/preference/[name='TARGET']/value``

        * - Post-processing
          - The same as for :ref:`target-hosts`

        * - Column type
          - ``debug``, ``default``

*************
Scanned hosts
*************

    .. list-table:: Scanned hosts - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Scanned hosts

        * - Description
          - Number of all ReportHost items listed in provided nessus file.

        * - Source
          - nessus file > ``ReportHost``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

**************************************
Scanned hosts with credentialed checks
**************************************

    .. list-table:: Scanned hosts with credentialed checks - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Scanned hosts with credentialed checks

        * - Description
          - Number of all ReportHost items listed in provided nessus file where Plugin ID 10506 "Nessus Scan Information" output contains ``Credentialed checks : yes``.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="19506"]/plugin_output``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/19506

*****************
Unreachable hosts
*****************

    .. list-table:: Unreachable hosts - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Unreachable hosts

        * - Description
          - Number of target hosts left after subtracting of scanned hosts list from target hosts list.

        * - Source
          - nessus file > ``Preferences/ServerPreferences/preference/[name='TARGET']/value`` - ``ReportHost``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

************
Scan started
************

    .. list-table:: Scan started - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Scan started

        * - Description
          - Exact date and time when scan of the first host has been initiated.

        * - Source
          - nessus file > ``ReportHost/HostProperties/tag/[@name='HOST_START']``

        * - Post-processing
          - Date and time returned in format ``%a %b %d %H:%M:%S %Y``.

        * - Column type
          - ``debug``, ``default``

**********
Scan ended
**********

    .. list-table:: Scan ended - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Scan ended

        * - Description
          - Exact date and time when scan of the last host has been ended.

        * - Source
          - nessus file > ``ReportHost/HostProperties/tag/[@name='HOST_END']``

        * - Post-processing
          - Date and time returned in format ``%a %b %d %H:%M:%S %Y``.

        * - Column type
          - ``debug``, ``default``

*********************
Elapsed time per scan
*********************

    .. list-table:: Elapsed time per scan - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Elapsed time per scan

        * - Description
          - Duration of the entire scan, based on subtraction Scan Start Time of first host scanned from Scan End Time of last host scanned.

        * - Source
          - nessus file > ``ReportHost/HostProperties/tag/[@name='HOST_END']`` - ``ReportHost/HostProperties/tag/[@name='HOST_START']``

        * - Post-processing
          - Elapsed time returned in format ``HH:MM:SS``.

        * - Column type
          - ``debug``, ``default``

***********
Policy name
***********

    .. list-table:: Policy name - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Policy name

        * - Description
          - Policy name selected by user during scan setting up.

        * - Source
          - nessus file > ``Policy/policyName``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``

**********
Login used
**********

    .. list-table:: Login used - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Login used

        * - Description
          - Login name used during scan of reported host.

        * - Source
          - 
            nessus file > ``ReportHost/HostProperties/tag/[@name='login-used']``
            
        * - Post-processing
          - 
            *none*

        * - Column type
          - ``debug``, ``default``

******
DB SID
******

    .. list-table:: DB SID - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - DB SID

        * - Description
          - Database SID set by user during scan setting up.

        * - Source
          - nessus file > ``Preferences/PluginsPreferences/item/[fullName='Database settings[entry]:Database SID :']/selectedValue``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

*******
DB port
*******

    .. list-table:: DB port - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - DB port

        * - Description
          - Database port set by user during scan setting up.

        * - Source
          - nessus file > ``Preferences/PluginsPreferences/item/[fullName='Database settings[entry]:Database port to use :']/selectedValue``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

**************
Reverse lookup
**************

    .. list-table:: Reverse lookup - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Reverse lookup

        * - Description
          - Information if option *Settings > Report > Output > 'Designate hosts by their DNS name'* has been turned on in policy used during scan.

        * - Source
          - nessus file > ``Preferences/ServerPreferences/preference/[name='reverse_lookup']/value``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``

*********
Max hosts
*********

    .. list-table:: Max hosts - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Max hosts

        * - Description
          - Value set for Max simultaneous hosts per scan in policy used during scan.

        * - Source
          - nessus file > ``Preferences/ServerPreferences/preference/[name='max_hosts']/value``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``

**********
Max checks
**********

    .. list-table:: Max checks - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Max checks

        * - Description
          - Value set for Max simultaneous checks per host in policy used during scan.

        * - Source
          - nessus file > ``Preferences/ServerPreferences/preference/[name='max_checks']/value``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``

***************
Network timeout
***************

    .. list-table:: Network timeout - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Network timeout

        * - Description
          - Value set for Network timeout (in seconds) in policy used during scan.

        * - Source
          - nessus file > ``Preferences/ServerPreferences/preference/[name='checks_read_timeout']/value``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``

************
Used plugins
************

    .. list-table:: Used plugins - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Used plugins

        * - Description
          - Number of all plugins used during scans.

        * - Source
          - nessus file > ``Preferences/ServerPreferences/preference/[name='plugin_set']/value``

        * - Post-processing
          - Value split by semicolon ``;``.

        * - Column type
          - ``debug``

***********
ALL plugins
***********

    .. list-table:: ALL plugins - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - ALL plugins

        * - Description
          - Number of reported plugins for all hosts in scan.

        * - Source
          - nessus files > ``ReportHost/ReportItem``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

****************
Critical plugins
****************

    .. list-table:: Critical plugins - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Critical plugins

        * - Description
          - Number of reported plugins for all hosts in scan with Critical Risk Factor.

        * - Source
          - nessus file > ``ReportHost/ReportItem/risk_factor/"Critical"``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

************
High plugins
************

    .. list-table:: High plugins - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - High plugins

        * - Description
          - Number of reported plugins for all hosts in scan with High Risk Factor.

        * - Source
          - nessus file > ``ReportHost/ReportItem/risk_factor/"High"``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

**************
Medium plugins
**************

    .. list-table:: Medium plugins - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Medium plugins

        * - Description
          - Number of reported plugins for all hosts in scan with Medium Risk Factor.

        * - Source
          - nessus file > ``ReportHost/ReportItem/risk_factor/"Medium"``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

***********
Low plugins
***********

    .. list-table:: Low plugins - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Low plugins

        * - Description
          - Number of reported plugins for all hosts in scan with Low Risk Factor.

        * - Source
          - nessus file > ``ReportHost/ReportItem/risk_factor/"Low"``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

************
None plugins
************

    .. list-table:: None plugins - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - *none* plugins

        * - Description
          - Number of reported plugins for all hosts in scan with None Risk Factor.

        * - Source
          - nessus file > ``ReportHost/ReportItem/risk_factor/"None"``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

**************
ALL compliance
**************

    .. list-table:: ALL compliance - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - ALL compliance

        * - Description
          - Number of reported compliance plugins for all hosts in scan.

        * - Source
          - nessus file > ``ReportHost/ReportItem/compliance/"True"``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

*****************
Passed compliance
*****************

    .. list-table:: Passed compliance - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Passed compliance

        * - Description
          - Number of reported compliance plugins for all hosts in scan with PASSED compliance result.

        * - Source
          - nessus file > ``ReportHost/ReportItem/"cm:compliance-result", namespaces={'cm': 'http://www.nessus.org/cm'}/"PASSED"``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

*****************
Failed compliance
*****************

    .. list-table:: Failed compliance - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Failed compliance

        * - Description
          - Number of reported compliance plugins for all hosts in scan with FAILED compliance result.

        * - Source
          - nessus file > ``ReportHost/ReportItem/"cm:compliance-result", namespaces={'cm': 'http://www.nessus.org/cm'}/"FAILED"``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

******************
Warning compliance
******************

    .. list-table:: Warning compliance - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Warning compliance

        * - Description
          - Number of reported compliance plugins for all hosts in scan with WARNING compliance result.

        * - Source
          - nessus file > ``ReportHost/ReportItem/"cm:compliance-result", namespaces={'cm': 'http://www.nessus.org/cm'}/"WARNING"``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``
