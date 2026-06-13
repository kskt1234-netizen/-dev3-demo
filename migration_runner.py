import subprocess

def run_migration(script_path: str):
    result = subprocess.run(["python", script_path], capture_output=True, check=True)
    return result.stdout
