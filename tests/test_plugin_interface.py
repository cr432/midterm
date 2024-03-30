"""test_plugin_interface.py"""
from decimal import Decimal
import logging
from plugins.plugin_interface import CommandPlugin

# Set up logging
logger = logging.getLogger(__name__)

class MockPlugin(CommandPlugin):
    """MockPlugin class."""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """Execute method."""
        return a + b

def test_plugin_interface():
    """Test plugin interface."""
    logger.info("Testing plugin interface.")
    plugin = MockPlugin()
    result = plugin.execute(Decimal('2'), Decimal('3'))
    assert result == Decimal('5')
