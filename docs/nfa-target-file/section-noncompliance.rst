#####################
Noncompliance section
#####################

Here you will find all details about data visible in target file in *Noncompliance* section.

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


*****************
Nessus scanner IP
*****************

    .. list-table:: Nessus scanner IP - column details
        :widths: 10 90
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
          - absolute path of the given file

        * - Column type
          - ``debug``

******
Target
******

    .. list-table:: Target - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Target

        * - Description
          - Name of reported host. This can be either |IP| or |FQDN|, depending on this what has been given as target.

        * - Source
          - nessus file > ``ReportHost/[@name='name']``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

********
Hostname
********

    .. list-table:: Hostname - column details
        :widths: 10 90
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
        :widths: 10 90
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

**
IP
**

    .. list-table:: IP - column details
        :widths: 10 90
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
        :widths: 10 90
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
        :widths: 10 90
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

*********
Plugin ID
*********

    .. list-table:: Plugin ID - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Plugin ID

        * - Description
          - Exact Plugin ID returned by Nessus.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[@pluginID]``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

***********
Plugin name
***********

    .. list-table:: Plugin name - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Plugin name

        * - Description
          - Exact Plugin Name returned by Nessus.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[@pluginName]``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

***********
Plugin type
***********

    .. list-table:: Plugin type - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Plugin type

        * - Description
          - Exact Plugin type returned by Nessus.

        * - Source
          - nessus file > ``ReportHost/ReportItem/plugin_type``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

***********
Risk Factor
***********

    .. list-table:: Risk Factor - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Risk Factor

        * - Description
          - Exact Plugin Risk Factor returned by Nessus.

        * - Source
          - nessus file > ``ReportHost/ReportItem/risk_factor``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

*************
Plugin family
*************

    .. list-table:: Plugin family - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Plugin family

        * - Description
          - Exact Plugin Family returned by Nessus.

        * - Source
          - nessus file > ``ReportHost/ReportItem/[@pluginFamily]``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

**********************
Compliance plugin file
**********************

    .. list-table:: Compliance plugin file - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Compliance plugin file

        * - Description
          - Information if this is Compliance plugin.

        * - Source
          - nessus file > ``ReportHost/ReportItem/compliance/``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``

****************
Plugin file name
****************

    .. list-table:: Plugin file name - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Plugin file name

        * - Description
          - Exact Plugin file name returned by Nessus.

        * - Source
          - nessus file > ``ReportHost/ReportItem/fname``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``

**************
Plugin version
**************

    .. list-table:: Plugin version - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Plugin version

        * - Description
          - Exact Plugin version returned by Nessus.

        * - Source
          - nessus file > ``ReportHost/ReportItem/script_version``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

***********************
Plugin publication date
***********************

    .. list-table:: Plugin publication date - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Plugin publication date

        * - Description
          - Exact Plugin publication date returned by Nessus.

        * - Source
          - nessus file > ``ReportHost/ReportItem/plugin_publication_date``

        * - Post-processing
          - Return in format ``yyyy-mm-dd``.

        * - Column type
          - ``debug``, ``default``

************************
Plugin modification date
************************

    .. list-table:: Plugin modification date - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Plugin modification date

        * - Description
          - Exact Plugin modification date returned by Nessus.

        * - Source
          - nessus file > ``ReportHost/ReportItem/plugin_modification_date``

        * - Post-processing
          - Return in format ``yyyy-mm-dd``.

        * - Column type
          - ``debug``, ``default``

**********
Check name
**********

    .. list-table:: Check name - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Check name

        * - Description
          - Exact Compliance Check name returned by Nessus.

        * - Source
          - nessus file > ``ReportHost/ReportItem/"cm:compliance-check-name", namespaces={'cm': 'http://www.nessus.org/cm'}/``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

***************
Audit file name
***************

    .. list-table:: Audit file name - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Audit file name

        * - Description
          - Exact Compliance Audit file name returned by Nessus.

        * - Source
          - nessus file > ``ReportHost/ReportItem/"cm:compliance-audit-file", namespaces={'cm': 'http://www.nessus.org/cm'}/``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

********
Check ID
********

    .. list-table:: Check ID - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Check ID

        * - Description
          - Exact Compliance Check ID returned by Nessus.

        * - Source
          - nessus file > ``ReportHost/ReportItem/"cm:compliance-check-id", namespaces={'cm': 'http://www.nessus.org/cm'}/``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``

*************
Current value
*************

    .. list-table:: Current value - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Current value

        * - Description
          - Exact Compliance Check current value returned by Nessus.

        * - Source
          - nessus file > ``ReportHost/ReportItem/"cm:compliance-actual-value", namespaces={'cm': 'http://www.nessus.org/cm'}/``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

*****
Uname
*****

    .. list-table:: Uname - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Uname

        * - Description
          - Exact Compliance Check uname returned by Nessus.

        * - Source
          - nessus file > ``ReportHost/ReportItem/"cm:compliance-uname", namespaces={'cm': 'http://www.nessus.org/cm'}/``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``

***********
Description
***********

    .. list-table:: Description - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Description

        * - Description
          - Exact Compliance Check description returned by Nessus.

        * - Source
          - nessus file > ``ReportHost/ReportItem/"cm:compliance-info", namespaces={'cm': 'http://www.nessus.org/cm'}/``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

************
Check status
************

    .. list-table:: Check status - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Check status

        * - Description
          - Exact Compliance Check status returned by Nessus.

        * - Source
          - nessus file > ``ReportHost/ReportItem/"cm:compliance-result", namespaces={'cm': 'http://www.nessus.org/cm'}/``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

*********
Reference
*********

    .. list-table:: Reference - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Reference

        * - Description
          - Exact Compliance Check reference returned by Nessus.

        * - Source
          - nessus file > ``ReportHost/ReportItem/"cm:compliance-reference", namespaces={'cm': 'http://www.nessus.org/cm'}/``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``

*****
Error
*****

    .. list-table:: Error - column details
        :widths: 10 90
        :stub-columns: 1

        * - Header name
          - Error

        * - Description
          - Exact Compliance Check error returned by Nessus, if error occur.

        * - Source
          - nessus file > ``ReportHost/ReportItem/"cm:compliance-error", namespaces={'cm': 'http://www.nessus.org/cm'}/``

        * - Post-processing
          - *none*

        * - Column type
          - ``debug``, ``default``
