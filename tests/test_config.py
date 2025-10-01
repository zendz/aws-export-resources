#!/usr/bin/env python3
"""
Configuration Test Script

This script tests that the configuration is properly loaded and accessible.
Run with: python3 test_config.py
"""

try:
    from config import (
        AWS_PROFILES,
        COMMON_TAG_KEYS,
        MAX_WORKERS,
        ENABLED_SERVICES,
        EXCEL_STYLING
    )
    
    print("✅ Configuration import successful!")
    print(f"📋 AWS Profiles configured: {len(AWS_PROFILES)}")
    print(f"🏷️  Common tag keys: {len(COMMON_TAG_KEYS)}")
    print(f"⚡ Max workers: {MAX_WORKERS}")
    print(f"🔧 Enabled services: {len(ENABLED_SERVICES)}")
    print(f"📊 Excel styling configured: {'Yes' if EXCEL_STYLING else 'No'}")
    
    print("\n📋 Configured AWS Profiles:")
    for i, profile in enumerate(AWS_PROFILES, 1):
        print(f"  {i}. {profile}")
    
    print("\n🏷️  Configured Tag Keys:")
    for i, tag in enumerate(COMMON_TAG_KEYS, 1):
        print(f"  {i}. {tag}")
    
    print("\n🔧 Enabled Services:")
    for i, service in enumerate(ENABLED_SERVICES, 1):
        print(f"  {i}. {service}")
        
    print("\n✅ Configuration test completed successfully!")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("📝 Make sure config.py exists and is properly formatted")
    
except Exception as e:
    print(f"❌ Configuration error: {e}")
    print("📝 Check your config.py file for syntax errors")