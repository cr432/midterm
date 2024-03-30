# operations.py
from decimal import Decimal
from abc import ABC, abstractmethod
from logging_config import logger
import os
import importlib.util

class Command(ABC):
    @abstractmethod
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        pass

class AddCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        result = a + b
        logger.info(f'Addition operation: {a} + {b} = {result}')
        return result

class SubtractCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        result = a - b
        logger.info(f'Subtraction operation: {a} - {b} = {result}')
        return result

class MultiplyCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        result = a * b
        logger.info(f'Multiplication operation: {a} * {b} = {result}')
        return result

class DivideCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        if b != 0:
            result = a / b
            logger.info(f'Division operation: {a} / {b} = {result}')
            return result
        else:
            logger.error('Division by zero error')
            raise ZeroDivisionError("Error: Division by zero.")

class MenuCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        logger.info('Displaying menu options')
        print("Available Commands:")
        print("add - Addition")
        print("subtract - Subtraction")
        print("multiply - Multiplication")
        print("divide - Division")
        for plugin in load_plugins():
            print(f"{plugin.__class__.__name__.lower()} - {plugin.__class__.__name__}")
        return Decimal(0)

def load_plugins():
    plugins = []
    plugin_dir = 'plugins'
    plugin_files = os.listdir(plugin_dir)
    for file in plugin_files:
        if file.endswith('.py'):
            module_name = file[:-3]
            module_path = os.path.join(plugin_dir, file)
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            plugin_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(plugin_module)
            for name in dir(plugin_module):
                obj = getattr(plugin_module, name)
                if hasattr(obj, '__bases__') and Command in obj.__bases__:
                    plugin = obj()
                    plugins.append(plugin)
                    break
    return plugins
