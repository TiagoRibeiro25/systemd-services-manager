import subprocess

def get_services(filter_type):
    try:
        cmd = []

        if filter_type == "all":
            cmd = ['systemctl', 'list-units', '--type=service', '--all', '--no-pager', '--no-legend']
        elif filter_type == "running":
            cmd = ['systemctl', 'list-units', '--type=service', '--state=running', '--no-pager', '--no-legend']
        elif filter_type == "enabled":
            cmd = ['systemctl', 'list-unit-files', '--type=service', '--state=enabled', '--no-pager', '--no-legend']

        if not cmd:
            raise ValueError(f"Invalid filter_type: {filter_type}")

        output = subprocess.check_output(cmd, text=True)
        services = []
        for line in output.strip().split("\n"):
            if line:
                parts = line.split()
                name = parts[0]
                status = parts[3] if filter_type != "enabled" else parts[1]
                services.append((name, status))
        return services
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return []
    except ValueError as ve:
        print(ve)
        return []

def manage_service(action, service):
    try:
        subprocess.run(["systemctl", action, service], check=True)
        return f"{action.capitalize()}ed {service} successfully."
    except subprocess.CalledProcessError as e:
        return f"Failed to {action} {service}:\n{e}"
