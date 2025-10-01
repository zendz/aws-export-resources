# AWS Export Resources

A Python tool to ex3. Configure your AWS credentials:
   ```bash
   aws configure
   ```
   Or use environment variables, IAM roles, or AWS profiles.

4. Test your configuration:
   ```bash
   python3 test_config.py
   ```AWS resources across multiple services and regions to an Excel spreadsheet for inventory management and compliance reporting.

## Features

- **Multi-Service Support**: Export resources from 20+ AWS services including EC2, S3, RDS, Lambda, VPC, and more
- **Multi-Region**: Scan resources across all AWS regions or specific regions
- **Excel Export**: Generates a comprehensive Excel file with separate sheets for each service
- **Concurrent Processing**: Uses threading for faster resource discovery
- **Error Handling**: Robust error handling with detailed logging
- **Flexible Configuration**: Support for different AWS profiles and credentials

## Supported AWS Services

This tool exports the following AWS resources across multiple profiles:

- **EC2 Instances** - Including security groups, VPC details, and instance metadata
- **RDS Instances & Clusters** - Database instances, Aurora clusters, and configuration
- **Lambda Functions** - Function details, runtime, memory, and VPC configuration
- **EFS File Systems** - File system details, performance mode, and access points
- **ECS Services** - Service definitions, task definitions, and cluster information
- **ECS Clusters** - Cluster status, capacity providers, and resource metrics
- **EKS Clusters** - Kubernetes cluster details, node groups, and networking
- **ElastiCache** - Redis and Memcached clusters with configuration details
- **Amazon MQ** - Message broker instances and configuration
- **Load Balancers** - ALB/NLB with listeners, target groups, and TLS certificates
- **DynamoDB Tables** - Table schemas, capacity settings, and global tables
- **CloudWatch Alarms** - Monitoring alarms and their configurations
- **CloudWatch Log Groups** - Log group details and retention settings
- **AWS Transfer Family** - SFTP/FTPS server details and user configurations
- **AWS Personalize** - Machine learning solution schemas and campaigns
- **S3 Buckets** - Bucket properties, encryption, versioning, and lifecycle policies
- **S3 Glacier Vaults** - Archive vault details and access policies
- **Cognito User Pools** - User authentication pool configurations
- **Cognito Identity Pools** - Identity federation pool settings
- **VPC Endpoints** - Service endpoints, DNS settings, and security configurations
- **KMS Keys** - Encryption key details, rotation status, and aliases
- **ECR Repositories** - Container registry details, policies, image statistics, and security scanning
- **API Gateway** - REST APIs with stages, endpoints, configuration, and comprehensive tag support
- **VPC Summary** - Complete VPC topology with subnets, route tables, and gateways

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/zendz/aws-export-resources.git
   cd aws-export-resources
   ```

2. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

3. Configure AWS credentials:
   ```bash
   aws configure
   ```
   Or use environment variables, IAM roles, or AWS profiles.

## Usage

### Basic Usage

```bash
python3 aws_export_resources.py
```

### With Custom Profile

```bash
AWS_PROFILE=your-profile python3 aws_export_resources.py
```

### Command Line Options

The tool supports various configuration options through environment variables or code modification:

- `AWS_PROFILE`: AWS profile to use
- `AWS_REGION`: Specific region to scan (default: all regions)
- `OUTPUT_FILE`: Custom output filename

## Output

The tool generates an Excel file named `aws_resources_DDMMYY-HHMM_ACCOUNT-ID-PROFILE.xlsx` containing:

- **Summary Sheet**: Overview of all discovered resources
- **Service-Specific Sheets**: Detailed information for each AWS service
- **Styled Formatting**: Color-coded headers and proper formatting

## Configuration

### Basic Configuration

Edit `config.py` to customize the tool for your environment:

```python
# AWS Profiles to scan
AWS_PROFILES = [
    'production',
    'staging',
    'dev'
]

# Common tags to extract as columns
COMMON_TAG_KEYS = [
    'Service',
    'Environment',
    'Project',
    'Name'
]
```

### Advanced Configuration

The `config.py` file provides extensive configuration options:

- **AWS Services**: Enable/disable specific services to scan
- **Regions**: Specify regions to scan or scan all regions
- **Threading**: Configure parallel processing settings
- **Excel Styling**: Customize output formatting
- **Error Handling**: Configure retry logic and timeouts
- **Security**: Enable compliance and audit features

### AWS Credentials

The tool supports multiple authentication methods:

1. **AWS CLI Profile**:
   ```bash
   aws configure --profile myprofile
   ```

2. **Environment Variables**:
   ```bash
   export AWS_ACCESS_KEY_ID=your-key
   export AWS_SECRET_ACCESS_KEY=your-secret
   export AWS_DEFAULT_REGION=us-east-1
   ```

3. **IAM Roles**: When running on EC2 instances

### Customization

You can customize the tool by modifying `config.py`:

- **Services to scan**: Edit `ENABLED_SERVICES` list
- **Regions**: Modify `AWS_REGIONS` setting
- **AWS Profiles**: Update `AWS_PROFILES` list
- **Tag extraction**: Customize `COMMON_TAG_KEYS`
- **Output format**: Adjust `EXCEL_STYLING` options
- **Performance**: Tune `MAX_WORKERS` and `TIMEOUTS`
- **Security**: Configure `SECURITY_SETTINGS`

## Performance Considerations

- **Large Accounts**: May take several minutes to complete
- **Rate Limiting**: AWS API rate limits may slow down execution
- **Memory Usage**: Large accounts may require more memory
- **Network**: Requires stable internet connection

## Troubleshooting

### Common Issues

1. **Authentication Errors**:
   - Verify AWS credentials are configured
   - Check IAM permissions
   - Ensure profile exists

2. **Permission Denied**:
   - Review IAM policies
   - Ensure read permissions for all services

3. **Timeout Issues**:
   - Reduce concurrent threads
   - Focus on specific regions
   - Break down by service

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

## Author

**Nattait Nandawarang**  
Expert DevOps Engineer  
Data Science and Data Engineering Team  
Gosoft (Thailand) Co., Ltd.  

**Contact:** GitHub Issues Only - [Create Issue](https://github.com/zendz/aws-export-resources/issues/new)

## Support

## Support

**All support is provided through GitHub Issues only.**

For issues, questions, or feature requests:
- 🐛 **Report Bugs**: [Create a Bug Report](https://github.com/zendz/aws-export-resources/issues/new)
- 💡 **Request Features**: [Suggest an Enhancement](https://github.com/zendz/aws-export-resources/issues/new)
- ❓ **Ask Questions**: [Get Help](https://github.com/zendz/aws-export-resources/issues/new)
- 📖 **Contributing**: Check the [Contributing Guide](CONTRIBUTING.md) for development setup
- 🔒 **Security**: See [Security Guidelines](SECURITY.md) for security-related information

**Why GitHub Issues?**
- Transparent and searchable for the community
- Better tracking and resolution of problems
- Collaborative problem-solving
- Knowledge base for future users

**Note:** Email contact has been removed for security and efficiency. All communication goes through GitHub Issues.

## Changelog

### Version 1.5.0
- **New Resource Types**: Added VPC Endpoints and KMS Keys export functionality
- **Enhanced Security**: Load balancer export now includes TLS certificate and security policy details
- **Excel Corruption Fix**: Comprehensive data sanitization prevents Excel file corruption
- **Improved Coverage**: Support for 21 AWS services with comprehensive field mapping

### Version 1.4.1
- Configuration separation into dedicated config.py file
- Updated documentation to use python3
- Enhanced security with GitHub Issues only policy
- Added configuration validation tools

### Version 1.4.0
- Comprehensive tag extraction system
- Enhanced parallel processing capabilities
- Advanced Excel formatting and styling