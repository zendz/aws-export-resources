#!/usr/bin/env python3
"""
Tag Verification Test Script
Tests tag extraction for different AWS service formats
"""

import sys
import boto3
from aws_export_resources import extract_tags, get_tag_values, COMMON_TAG_KEYS

def test_tag_formats():
    """Test different tag formats used by AWS services"""
    
    print("=== TAG VERIFICATION TEST ===\n")
    
    # Test Case 1: Standard AWS tag format (EC2, RDS, etc.)
    print("1. Testing Standard AWS Tag Format (EC2, RDS, S3):")
    standard_tags = [
        {'Key': 'Name', 'Value': 'web-server-01'},
        {'Key': 'Environment', 'Value': 'production'},
        {'Key': 'Service', 'Value': 'webserver'},
        {'Key': 'Project', 'Value': 'ecommerce'},
        {'Key': 'CustomTag', 'Value': 'custom-value'}
    ]
    
    common_tags, additional_tags = extract_tags(standard_tags)
    print(f"  Common Tags: {common_tags}")
    print(f"  Additional Tags: {additional_tags}")
    print(f"  Tag Values: {get_tag_values(standard_tags)}")
    print()
    
    # Test Case 2: Lambda tag format (dict format)
    print("2. Testing Lambda Tag Format (dict):")
    lambda_tags_dict = {
        'Name': 'lambda-function-01',
        'Environment': 'staging', 
        'Service': 'api',
        'CustomLambdaTag': 'lambda-specific'
    }
    
    # Convert to standard format (as done in Lambda export)
    lambda_tags = [{'Key': k, 'Value': v} for k, v in lambda_tags_dict.items()]
    common_tags, additional_tags = extract_tags(lambda_tags)
    print(f"  Original Dict: {lambda_tags_dict}")
    print(f"  Converted: {lambda_tags}")
    print(f"  Common Tags: {common_tags}")
    print(f"  Additional Tags: {additional_tags}")
    print()
    
    # Test Case 3: ECS Cluster tag format (lowercase keys)
    print("3. Testing ECS Cluster Tag Format (lowercase keys):")
    ecs_cluster_tags = [
        {'key': 'Name', 'value': 'ecs-cluster-01'},
        {'key': 'Environment', 'value': 'development'},
        {'key': 'Service', 'value': 'container-service'},
        {'key': 'customTag', 'value': 'ecs-specific'}
    ]
    
    # This format needs conversion
    print(f"  Original ECS format: {ecs_cluster_tags}")
    # Convert lowercase to standard format
    ecs_converted_tags = [{'Key': tag.get('key', ''), 'Value': tag.get('value', '')} for tag in ecs_cluster_tags]
    print(f"  Converted to standard: {ecs_converted_tags}")
    
    common_tags, additional_tags = extract_tags(ecs_converted_tags)
    print(f"  Common Tags: {common_tags}")
    print(f"  Additional Tags: {additional_tags}")
    print()
    
    # Test Case 4: Empty tags
    print("4. Testing Empty Tags:")
    empty_tags = []
    common_tags, additional_tags = extract_tags(empty_tags)
    print(f"  Common Tags: {common_tags}")
    print(f"  Additional Tags: {additional_tags}")
    print()
    
    # Test Case 5: Case sensitivity test
    print("5. Testing Case Sensitivity:")
    case_tags = [
        {'Key': 'name', 'Value': 'lowercase-name'},  # lowercase 'name'
        {'Key': 'ENVIRONMENT', 'Value': 'UPPERCASE-ENV'},  # uppercase
        {'Key': 'Service', 'Value': 'mixed-case'}  # proper case
    ]
    
    common_tags, additional_tags = extract_tags(case_tags)
    print(f"  Tags: {case_tags}")
    print(f"  Common Tags: {common_tags}")
    print(f"  Additional Tags: {additional_tags}")
    print()
    
    # Test Case 6: Missing values
    print("6. Testing Missing/Malformed Tags:")
    malformed_tags = [
        {'Key': 'Name'},  # Missing Value
        {'Value': 'orphan-value'},  # Missing Key
        {'Key': '', 'Value': 'empty-key'},
        {'Key': 'EmptyValue', 'Value': ''},
        {'Key': 'Normal', 'Value': 'normal-value'}
    ]
    
    common_tags, additional_tags = extract_tags(malformed_tags)
    print(f"  Tags: {malformed_tags}")
    print(f"  Common Tags: {common_tags}")
    print(f"  Additional Tags: {additional_tags}")
    print()

def test_live_aws_tags():
    """Test with real AWS resources if available"""
    
    print("=== LIVE AWS TAG TEST ===\n")
    
    try:
        # Test with EC2 (if available)
        print("Testing EC2 instances tag format:")
        ec2 = boto3.client('ec2', region_name='ap-southeast-1')
        response = ec2.describe_instances(MaxResults=5)
        
        instance_count = 0
        for reservation in response.get('Reservations', [])[:2]:  # Limit to 2 reservations
            for instance in reservation.get('Instances', [])[:1]:  # Limit to 1 instance per reservation
                instance_count += 1
                instance_id = instance.get('InstanceId', 'Unknown')
                tags = instance.get('Tags', [])
                
                print(f"  Instance {instance_id}:")
                print(f"    Raw Tags: {tags}")
                
                if tags:
                    common_tags, additional_tags = extract_tags(tags)
                    print(f"    Common Tags: {common_tags}")
                    print(f"    Additional Tags: {additional_tags}")
                else:
                    print(f"    No tags found")
                print()
                
                if instance_count >= 2:  # Limit output
                    break
            if instance_count >= 2:
                break
                
    except Exception as e:
        print(f"  Could not test EC2 tags: {e}")
        print()
    
    try:
        # Test with Lambda (if available)
        print("Testing Lambda functions tag format:")
        lambda_client = boto3.client('lambda', region_name='ap-southeast-1')
        response = lambda_client.list_functions(MaxItems=3)
        
        for func in response.get('Functions', [])[:2]:  # Limit to 2 functions
            func_name = func.get('FunctionName', 'Unknown')
            tags = func.get('Tags', {})
            
            print(f"  Function {func_name}:")
            print(f"    Raw Tags (dict): {tags}")
            
            if tags:
                # Convert dict to standard format
                lambda_tags = [{'Key': k, 'Value': v} for k, v in tags.items()]
                print(f"    Converted Tags: {lambda_tags}")
                
                common_tags, additional_tags = extract_tags(lambda_tags)
                print(f"    Common Tags: {common_tags}")
                print(f"    Additional Tags: {additional_tags}")
            else:
                print(f"    No tags found")
            print()
                
    except Exception as e:
        print(f"  Could not test Lambda tags: {e}")
        print()

if __name__ == "__main__":
    print(f"Common Tag Keys Configuration: {COMMON_TAG_KEYS}\n")
    
    test_tag_formats()
    
    if len(sys.argv) > 1 and sys.argv[1] == '--live':
        test_live_aws_tags()
    else:
        print("Run with '--live' flag to test with real AWS resources")