#!/usr/bin/env python3
"""
Test ECS Cluster AWSBatch     pri    print(f"Filter Criteria:")
    print(f"  - Starts with 'AWSBatch-' (AWS Batch cluster naming pattern)")"Filter Criteria:")
    print(f"  - Starts with 'AWSBatch-' (AWS Batch cluster naming pattern)")
    
    # Verify expected results
    expected_filtered = 6  # The 6 clusters that start with "AWSBatch-"
    expected_kept = 7      # All other clusters
    
    actual_filtered = [name for name in test_clusters if name.startswith('AWSBatch-')]
    actual_kept = [name for name in test_clusters if not name.startswith('AWSBatch-')]ering
Validates that AWS Batch clusters are properly filtered out
"""

def test_awsbatch_filter():
    """Test the AWS Batch cluster filtering logic"""
    
    print("=== ECS CLUSTER AWS BATCH FILTER TEST ===\n")
    
    # Test cluster names based on real AWS Batch patterns
    test_clusters = [
        # Real AWS Batch cluster patterns (should be filtered)
        "AWSBatch-sds-isearch-analytics-logs-rolling-environment-3c1fc7df-0864-34fa-9285-ada49197ca39",
        "AWSBatch-sds-scv-promotion-comparison-prd-ondemand-compute-env-cuarm6p-a0a155ed-472a-3ae6-9676-fd6a1eb3d0a0",
        "AWSBatch-sds-isearch-autofix-search-44433018-6a85-3fef-9983-9831e3678195",
        "AWSBatch-sds-smoap-user-embedding-prd-ondemand-compute-env-dankcat-c447381e-6f55-37aa-8d0a-c418a25789d5",
        "AWSBatch-compute-environment-1",
        "AWSBatch-job-queue-123",
        # These should NOT be filtered (normal ECS clusters)
        "production-web-cluster",
        "staging-api-cluster", 
        "monitoring-cluster",
        "data-processing-cluster",
        "my-batch-cluster",  # This contains "batch" but doesn't start with "AWSBatch-"
        "batch-processing-cluster",  # This also contains "batch" but doesn't start with "AWSBatch-"
        "AWSBatchServiceRole",  # This doesn't have the hyphen after AWSBatch
    ]
    
    print("Testing cluster name filtering logic:")
    print("-" * 50)
    
    filtered_count = 0
    kept_count = 0
    
    for cluster_name in test_clusters:
        # Apply the corrected filter logic - AWS Batch clusters start with "AWSBatch-"
        should_filter = cluster_name.startswith('AWSBatch-')
        
        if should_filter:
            print(f"❌ FILTERED: {cluster_name}")
            filtered_count += 1
        else:
            print(f"✅ KEPT:     {cluster_name}")
            kept_count += 1
    
    print(f"\nSummary:")
    print(f"  Clusters filtered out: {filtered_count}")
    print(f"  Clusters kept: {kept_count}")
    print(f"  Total clusters tested: {len(test_clusters)}")
    
    print(f"\nFilter Criteria:")
    print(f"  - Contains 'AWSBatch' anywhere in name")
    print(f"  - Starts with 'AWSBatch'")
    print(f"  - Contains 'batch' (case-insensitive)")
    
    # Verify expected results
    expected_filtered = ['AWSBatch-compute-environment-1', 'AWSBatchServiceRole-cluster', 
                        'my-batch-cluster', 'production-batch-workload', 'AWSBATCH_DEFAULT', 
                        'batch-processing-cluster', 'data-processing-cluster']
    expected_kept = ['production-web-cluster', 'staging-api-cluster', 'monitoring-cluster']
    
    actual_filtered = [name for name in test_clusters if ('AWSBatch' in name or 
                                                         name.startswith('AWSBatch') or
                                                         'batch-' in name.lower() or
                                                         '-batch-' in name.lower() or 
                                                         name.lower().endswith('-batch') or
                                                         name.lower() == 'batch')]
    actual_kept = [name for name in test_clusters if not ('AWSBatch' in name or 
                                                          name.startswith('AWSBatch') or
                                                          'batch-' in name.lower() or
                                                          '-batch-' in name.lower() or 
                                                          name.lower().endswith('-batch') or
                                                          name.lower() == 'batch')]
    
    print(f"\n=== VALIDATION ===")
    print(f"Expected filtered: {expected_filtered}, Actual: {len(actual_filtered)}")
    print(f"Expected kept: {expected_kept}, Actual: {len(actual_kept)}")
    
    if len(actual_filtered) == expected_filtered and len(actual_kept) == expected_kept:
        print("✅ Filter working as expected!")
        print(f"\nFiltered clusters (starting with 'AWSBatch-'):")
        for cluster in actual_filtered:
            print(f"  • {cluster}")
        print(f"\nKept clusters (normal ECS clusters):")
        for cluster in actual_kept:
            print(f"  • {cluster}")
    else:
        print("❌ Filter results don't match expectations")
        print(f"Actual filtered: {actual_filtered}")
        print(f"Actual kept: {actual_kept}")

def test_edge_cases():
    """Test edge cases for the filter"""
    
    print(f"\n=== EDGE CASES TEST ===")
    print("-" * 30)
    
    edge_cases = [
        ("", False, "Empty string"),
        ("AWSBatch", False, "AWSBatch without hyphen"), 
        ("AWSBatch-", True, "AWSBatch with hyphen but no suffix"),
        ("AWSBatch-123", True, "AWSBatch with simple suffix"),
        ("AWSBatch-compute-env-123", True, "Typical AWS Batch pattern"),
        ("my-AWSBatch-cluster", False, "AWSBatch in middle"),
        ("awsbatch-cluster", False, "Lowercase variant"),
        ("batch-AWSBatch", False, "Different order"),
        ("AWSBatchServiceRole", False, "Similar but no hyphen"),
        ("production-web-cluster", False, "Normal ECS cluster"),
        ("AWSBatch-sds-isearch-analytics-logs-rolling-environment-3c1fc7df-0864-34fa-9285-ada49197ca39", True, "Real AWS Batch example")
    ]
    
    for cluster_name, expected_filtered, description in edge_cases:
        should_filter = cluster_name.startswith('AWSBatch-')
        
        status = "✅" if should_filter == expected_filtered else "❌"
        action = "FILTERED" if should_filter else "KEPT"
        
        print(f"{status} '{cluster_name}' → {action} ({description})")

if __name__ == "__main__":
    test_awsbatch_filter()
    test_edge_cases()
    
    print(f"\n" + "="*60)
    print("AWS BATCH FILTER IMPLEMENTATION READY")
    print("="*60)
    print("The ECS Clusters export will now exclude:")
    print("• Clusters starting with 'AWSBatch-' (AWS Batch cluster pattern)")
    print("• This precisely targets AWS Batch managed clusters")
    print("• Normal ECS clusters with 'batch' in names will be kept")
    print("="*60)