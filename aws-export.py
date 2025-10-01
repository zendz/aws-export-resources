#!/usr/bin/env python3
"""
AWS Export Resources - Enhanced CLI Entry Point

This script provides a better command-line interface with help and version options.
"""

import sys
import os
import argparse

# Add src directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.insert(0, src_dir)


def show_help():
    """Display help information"""
    help_text = """
AWS Export Resources Tool - v2.0.1

DESCRIPTION:
    A comprehensive AWS resource inventory tool that exports detailed information
    about AWS resources across multiple profiles to Excel format.

USAGE:
    python3 aws-export.py [OPTIONS] [PROFILES...]

OPTIONS:
    -h, --help          Show this help message
    -v, --version       Show version information
    -l, --list-profiles List configured AWS profiles

EXAMPLES:
    # Export all configured profiles
    python3 aws-export.py

    # Export specific profiles
    python3 aws-export.py profile1 profile2

    # Show version
    python3 aws-export.py --version

    # List available profiles
    python3 aws-export.py --list-profiles

SUPPORTED SERVICES:
    EC2, RDS, Lambda, EFS, ECS, EKS, ElastiCache, MQ, Load Balancers,
    DynamoDB, CloudWatch, S3, Glacier, VPC, KMS, ECR, API Gateway, and more.

OUTPUT:
    Excel files are saved in the 'outputs/' directory with timestamps and
    account information in the filename.

For more information, visit:
https://github.com/zendz/aws-export-resources
"""
    print(help_text)


def show_version():
    """Display version information"""
    try:
        from config import VERSION, TOOL_NAME, AUTHOR
        print(f"{TOOL_NAME} v{VERSION}")
        print(f"Author: {AUTHOR}")
    except ImportError:
        print("AWS Export Resources v2.0.1")


def list_profiles():
    """List configured AWS profiles"""
    try:
        import boto3
        session = boto3.Session()
        profiles = session.available_profiles
        if profiles:
            print("Available AWS profiles:")
            for profile in sorted(profiles):
                print(f"  - {profile}")
        else:
            print("No AWS profiles found. Configure profiles in ~/.aws/credentials")
    except Exception as e:
        print(f"Error listing profiles: {e}")


def main():
    """Enhanced main function with CLI support"""
    # Check for help/version flags first
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg in ['-h', '--help', 'help']:
            show_help()
            return
        elif arg in ['-v', '--version', 'version']:
            show_version()
            return
        elif arg in ['-l', '--list-profiles', 'list-profiles']:
            list_profiles()
            return

    # Import and run the main function
    try:
        from aws_export_resources import main as aws_main
        aws_main()
    except ImportError as e:
        print(f"Error importing from src directory: {e}")
        print("Make sure all required dependencies are installed:")
        print("pip3 install boto3 openpyxl")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n❌ Export cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()