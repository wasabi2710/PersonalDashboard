import psutil

def get_system_resources():
    cpu_percent = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent

    resource_data = {
        "cpu_percent": cpu_percent,
        "memory_percent": memory_usage,
    }

    return resource_data