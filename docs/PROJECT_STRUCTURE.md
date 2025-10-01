# Project Structure - AWS Export Resources v2.0.0

This document describes the organization of the AWS Export Resources project following the major v2.0.0 restructure.

## Overview

Version 2.0.0 introduces a complete architectural overhaul with professional Python package structure, enhanced CLI interface, and improved maintainability. All source code is now organized in the `src/` directory following Python best practices.

## Directory Structure

```
aws-export-resources/
├── src/                           # Source code
│   ├── __init__.py               # Package initialization
│   ├── _version.py               # Version information
│   ├── aws_export_resources.py   # Main export logic
│   └── config.py                 # Configuration settings
├── tests/                        # Test files and utilities
│   ├── __init__.py
│   ├── test_*.py                 # Test scripts
│   └── tag_verification_report.py
├── examples/                     # Example configurations
│   ├── __init__.py
│   └── config_example.py         # Example configuration
├── outputs/                      # Generated Excel files
│   └── *.xlsx                    # Export output files
├── docs/                         # Documentation files
│   ├── README.md
│   ├── CHANGELOG.md
│   └── CONTRIBUTING.md
├── main.py                       # Main entry point
├── run.py                        # Convenient run script
├── setup.py                      # Package installation script
├── requirements.txt              # Python dependencies
└── MANIFEST.in                   # Package manifest
```

## Entry Points

### Development/Direct Usage
- `python3 run.py` - Convenient entry point with error handling
- `python3 main.py` - Main entry point
- `cd src && python3 aws_export_resources.py` - Direct execution

### Package Installation
- `pip3 install -e .` - Install in development mode
- `aws-export-resources` - Command line tool (after installation)

## Configuration

- **src/config.py** - Main configuration file
- **examples/config_example.py** - Example configuration template

## Testing

- **tests/** - All test files and utilities
- Run tests from project root: `python3 -m pytest tests/`

## Output Files

- **outputs/** - All generated Excel files are stored here
- Files are automatically named with timestamp and profile information