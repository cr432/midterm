"""test_plugins.py"""
from decimal import Decimal
from importlib import import_module
import os
import inspect

from plugins.plugin_interface import CommandPlugin

def test_plugins():
    """Testing plugin execution"""
    plugins = []

    # Load plugins from the 'plugins' directory
    plugins_directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'plugins')
    for file_name in os.listdir(plugins_directory):
        if file_name.endswith('_plugin.py'):
            module_name = file_name[:-3]  # Remove '.py' extension
            module = import_module(f'plugins.{module_name}')
            for _, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, CommandPlugin) and obj != CommandPlugin:
                    plugins.append(obj())

    assert len(plugins) > 0
    for plugin in plugins:
        if plugin.__class__.__name__ == 'MenuPlugin':
            continue  # Skip testing MenuPlugin
        result = plugin.execute(Decimal('2'), Decimal('3'))
        assert result is not None, f"Plugin {plugin.__class__.__name__} returned None"  # Ensure the result is not None
        assert isinstance(result, (Decimal, int)), f"Plugin {plugin.__class__.__name__} returned invalid result type: {type(result)}"  # Check for Decimal or int
