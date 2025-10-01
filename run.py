#!/usr/bin/env python3
"""
AWS Export Resources - Direct Entry Point

Alternative entry point that can be used from the root directory.
"""

import sys
import os

# Add src directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.insert(0, src_dir)

if __name__ == "__main__":
    # Import and run the main function
    try:
        from aws_export_resources import main
        main()
    except ImportError as e:
        print(f"Error importing from src directory: {e}")
        print("Make sure all required dependencies are installed:")
        print("pip3 install boto3 openpyxl")
        sys.exit(1)