# AWS Export Resources

A Python tool to export AWS resources across multiple services and regions to an Excel spreadsheet for inventory management and compliance reporting.

## Features

- **Multi-Service Support**: Export resources from 20+ AWS services including EC2, S3, RDS, Lambda, VPC, and more
- **Multi-Region**: Scan resources across all AWS regions or specific regions
- **Excel Export**: Generates a comprehensive Excel file with separate sheets for each service
- **Concurrent Processing**: Uses threading for faster resource discovery
- **Error Handling**: Robust error handling with detailed logging
- **Flexible Configuration**: Support for different AWS profiles and credentials

## Supported AWS Services

- EC2 Instances
- S3 Buckets
- RDS Instances
- Lambda Functions
- VPC Resources
- Load Balancers (ALB/NLB/CLB)
- Auto Scaling Groups
- CloudFormation Stacks
- IAM Roles and Users
- Route53 Hosted Zones
- CloudWatch Alarms
- SNS Topics
- SQS Queues
- And many more...

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/zendz/aws-export-resources.git
   cd aws-export-resources
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure AWS credentials:
   ```bash
   aws configure
   ```
   Or use environment variables, IAM roles, or AWS profiles.

## Usage

### Basic Usage

```bash
python main9.py
```

### With Custom Profile

```bash
AWS_PROFILE=your-profile python main9.py
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

You can customize the tool by modifying:

- **Services to scan**: Edit the service list in the main function
- **Regions**: Modify the region list or use specific regions
- **Output format**: Customize Excel styling and structure
- **Filters**: Add resource filtering logic

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

### Version 1.0.0
- Initial release
- Support for 20+ AWS services
- Multi-region scanning
- Excel export functionality
- Concurrent processing