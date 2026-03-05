import psutil
import time

def get_system_metrics():
    return {
        "cpu_usage_percent": psutil.cpu_percent(),
        "memory_usage_percent": psutil.virtual_memory().percent,
        "disk_usage_percent": psutil.disk_usage('/').percent,
        "active_processes": len(psutil.pids()),
        "timestamp": time.time()
    }
