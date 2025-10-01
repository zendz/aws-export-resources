# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.5.3] - 2025-10-01

### Fixed
- **Tag Data Verification**: Comprehensive tag handling improvements
  - Fixed Lambda functions duplicate tag processing issue
  - Fixed ECS Clusters lowercase tag format conversion (key/value → Key/Value)
  - Improved malformed tag filtering to prevent invalid additional tag entries
  - Enhanced error handling for missing tag keys or values
  - Standardized tag processing across all AWS services
- **Data Quality**: Eliminated tag-related Excel export inconsistencies
- **Export Reliability**: Reduced failures from tag processing errors

### Enhanced
- **Tag Validation**: Added comprehensive tag format validation
- **Service Compatibility**: Ensured consistent tag extraction across 22 AWS services
- **Case Sensitivity**: Improved case-insensitive tag matching for common tags

## [1.5.2] - 2025-10-01

### Added
- **ECS Clusters Export**: New comprehensive ECS cluster monitoring functionality
  - Cluster status and resource metrics (active services, running/pending tasks)
  - Container instance counts and cluster statistics
  - Capacity provider configuration and strategies
  - Service Connect defaults and cluster configurations
  - Complete tag support with ARN identification
  - Integration with parallel processing workflow

### Enhanced
- **Service Coverage**: Now supports 22 AWS services with ECS Clusters addition
- **Container Orchestration**: Complete ECS coverage with both Services and Clusters

## [1.5.1] - 2025-10-01

### Added
- **ARN Fields**: Enhanced resource identification with ARN columns
  - EC2 instances: Added ARN column for complete resource identification
  - Lambda functions: Added ARN and Create Date columns
  - DynamoDB tables: Added ARN column
  - S3 buckets: Added ARN column
  - ECS Services: Added ARN and Create Date columns
  - RDS Instances: Added ARN and Create Date columns

### Enhanced
- **KMS Keys Export**: Now exports only customer-managed keys (excludes AWS-managed keys)
- **Resource Tracking**: Improved resource identification and compliance reporting

### Fixed
- KMS export performance improved by filtering out numerous AWS-managed keys
- Resource ARNs provide consistent identification across AWS services

## [1.5.0] - 2025-10-01

### Added
- **VPC Endpoints Export**: Added comprehensive VPC endpoints export functionality
  - VPC endpoint details including type, service name, and state
  - Associated VPC information (ID, name, CIDR)
  - Network configuration (route tables, subnets, security groups)
  - DNS settings and policy documents
  - Creation timestamps and DNS entries
- **KMS Keys Export**: Added detailed KMS keys export functionality
  - Key metadata including ARN, description, and usage
  - Key state and management information (AWS vs Customer managed)
  - Security features (rotation status, multi-region configuration)
  - Key aliases and associated tags
  - Creation and deletion dates

### Enhanced
- Load balancer export with additional security details:
  - TLS certificate information from listeners
  - Security policy details for SSL/TLS connections
  - ARN and creation date information

### Fixed
- **Excel Corruption Prevention**: Added comprehensive data sanitization
  - Prevents Excel formula injection (escapes =, +, -, @ characters)
  - Removes control characters that cause XML corruption
  - Limits cell content length to prevent Excel limits exceeded
  - Sanitizes all exported data to ensure valid Excel files
- Fixed VPC Summary worksheet missing tag columns causing sheet corruption

### Changed
- Updated configuration to include 'vpc-endpoints' and 'kms' services
- Improved parallel processing to handle new resource types
- Enhanced data validation and sanitization across all export functions

## [1.4.1] - 2025-10-01

### Added
- Separated configuration into dedicated `config.py` file
- Added `config_example.py` template for easy setup
- Added `test_config.py` utility for configuration validation
- Comprehensive documentation and security improvements
- Professional contact information with GitHub Issues only policy

### Changed
- Updated all documentation to use `python3` instead of `python`
- Moved from email contact to GitHub Issues only for security
- Enhanced project structure with proper file organization

### Security
- Implemented email protection against bot scanning
- Added `config.py` to .gitignore to prevent credential exposure
- Created SECURITY.md with comprehensive security guidelines
- Removed email addresses from all public documentation

### Documentation
- Updated README.md with configuration section and python3 usage
- Enhanced CONTRIBUTING.md with config setup instructions
- Added professional author attribution with organization details
- Improved project setup and usage instructions

## [1.4.0] - 2025-10-01

### Added
- Comprehensive tag extraction system with configurable common tags
- Standardized tag columns across all resource types
- Support for additional tags collection beyond common tags
- Enhanced VPC and subnet details integration across all services
- Detailed storage information for ECS services (EBS, EFS, Ephemeral)
- Comprehensive parallel profile processing with optional main_parallel_profiles()
- Comprehensive error reporting and logging

### Improved
- Excel formatting with auto-column width adjustment
- Header styling with consistent formatting across all sheets
- Thread-safe parallel processing for faster exports
- Configurable tag extraction with common tag filtering
- Code documentation and maintainability

## [1.3.0] - 2025-09-30

### Added
- Parallel processing with threading for faster exports
- Concurrent API calls for multiple services using ThreadPoolExecutor
- Execution time tracking and progress indicators

### Improved
- Error handling with thread-safe operations
- Performance improvements: 70% faster execution time

## [1.2.0] - 2025-09-28

### Added
- S3 Buckets with comprehensive details (versioning, encryption, public access)
- S3 Glacier Vaults with notification settings
- Cognito User Pools and Identity Pools

### Improved
- Error handling and resource details
- Security information extraction

## [1.1.0] - 2025-09-25

### Added
- Load Balancers (ALB, NLB, GLB) export
- DynamoDB Tables with detailed configuration
- CloudWatch Alarms and Log Groups
- Transfer Family servers
- AWS Personalize campaigns
- Enhanced RDS with Aurora Clusters support

### Fixed
- Bug fixes for VPC detection

## [1.0.0] - 2025-09-20

### Added
- Initial release
- Basic AWS resource export functionality
- Support for EC2, RDS, Lambda, EFS, ECS, EKS, ElastiCache, Amazon MQ
- Multi-profile support
- Excel export with formatting

## Known Issues & Limitations

- AWS API rate limiting may occur with too many concurrent requests
- Some services may not be available in all AWS regions
- Large accounts may experience timeout issues with certain services
- S3 bucket operations may be slow for accounts with many buckets

## Authors

- **Nattait Nandawarang** - *Gosoft (Thailand) Co., Ltd.*
- Position: Expert DevOps Engineer, Data Science and Data Engineering Team