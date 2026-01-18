# -*- coding: utf-8 -*-
"""
Plugin system for nessus file analyzer (NFA).

This module provides the base classes and discovery mechanism for NFA plugins.
"""

from .base import NFAPlugin, PluginMetadata
from .discovery import discover_plugins, get_installed_plugins

__all__ = ['NFAPlugin', 'PluginMetadata', 'discover_plugins', 'get_installed_plugins']
