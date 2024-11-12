import os

ALL_ROUTERS_TO_INSTALL = []
CURRENT_DIRECTORY = "lib"

for package_directory in os.scandir(os.path.dirname(__file__)):
    if not package_directory.is_dir() or package_directory.name.startswith("__"):
        continue
    for router in os.scandir(f"{package_directory.path}/routers"):
        if router.name.startswith("__"):
            continue
        ALL_ROUTERS_TO_INSTALL.append(f"{CURRENT_DIRECTORY}.{package_directory.name}.routers.{router.name}")