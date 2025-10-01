#!/usr/bin/env python3
"""
AWS Export Resources - Main Entry Point

This is the main entry point for the AWS Export Resources tool.
The actual implementation is in the src/ directory.

Usage:
    python3 main.py                    # Use configured profiles
    python3 main.py profile1 profile2  # Use specific profiles
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import and run the main function from the source package
from aws_export_resources import main

if __name__ == "__main__":
    main()