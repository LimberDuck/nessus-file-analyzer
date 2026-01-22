# -*- coding: utf-8 -*-
"""
Plugin discovery mechanism for NFA.

This module handles discovering and loading installed NFA plugins using entry points.
"""

import sys
from typing import List, Dict, Type
from .base import NFAPlugin

# Python 3.10+ uses importlib.metadata, earlier versions use importlib_metadata
if sys.version_info >= (3, 10):
    from importlib.metadata import entry_points
else:
    from importlib_metadata import entry_points


# Bundled plugins for PyInstaller frozen builds
# Entry points don't work in frozen apps, so we register known plugins here
BUNDLED_PLUGINS = [
    ('nfa_plugin_software_enumeration.software_enumeration', 'SoftwareEnumerationPlugin'),
]


def _discover_bundled_plugins() -> List[Type[NFAPlugin]]:
    """
    Load plugins bundled with PyInstaller frozen builds.

    Returns:
        List of plugin classes from bundled plugins
    """
    discovered_plugins = []

    for module_path, class_name in BUNDLED_PLUGINS:
        try:
            import importlib
            module = importlib.import_module(module_path)
            plugin_class = getattr(module, class_name)
            if isinstance(plugin_class, type) and issubclass(plugin_class, NFAPlugin):
                discovered_plugins.append(plugin_class)
            else:
                print(f"Warning: Bundled plugin {class_name} does not inherit from NFAPlugin")
        except ImportError as e:
            # Plugin not bundled, skip silently
            pass
        except Exception as e:
            print(f"Warning: Failed to load bundled plugin {class_name}: {e}")

    return discovered_plugins


def discover_plugins() -> List[Type[NFAPlugin]]:
    """
    Discover all installed NFA plugins using entry points.

    Plugins are discovered via the 'nfa.plugins' entry point group.
    Each plugin package should register its plugin class in setup.py like:

        entry_points={
            'nfa.plugins': [
                'plugin_name = package.module:PluginClass',
            ],
        }

    For PyInstaller frozen builds, bundled plugins are loaded directly
    since entry points don't work in frozen applications.

    Returns:
        List of plugin classes (not instances) that inherit from NFAPlugin
    """
    discovered_plugins = []

    try:
        # Python 3.10+ returns EntryPoints object with select() method
        if sys.version_info >= (3, 10):
            eps = entry_points(group='nfa.plugins')
        else:
            # Python 3.9 and earlier returns dict
            eps = entry_points().get('nfa.plugins', [])

        for ep in eps:
            try:
                plugin_class = ep.load()
                # Verify it's a subclass of NFAPlugin
                if isinstance(plugin_class, type) and issubclass(plugin_class, NFAPlugin):
                    discovered_plugins.append(plugin_class)
                else:
                    print(f"Warning: Plugin {ep.name} does not inherit from NFAPlugin")
            except Exception as e:
                print(f"Warning: Failed to load plugin {ep.name}: {e}")

    except Exception as e:
        print(f"Warning: Failed to discover plugins: {e}")

    # For frozen builds (PyInstaller), also try loading bundled plugins
    # This is needed because entry points don't work in frozen applications
    if getattr(sys, 'frozen', False):
        bundled = _discover_bundled_plugins()
        # Add bundled plugins that weren't already discovered via entry points
        existing_names = {p.__name__ for p in discovered_plugins}
        for plugin in bundled:
            if plugin.__name__ not in existing_names:
                discovered_plugins.append(plugin)

    return discovered_plugins


def get_installed_plugins() -> Dict[str, Type[NFAPlugin]]:
    """
    Get a dictionary of installed plugins keyed by plugin ID.

    Returns:
        Dictionary mapping plugin ID (string) to plugin class
        Example: {'software_enumeration': SoftwareEnumerationPlugin}
    """
    plugins = discover_plugins()
    plugin_dict = {}

    for plugin_class in plugins:
        try:
            # Instantiate temporarily to get metadata
            plugin_instance = plugin_class()
            metadata = plugin_instance.get_metadata()
            plugin_dict[metadata.id] = plugin_class
        except Exception as e:
            print(f"Warning: Failed to get metadata from plugin {plugin_class.__name__}: {e}")

    return plugin_dict
