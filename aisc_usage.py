import subprocess
import json

# Run sinfo command and get output
output = subprocess.check_output("sinfo -p aisc -N -o '%all' --noheader --Format=NodeHost,Features --json", shell=True)

# Convert JSON output to Python data structure
data = json.loads(output)

# Iterate over nodes and print only those that belong to 'aisc' partition
for node in data["nodes"]:
    if 'aisc' in node['partitions']:
        print(f"Node Name: {node['name']}")
        print(f"Architecture: {node['architecture']}")
        print(f"Number of Cores: {node['cores']}")
        print(f"CPU Load: {node['cpu_load']}")
        print(f"Memory Free: {node['free_memory']} MB")
        print(f"State: {node['state']}")
        print(f"Operating System: {node['operating_system']}")
        print(f"Partitions: {', '.join(node['partitions'])}")
        print(f"Allocated Memory: {node['alloc_memory']} MB")
        print(f"Allocated CPUs: {node['alloc_cpus']}")
        print(f"Idle CPUs: {node['idle_cpus']}")
        print(f"Generic Resources (GRES): {node['gres']}")
        print(f"GRES Used: {node['gres_used']}")
        print("---\n")

