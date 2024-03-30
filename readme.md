# Advanced Python Calculator

This project is an advanced Python-based calculator application developed for the Software Engineering Graduate Course. It incorporates professional software development practices, including clean and maintainable code, design patterns, comprehensive logging, dynamic configuration via environment variables, sophisticated data handling with Pandas, and a command-line interface (REPL) for real-time user interaction.

## Core Functionalities

### Command-Line Interface (REPL)

The calculator application provides a Read-Eval-Print Loop (REPL) for direct interaction with users. The interface supports:

- Execution of arithmetic operations (Add, Subtract, Multiply, and Divide)
- Management of calculation history
- Access to extended functionalities through dynamically loaded plugins

**Implementation:** See [`main.py`](main.py#L31) for the REPL implementation.

### Plugin System

The application includes a flexible plugin system to seamlessly integrate new commands or features. This system allows:

- Dynamic loading and integration of plugins without modifying the core application code
- A "Menu" command in the REPL to list all available plugin commands for user interaction

**Implementation:** See the [`plugins/`](plugins/) directory for plugin implementations.

### Calculation History Management with Pandas

Pandas is utilized for managing a robust calculation history, enabling users to:

- Load, save, clear, and delete history records through the REPL interface

**Implementation:** See [`calculations.py`](/calculator/calculations.py#L46) for calculation history management with Pandas.

### Professional Logging Practices

A comprehensive logging system is established to record:

- Detailed application operations, data manipulations, errors, and informational messages
- Differentiated log messages by severity (INFO, WARNING, ERROR) for effective monitoring
- Dynamic logging configuration through environment variables for levels and output destinations

**Implementation:** See [`logging_config.py`](logging_config.py) for logging configuration.

### Advanced Data Handling with Pandas

Pandas is employed for:

- Efficient data reading and writing to CSV files
- Managing calculation history

**Implementation:** See [`calculations.py`](calculations.py) for examples of advanced data handling with Pandas.

## Design Patterns

The following design patterns are implemented to address various software design challenges:

- Facade Pattern: Offers a simplified interface for complex Pandas data manipulations
- Command Pattern: Structures commands within the REPL for effective calculation and history management
- Factory Method, Singleton, and Strategy Patterns: Enhance the application's code structure, flexibility, and scalability

**Implementation:** Design patterns are implemented throughout the codebase. See relevant files for each pattern's implementation.

## Testing and Code Quality

The application ensures robust testing and code quality practices:

- Achieved over 90% test coverage with Pytest
- Adhered to PEP 8 standards for clean and readable code
- Utilized Pylint for code quality checks

**Implementation:** See the [`tests/`](tests/) directory for test implementations.

## Version Control, Documentation, and Logging

Best practices are followed for version control, documentation, and logging:

- Maintained logical and informative commit history
- Provided comprehensive setup and usage instructions in the README.md
- Implemented adaptable and informative logging practices

**Implementation:** Refer to the commit history for version control practices, README.md for documentation, and log for logging examples.

## Environment Variables

Dynamic logging configuration is achieved through environment variables, allowing users to configure log levels and output destinations according to their requirements.

**Implementation:** See [`.env`](.env) for environment variables configuration.

## Video Demonstration

A 3-5 minute video demonstration showcasing the calculator's key features and functionalities is available [here](video_link).

## Setup Instructions

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the application using `python main.py`.

## Usage

- Launch the calculator application by running `python main.py`.
- Follow the on-screen prompts to perform arithmetic operations, manage calculation history, and access extended functionalities through plugins.

