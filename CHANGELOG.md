# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-10-01

### MAJOR RELEASE: Complete Project Restructure ⚡

This major version release introduces a complete architectural overhaul with a professional Python package structure, enhanced CLI interface, and improved maintainability.

### 🎯 **Breaking Changes**
- **Project Structure**: Complete reorganization into `src/` package structure
- **Entry Points**: New CLI interface and multiple execution methods
- **Configuration**: Centralized configuration management with better organization
- **File Organization**: Separated source code, tests, examples, and outputs

### 🚀 **Added**
- **Professional Package Structure**:
  - `src/` directory containing all source code as proper Python package
  - `tests/` directory for all test files and utilities
  - `examples/` directory for configuration examples
  - `outputs/` directory for generated Excel files
  - `docs/` directory for enhanced documentation

- **Enhanced CLI Interface** (`aws-export.py`):
  - `--help` flag with comprehensive usage information
  - `--version` flag for version information
  - `--list-profiles` flag to show available AWS profiles
  - Better error handling and user feedback
  - Professional command-line experience

- **Multiple Entry Points**:
  - `aws-export.py` - Enhanced CLI with help system
  - `run.py` - Simple entry point with error handling  
  - `main.py` - Basic entry point for compatibility
  - Direct execution support from `src/` directory

- **Package Installation Support**:
  - `setup.py` for proper Python package installation
  - `pip install -e .` development mode support
  - `aws-export-resources` command-line tool after installation
  - `MANIFEST.in` for proper package distribution

### 🔧 **Enhanced**
- **Configuration Management**:
  - Moved all hardcoded values to centralized configuration
  - `MAX_WORKERS` and `MAX_PROFILE_WORKERS` from config
  - `OUTPUT_FILE_PREFIX` configurable filename prefix
  - `EXCEL_STYLING` centralized formatting configuration
  - Version information managed in dedicated `_version.py`

- **Code Organization**:
  - Clean separation between source code and configuration
  - Proper Python package structure with `__init__.py` files
  - Professional project layout following Python best practices
  - Better maintainability and extensibility

### 📈 **Migration Guide**
- **Old usage**: `python3 aws_export_resources.py`
- **New usage**: 
  - `python3 aws-export.py` (recommended - enhanced CLI)
  - `python3 run.py` (simple alternative)
  - `pip install -e . && aws-export-resources` (package installation)

### 🛠️ **Technical Improvements**
- Version management centralized in `src/_version.py`
- Configuration imports streamlined and organized
- Better error handling across all entry points
- Enhanced documentation and project structure guide
- Proper package manifest for distribution

## [1.5.5] - 2025-10-01

### Added
- **ECR (Elastic Container Registry)**: Complete container repository export
  - Repository details: name, ARN, URI, registry ID, creation date
  - Configuration: image tag mutability, scan on push, encryption settings
  - Policies: lifecycle policy and repository policy detection
  - Statistics: image count, repository size in MB, last push date
  - Security: KMS encryption key information and vulnerability scanning
  - Full tag extraction support for resource organization
- **API Gateway**: Comprehensive REST API export functionality
  - API information: name, ID, type, protocol, endpoints
  - Stage details: stage names and endpoints for each API
  - Configuration: API key source, CORS settings, binary media types
  - Settings: compression settings, execute API endpoint status
  - ARN generation for proper resource identification
  - Complete tag support with both API-level and stage-level tags
  - Creation dates with proper timestamp formatting

### Enhanced
- **Tag Processing**: Improved tag format compatibility
  - Fixed API Gateway tag format conversion (dictionary → AWS standard format)
  - Enhanced tag extraction to handle service-specific tag structures
  - Standardized tag processing across all 25+ AWS services
- **Parallel Processing**: Both services integrated into concurrent export workflow
- **Error Handling**: Robust error handling for API failures and missing permissions
- **Excel Export**: Added dedicated worksheets for ECR and API Gateway services

### Fixed
- **API Gateway Tags**: Resolved 'str' object has no attribute 'get' error
  - Root cause: Tag format mismatch between API Gateway and standard AWS format
  - Solution: Convert API Gateway dictionary format to standard AWS list format
  - Impact: Eliminates all API Gateway export errors and enables proper tag extraction

## [1.5.4] - 2025-10-01

### Enhanced
- **ECS Clusters AWS Batch Filter**: Improved AWS Batch cluster filtering precision
  - Updated filter to specifically target clusters starting with "AWSBatch-"
  - Based on real AWS Batch cluster naming patterns (e.g., AWSBatch-environment-uuid)
  - Prevents filtering of normal ECS clusters that contain "batch" in their names
  - More accurate identification of AWS Batch managed clusters vs user-created ECS clusters

### Fixed
- **ECS Clusters Export**: Eliminates AWS Batch cluster noise from ECS exports
- **Filter Precision**: Reduces false positives in AWS Batch cluster detection

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