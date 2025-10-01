"""
AWS Export Resources - Example Configuration File

Copy this file to config.py and modify according to your environment.
This example shows the basic configuration needed to get started.

Author: Nattait Nandawarang
Organization: Gosoft (Thailand) Co., Ltd.
Contact: GitHub Issues Only - https://github.com/zendz/aws-export-resources/issues
"""

# ==================== BASIC CONFIGURATION ====================
# List your AWS profile names here
AWS_PROFILES = [
    'default',        # Default AWS profile
    'production',     # Production environment
    'staging',        # Staging environment
    'development'     # Development environment
]

# ==================== TAG CONFIGURATION ====================
# Common tags that will be extracted as separate columns
COMMON_TAG_KEYS = [
    'Name',           # Resource name
    'Environment',    # Environment (dev, staging, prod)
    'Project',        # Project identifier
    'Owner',          # Resource owner
    'CostCenter',     # Cost center for billing
    'Application'     # Application name
]

# ==================== BASIC SETTINGS ====================
# Maximum number of threads for parallel processing
MAX_WORKERS = 5

# Services to include (remove unwanted services)
ENABLED_SERVICES = [
    'ec2',
    'rds',
    'lambda',
    's3',
    'vpc'
]

# AWS regions to scan (None = all regions)
AWS_REGIONS = None

# ==================== EXCEL CONFIGURATION ====================
EXCEL_STYLING = {
    'header_font': {'bold': True, 'color': 'FFFFFF', 'size': 12},
    'header_fill': {'fill_type': 'solid', 'start_color': '366092'},
    'header_alignment': {'horizontal': 'center', 'vertical': 'center'}
}

# ==================== DEFAULT SETTINGS ====================
# These can be left as-is for most use cases
OUTPUT_FILE_PREFIX = 'aws_resources'
TIMEOUTS = {'api_call': 30, 'service_export': 300, 'total_export': 1800}
RETRY_CONFIG = {'max_attempts': 3, 'backoff_factor': 2, 'retry_on_errors': ['ClientError', 'TimeoutError', 'ConnectionError']}
LOGGING_CONFIG = {'level': 'INFO', 'format': '%(asctime)s - %(levelname)s - %(message)s', 'show_progress': True, 'show_timing': True}
ADVANCED_OPTIONS = {'include_additional_tags': True, 'auto_adjust_column_width': True, 'include_empty_services': False, 'parallel_profile_processing': False, 'detailed_vpc_info': True, 'include_cost_estimates': False}
SECURITY_SETTINGS = {'mask_sensitive_data': False, 'exclude_default_vpcs': False, 'compliance_mode': False, 'audit_trail': True}