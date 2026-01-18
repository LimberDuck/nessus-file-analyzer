# -*- coding: utf-8 -*-
"""
Base classes for NFA plugins.

This module defines the abstract base classes that all NFA plugins must inherit from.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Any, Optional
import xlsxwriter


@dataclass
class PluginMetadata:
    """
    Metadata for an NFA plugin.

    Attributes:
        name: Display name of the plugin (e.g., "Software Enumeration")
        id: Unique identifier for the plugin (e.g., "software_enumeration")
        version: Plugin version string (e.g., "1.0.0")
        description: Short description of what the plugin does
        author: Plugin author name
        plugin_ids: List of Nessus Plugin IDs this plugin processes
    """
    name: str
    id: str
    version: str
    description: str
    author: str
    plugin_ids: List[int]


class NFAPlugin(ABC):
    """
    Abstract base class for all NFA plugins.

    Plugins must implement this interface to be discoverable and usable by NFA.
    Each plugin provides custom report generation based on specific Nessus plugin outputs.
    """

    @abstractmethod
    def get_metadata(self) -> PluginMetadata:
        """
        Return metadata about this plugin.

        Returns:
            PluginMetadata: Plugin metadata including name, version, and plugin IDs
        """
        pass

    @abstractmethod
    def process_host_data(self, host_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Process data from a single host.

        This method is called for each host in the scan. It should extract and transform
        data from the specified plugin IDs into a format suitable for report generation.

        Args:
            host_data: Dictionary containing host information and plugin outputs
                Structure:
                {
                    'hostname': str,
                    'ip': str,
                    'os': str,
                    'plugins': {
                        plugin_id: {
                            'plugin_output': str,
                            'plugin_name': str,
                            ...
                        }
                    }
                }

        Returns:
            Dictionary with processed data for this host, or None if no relevant data found.
            The structure depends on the plugin implementation.
        """
        pass

    @abstractmethod
    def generate_report(self, workbook: xlsxwriter.Workbook, processed_data: List[Dict[str, Any]],
                       parsing_settings: Dict[str, Any]) -> None:
        """
        Generate the Excel report sheet for this plugin.

        This method is called once after all hosts have been processed. It should create
        one or more worksheets in the provided workbook with the processed data.

        Args:
            workbook: xlsxwriter.Workbook object to add sheets to
            processed_data: List of dictionaries returned from process_host_data() for all hosts
            parsing_settings: Dictionary containing user settings from the UI
        """
        pass

    @abstractmethod
    def get_enabled_setting_key(self) -> str:
        """
        Return the key used in parsing_settings to check if this plugin is enabled.

        Returns:
            String key, e.g., "plugin_software_enumeration_enabled"
        """
        pass

    def get_additional_settings(self) -> List[Dict[str, Any]]:
        """
        Return additional UI settings for this plugin (optional).

        Override this method to provide custom checkboxes or options in the Advanced tab.

        Returns:
            List of setting dictionaries with the following structure:
            [
                {
                    'type': 'checkbox',  # Currently only 'checkbox' is supported
                    'key': 'setting_key',  # Key in parsing_settings dictionary
                    'label': 'Display Label',  # Text shown in UI
                    'default': False,  # Default value
                    'tooltip': 'Optional tooltip text'
                }
            ]
        """
        return []
