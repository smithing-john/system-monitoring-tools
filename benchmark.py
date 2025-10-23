#!/usr/bin/env python3
"""
Performance benchmarking utility
Compare system performance across different configurations
"""

import psutil
import time
from datetime import datetime

def cpu_benchmark(duration=10):
    """Run CPU benchmark test"""
    print(f"Running CPU benchmark for {duration} seconds...")
    
    results = []
    start_time = time.time()
    
    while time.time() - start_time < duration:
        cpu = psutil.cpu_percent(interval=0.5)
        results.append(cpu)
    
    avg_cpu = sum(results) / len(results)
    max_cpu = max(results)
    min_cpu = min(results)
    
    print(f"\nCPU Benchmark Results:")
    print(f"  Average: {avg_cpu:.2f}%")
    print(f"  Maximum: {max_cpu:.2f}%")
    print(f"  Minimum: {min_cpu:.2f}%")
    
    return avg_cpu

def memory_stress_test(iterations=100):
    """Run memory stress test"""
    print(f"\nRunning memory stress test ({iterations} iterations)...")
    
    data_blocks = []
    mem_before = psutil.virtual_memory().percent
    
    for i in range(iterations):
        # Allocate 10MB blocks
        data_blocks.append(bytearray(10 * 1024 * 1024))
        if i % 10 == 0:
            print(f"  Iteration {i}/{iterations}")
    
    mem_after = psutil.virtual_memory().percent
    mem_increase = mem_after - mem_before
    
    print(f"\nMemory Stress Test Results:")
    print(f"  Memory before: {mem_before:.2f}%")
    print(f"  Memory after: {mem_after:.2f}%")
    print(f"  Increase: {mem_increase:.2f}%")
    
    # Cleanup
    data_blocks.clear()
    
    return mem_increase

def disk_io_test(file_size_mb=100):
    """Run disk I/O test"""
    print(f"\nRunning disk I/O test ({file_size_mb}MB file)...")
    
    test_file = 'benchmark_test.tmp'
    data = bytearray(file_size_mb * 1024 * 1024)
    
    # Write test
    start = time.time()
    with open(test_file, 'wb') as f:
        f.write(data)
    write_time = time.time() - start
    write_speed = file_size_mb / write_time
    
    # Read test
    start = time.time()
    with open(test_file, 'rb') as f:
        _ = f.read()
    read_time = time.time() - start
    read_speed = file_size_mb / read_time
    
    print(f"\nDisk I/O Test Results:")
    print(f"  Write speed: {write_speed:.2f} MB/s")
    print(f"  Read speed: {read_speed:.2f} MB/s")
    
    # Cleanup
    import os
    os.remove(test_file)
    
    return write_speed, read_speed

def run_full_benchmark():
    """Run complete system benchmark"""
    print("="*60)
    print("SYSTEM PERFORMANCE BENCHMARK")
    print("="*60)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    cpu_score = cpu_benchmark()
    mem_score = memory_stress_test(50)
    write_speed, read_speed = disk_io_test(50)
    
    print("\n" + "="*60)
    print("BENCHMARK COMPLETE")
    print("="*60)

if __name__ == "__main__":
    run_full_benchmark()