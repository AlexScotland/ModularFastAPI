import os
import subprocess

def install_dependencies_for_plugin(folder) -> None:
    """Install plugin dependencies dynamically."""
    folder_converted = folder.replace(".",os.sep)
    if not os.path.isdir(folder_converted):
        return
    requirements_path = os.path.join(folder_converted, "requirements.txt")
    if os.path.isfile(requirements_path):
        print(f"Installing dependencies for {folder_converted}")
        try:
            subprocess.run(
                ["pip", "install", "--no-cache-dir", "-r", requirements_path],
                check=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Failed to install dependencies for {folder_converted}: {e}")


def get_all_routers() -> list:
    all_routers = []
    current_directory = os.path.dirname(__file__).split(os.sep)[-1]
    for package_directory in os.scandir(os.path.dirname(__file__)):
        if not package_directory.is_dir() or package_directory.name.startswith("__"):
            continue
        for router in os.scandir(f"{package_directory.path}/routers"):
            if router.name.startswith("__"):
                continue
            all_routers.append(f"{current_directory}.{package_directory.name}.routers.{router.name}")
    return all_routers