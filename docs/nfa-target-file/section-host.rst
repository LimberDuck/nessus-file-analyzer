############
Host section
############

Here you will find all details about data visible in target file in *Host* section.

    .. list-table:: Column details explanation
        :widths: 20 80
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


*****************
Nessus scanner IP
*****************

    .. list-table:: Nessus scanner IP - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - Nessus scanner IP

        * - Description
          - Scanner IP used during scan of reported host based on Plugin ID 19506 output.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="19506"]/plugin_output``

        * - Post-processing
          - 
            1. If Plugin ID 19506 output exist extract Scanner IP from output line with ``Scanner IP :``
            2. If Plugin ID 19506 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``

.. seealso::
    Read more about plugin which source for this column on Tenable website https://www.tenable.com/plugins/nessus/19506

****************
Nessus scan name
****************

    .. list-table:: Nessus scan name - column details
        :widths: 20 80
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
        :widths: 20 80
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

******
Target
******

    .. list-table:: Target - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - Target

        * - Description
          - Name of reported host. This can be either |IP| or |FQDN|, depending on this what has been given as target.

        * - Source
          - 
            nessus file > ``ReportHost/[@name='name']``

            nessus file > ``Preferences/ServerPreferences/preference/[name='TARGET']/value``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

********
Hostname
********

    .. list-table:: Hostname - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - Hostname

        * - Description
          - Hostname of reported host.

        * - Source
          - nessus file > ``ReportHost/HostProperties/tag/[@name='hostname']``

        * - Post-processing
          - 
            1. Value changed to lowercase.
            2. If hostname field contains |FQDN| only hostname will be returned.

        * - Column type
          - ``debug``, ``default``

****
FQDN
****

    .. list-table:: FQDN - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - FQDN

        * - Description
          - |FQDN| of reported host.

        * - Source
          - nessus file > ``ReportHost/HostProperties/tag/[@name='host-fqdn']``

        * - Post-processing
          - Value changed to lowercase.

        * - Column type
          - ``debug``, ``default``

*********************
NetBIOS Computer name
*********************

    .. list-table:: NetBIOS Computer name - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - NetBIOS Computer name

        * - Description
          - NetBIOS Computer name of reported host.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="10150"]/plugin_output``

        * - Post-processing
          -
            1. If Plugin ID 10150 output exist extract computer name from output line with ``Computer name``
            2. Value changed to lowercase.
            3. If Plugin ID 10150 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``

.. seealso::
    Read more about plugin which source for this column on Tenable website https://www.tenable.com/plugins/nessus/10150

*********************
NetBIOS Domain name
*********************

    .. list-table:: NetBIOS Domain name - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - NetBIOS Domain name

        * - Description
          - NetBIOS Domain name of reported host.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="10150"]/plugin_output``

        * - Post-processing
          -
            1. If Plugin ID 10150 output exist extract domain name from output line with ``Workgroup / Domain name``
            2. Value changed to lowercase.
            3. If Plugin ID 10150 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``

.. seealso::
    Read more about plugin which source for this column on Tenable website https://www.tenable.com/plugins/nessus/10150

**
IP
**

    .. list-table:: IP - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - IP

        * - Description
          - |IP| of reported host.

        * - Source
          - nessus file > ``ReportHost/HostProperties/tag/[@name='host-ip']``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

*******
Scanned
*******

    .. list-table:: Scanned - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - Scanned

        * - Description
          - Information if target host has been scanned.
            
            - ``yes`` if target host is on the list of reported hosts.
            
            - ``no`` if target host is not on the list of reported hosts.

        * - Source
          - 
            nessus file > ``Preferences/ServerPreferences/preference/[name='TARGET']/value``

            nessus file > ``ReportHost/[@name='name']``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

*******************
Credentialed checks
*******************

    .. list-table:: Credentialed checks - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - Credentialed checks

        * - Description
          - Information if reported host has been scanned with credentialed checks.
            
        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="19506"]/plugin_output``

        * - Post-processing
          -
                1. If Plugin ID 19506 output exist extract ``yes`` or ``no`` from output line with ``Credentialed checks :``.
          
                2. If Plugin ID 19506 output does not exist return ``no``.

        * - Column type
          - ``debug``, ``default``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/19506

************
Scan started
************

    .. list-table:: Scan started - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - Scan started

        * - Description
          - Exact date and time when scan of the reported host has been initiated.

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
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - Scan ended

        * - Description
          - Exact date and time when scan of the reported host has been ended.

        * - Source
          - nessus file > ``ReportHost/HostProperties/tag/[@name='HOST_END']``

        * - Post-processing
          - Date and time returned in format ``%a %b %d %H:%M:%S %Y``.

        * - Column type
          - ``debug``, ``default``

*********************
Elapsed time per host
*********************

    .. list-table:: Elapsed time per host - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - Elapsed time per host

        * - Description
          - Duration of the particular host scanned based on subtraction Scan Start Time from Scan End Time.

        * - Source
          - nessus file > ``ReportHost/HostProperties/tag/[@name='HOST_END']`` - ``ReportHost/HostProperties/tag/[@name='HOST_START']``

        * - Post-processing
          - Elapsed time returned in format ``HH:MM:SS``.

        * - Column type
          - ``debug``, ``default``

*********************
Elapsed time per scan
*********************

    .. list-table:: Elapsed time per scan - column details
        :widths: 20 80
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
        :widths: 20 80
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
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - Login used

        * - Description
          - Login name used during scan of reported host.

        * - Source
          - 
            nessus file > ``ReportHost/HostProperties/tag/[@name='login-used']``
            
            nessus file > ``Preferences/PluginsPreferences/item/[fullName='VMware vCenter SOAP API Settings[entry]:VMware vCenter user name :']/selectedValue``
            
            nessus file > ``Preferences/PluginsPreferences/item/[fullName='Database settings[entry]:Login :']/selectedValue``
            
            nessus file > ``Preferences/PluginsPreferences/item/[fullName='Login configurations[entry]:SMB account :']/selectedValue``
            
            nessus file > ``Preferences/PluginsPreferences/item/[fullName='SSH settings[entry]:SSH user name :']/selectedValue``
            
            nessus file > ``Preferences/PluginsPreferences/item/[fullName='Login configurations[entry]:SMB domain (optional) :']/selectedValue``

        * - Post-processing
          - 
            For ``Preferences/PluginsPreferences/item/[fullName='Login configurations[entry]:SMB account :']/selectedValue``
            
            information about domain is added ``Preferences/PluginsPreferences/item/[fullName='Login configurations[entry]:SMB domain (optional) :']/selectedValue``
        
        * - Column type
          - ``debug``, ``default``

******
DB SID
******

    .. list-table:: DB SID - column details
        :widths: 20 80
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
        :widths: 20 80
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
        :widths: 20 80
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
        :widths: 20 80
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
        :widths: 20 80
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
        :widths: 20 80
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

****************
Operating System
****************

    .. list-table:: Operating System - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - Operating System

        * - Description
          - Information about Operating System of reported host.

        * - Source
          - nessus file > ``ReportHost/HostProperties/tag/[@name='operating-system']``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

***********
ALL plugins
***********

    .. list-table:: ALL plugins - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - ALL plugins

        * - Description
          - Number of reported plugins for particular reported host.

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
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - Critical plugins

        * - Description
          - Number of reported plugins for particular reported host with Critical Risk Factor.

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
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - High plugins

        * - Description
          - Number of reported plugins for particular reported host in scan with High Risk Factor.

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
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - Medium plugins

        * - Description
          - Number of reported plugins for particular reported host in scan with Medium Risk Factor.

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
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - Low plugins

        * - Description
          - Number of reported plugins for particular reported host in scan with Low Risk Factor.

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
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - *none* plugins

        * - Description
          - Number of reported plugins for particular reported host in scan with None Risk Factor.

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
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - ALL compliance

        * - Description
          - Number of reported compliance checks for particular reported host in scan.

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
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - Passed compliance

        * - Description
          - Number of reported compliance checks for particular reported host in scan with PASSED compliance result.

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
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - Failed compliance

        * - Description
          - Number of reported compliance checks for particular reported host in scan with FAILED compliance result.

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
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - Warning compliance

        * - Description
          - Number of reported compliance checks for particular reported host in scan with WARNING compliance result.

        * - Source
          - nessus file > ``ReportHost/ReportItem/"cm:compliance-result", namespaces={'cm': 'http://www.nessus.org/cm'}/"WARNING"``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

**************************
10180: Ping to remote host
**************************

    .. list-table:: 10180: Ping to remote host - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - 10180: Ping to remote host

        * - Description
          - Plugin ID 10180 output.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="10180"]/plugin_output``

        * - Post-processing
          -
            1. If Plugin ID 10180 output exist return it **in unchanged form**.
            2. If Plugin ID 10180 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/10180

*****************************
10287: Traceroute Information
*****************************

    .. list-table:: 10287: Traceroute Information - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - 10287: Traceroute Information

        * - Description
          - Plugin ID 10287 output.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="10287"]/plugin_output``

        * - Post-processing
          -
            1. If Plugin ID 10287 output exist return it **in unchanged form**.
            2. If Plugin ID 10287 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/10287

************************
11936: OS Identification
************************

    .. list-table:: 11936: OS Identification - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - 11936: OS Identification

        * - Description
          - Plugin ID 11936 output.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="11936"]/plugin_output``

        * - Post-processing
          -
            1. If Plugin ID 11936 output exist return it **in unchanged form**.
            2. If Plugin ID 11936 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/11936

****************************************
45590: Common Platform Enumeration (CPE)
****************************************

    .. list-table:: 45590: Common Platform Enumeration (CPE) - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - 45590: Common Platform Enumeration (CPE)

        * - Description
          - Plugin ID 45590 output.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="45590"]/plugin_output``

        * - Post-processing
          -
            1. If Plugin ID 45590 output exist return it **in unchanged form**.
            2. If Plugin ID 45590 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/45590

******************
54615: Device Type
******************

    .. list-table:: 54615: Device Type - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - 54615: Device Type

        * - Description
          - Plugin ID 54615 output.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="54615"]/plugin_output``

        * - Post-processing
          -
            1. If Plugin ID 54615 output exist return it **in unchanged form**.
            2. If Plugin ID 54615 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/54615

****************************************************
21745: Authentication Failure - Local Checks Not Run
****************************************************

    .. list-table:: 21745: Authentication Failure - Local Checks Not Run - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - 21745: Authentication Failure - Local Checks Not Run

        * - Description
          - Plugin ID 21745 output.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="21745"]/plugin_output``

        * - Post-processing
          -
            1. If Plugin ID 21745 output exist return it **in unchanged form**.
            2. If Plugin ID 21745 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/21745

**********************************************************************
12634: Authenticated Check : OS Name and Installed Package Enumeration
**********************************************************************

    .. list-table:: 12634: Authenticated Check : OS Name and Installed Package Enumeration - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - 12634: Authenticated Check : OS Name and Installed Package Enumeration

        * - Description
          - Plugin ID 12634 output.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="12634"]/plugin_output``

        * - Post-processing
          -
            1. If Plugin ID 12634 output exist return it **in unchanged form**.
            2. If Plugin ID 12634 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/12634

**************************************************
110385: Authentication Success Insufficient Access
**************************************************

    .. list-table:: 110385: Authentication Success Insufficient Access - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - 110385: Authentication Success Insufficient Access

        * - Description
          - Plugin ID 110385 output.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="110385"]/plugin_output``

        * - Post-processing
          -
            1. If Plugin ID 110385 output exist return it **in unchanged form**.
            2. If Plugin ID 110385 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/110385

*************************************************
102094: SSH Commands Require Privilege Escalation
*************************************************

    .. list-table:: 102094: SSH Commands Require Privilege Escalation - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - 102094: SSH Commands Require Privilege Escalation

        * - Description
          - Plugin ID 102094 output.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="102094"]/plugin_output``

        * - Post-processing
          -
            1. If Plugin ID 102094 output exist return it **in unchanged form**.
            2. If Plugin ID 102094 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``, ``default``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/102094

********************************************
10394: Microsoft Windows SMB Log In Possible
********************************************

    .. list-table:: 10394: Microsoft Windows SMB Log In Possible - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - 10394: Microsoft Windows SMB Log In Possible

        * - Description
          - Plugin ID 10394 output.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="10394"]/plugin_output``

        * - Post-processing
          -
            1. If Plugin ID 10394 output exist return it **in unchanged form**.
            2. If Plugin ID 10394 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/10394

**************************************************************
24786: Nessus Windows Scan Not Performed with Admin Privileges
**************************************************************

    .. list-table:: 24786: Nessus Windows Scan Not Performed with Admin Privileges - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - 24786: Nessus Windows Scan Not Performed with Admin Privileges

        * - Description
          - Plugin ID 24786 output.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="24786"]/plugin_output``

        * - Post-processing
          -
            1. If Plugin ID 24786 output exist return it **in unchanged form**.
            2. If Plugin ID 24786 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/24786

*********************************************************
24269: Windows Management Instrumentation (WMI) Available
*********************************************************

    .. list-table:: 24269: Windows Management Instrumentation (WMI) Available - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - 24269: Windows Management Instrumentation (WMI) Available

        * - Description
          - Plugin ID 24269 output.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="24269"]/plugin_output``

        * - Post-processing
          -
            1. If Plugin ID 24269 output exist return it **in unchanged form**.
            2. If Plugin ID 24269 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/24269

**********************************************
11011: Microsoft Windows SMB Service Detection
**********************************************

    .. list-table:: 11011: Microsoft Windows SMB Service Detection - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - 11011: Microsoft Windows SMB Service Detection

        * - Description
          - All occurrences of Plugin ID 11011 output.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="11011"]/plugin_output``

        * - Post-processing
          -
            1. If Plugin ID 11011 output exist return it **in unchanged form**.
            2. If more than one Plugin ID 11011 outputs exist, concatenate their **unchanged form** and return as one.
            3. If Plugin ID 11011 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/11011

*********************************************************
10400: Microsoft Windows SMB Registry Remotely Accessible
*********************************************************

    .. list-table:: 10400: Microsoft Windows SMB Registry Remotely Accessible - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - 10400: Microsoft Windows SMB Registry Remotely Accessible

        * - Description
          - Plugin ID 10400 output.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="10400"]/plugin_output``

        * - Post-processing
          -
            1. If Plugin ID 10400 output exist return it **in unchanged form**.
            2. If Plugin ID 10400 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/10400

*********************************************************************************
26917: Microsoft Windows SMB Registry : Nessus Cannot Access the Windows Registry
*********************************************************************************

    .. list-table:: 26917: Microsoft Windows SMB Registry : Nessus Cannot Access the Windows Registry - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - 26917: Microsoft Windows SMB Registry : Nessus Cannot Access the Windows Registry

        * - Description
          - Plugin ID 26917 output.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="26917"]/plugin_output``

        * - Post-processing
          -
            1. If Plugin ID 26917 output exist return it **in unchanged form**.
            2. If Plugin ID 26917 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/26917

**********************************************************************
42897: SMB Registry : Start the Registry Service during the scan (WMI)
**********************************************************************

    .. list-table:: 42897: SMB Registry : Start the Registry Service during the scan (WMI) - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - 42897: SMB Registry : Start the Registry Service during the scan (WMI)

        * - Description
          - Plugin ID 42897 output.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="42897"]/plugin_output``

        * - Post-processing
          -
            1. If Plugin ID 42897 output exist return it **in unchanged form**.
            2. If Plugin ID 42897 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/42897

****************************************************************************
20811: Microsoft Windows Installed Software Enumeration (credentialed check)
****************************************************************************

    .. list-table:: 20811: Microsoft Windows Installed Software Enumeration (credentialed check) - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - 20811: Microsoft Windows Installed Software Enumeration (credentialed check)

        * - Description
          - Plugin ID 20811 output.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="20811"]/plugin_output``

        * - Post-processing
          -
            1. If Plugin ID 20811 output exist return it **in unchanged form**.
            2. If Plugin ID 20811 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/20811

*******************************
91825: Oracle DB Login Possible
*******************************

    .. list-table:: 91825: Oracle DB Login Possible - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - 91825: Oracle DB Login Possible

        * - Description
          - Plugin ID 91825 output.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="91825"]/plugin_output``

        * - Post-processing
          -
            1. If Plugin ID 91825 output exist return it **in unchanged form**.
            2. If Plugin ID 91825 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/91825

******************************************
91827: Microsoft SQL Server Login Possible
******************************************

    .. list-table:: 91827: Microsoft SQL Server Login Possible - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - 91827: Microsoft SQL Server Login Possible

        * - Description
          - Plugin ID 91827 output.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="91827"]/plugin_output``

        * - Post-processing
          -
            1. If Plugin ID 91827 output exist return it **in unchanged form**.
            2. If Plugin ID 91827 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/91827

************************
47864: Cisco IOS Version
************************

    .. list-table:: 47864: Cisco IOS Version - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - 47864: Cisco IOS Version

        * - Description
          - Plugin ID 47864 output.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="47864"]/plugin_output``

        * - Post-processing
          -
            1. If Plugin ID 47864 output exist return it **in unchanged form**.
            2. If Plugin ID 47864 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/47864

***************************
67217: Cisco IOS XE Version
***************************

    .. list-table:: 67217: Cisco IOS XE Version - column details
        :widths: 20 80
        :stub-columns: 1

        * - Header name
          - 67217: Cisco IOS XE Version

        * - Description
          - Plugin ID 67217 output.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[pluginID="67217"]/plugin_output``

        * - Post-processing
          -
            1. If Plugin ID 67217 output exist return it **in unchanged form**.
            2. If Plugin ID 67217 output does not exist return:
                - ``No output recorded.`` - if plugin appeared in the report but does no return any output,
                - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
                - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

        * - Column type
          - ``debug``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/67217

