# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

### Authors
- Nattait Nandawarang - Gosoft (Thailand) Co., Ltd.

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
- Code documentation and maintainability

### Authors
- Nattait Nandawarang - Gosoft (Thailand) Co., Ltd.

## [1.3.0] - 2025-09-30

### Added
- Parallel processing with threading for faster exports
- Concurrent API calls for multiple services using ThreadPoolExecutor
- Execution time tracking and progress indicators

### Improved
- Error handling with thread-safe operations
- Performance improvements: 70% faster execution time

### Authors
- Nattait Nandawarang - Gosoft (Thailand) Co., Ltd.

## [1.2.0] - 2025-09-28

### Added
- S3 Buckets with comprehensive details (versioning, encryption, public access)
- S3 Glacier Vaults with notification settings
- Cognito User Pools and Identity Pools

### Improved
- Error handling and resource details
- Security information extraction

### Authors
- Nattait Nandawarang - Gosoft (Thailand) Co., Ltd.

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

### Authors
- Nattait Nandawarang - Gosoft (Thailand) Co., Ltd.

## [1.0.0] - 2025-09-20

### Added
- Initial release
- Basic AWS resource export functionality
- Support for EC2, RDS, Lambda, EFS, ECS, EKS, ElastiCache, Amazon MQ
- Multi-profile support
- Excel export with formatting

### Authors
- Nattait Nandawarang - Gosoft (Thailand) Co., Ltd.

## Known Issues & Limitations

- AWS API rate limiting may occur with too many concurrent requests
- Some services may not be available in all AWS regions
- Large accounts may experience timeout issues with certain services
- S3 bucket operations may be slow for accounts with many buckets