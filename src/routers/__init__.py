import importlib
import os

from fastapi import APIRouter

from lib import ALL_ROUTERS_TO_INSTALL

__globals = globals()

from routers.main import MAIN_ROUTER

def _get_routes_from_package_file(package_file):
    all_routers_to_import = []
    for obj_attribute in dir(package_file):
        if obj_attribute.startswith("__"):
            continue
        imported_attribute = getattr(package_file, obj_attribute)
        if isinstance(imported_attribute, APIRouter) and getattr(imported_attribute, 'routes'):
            all_routers_to_import.append(imported_attribute)
    return all_routers_to_import

# Dynamically import all routers
for package_routers in ALL_ROUTERS_TO_INSTALL:
    __globals[package_routers[:-3]] = importlib.import_module(package_routers[:-3], package=__name__)
    for router in _get_routes_from_package_file(__globals[package_routers[:-3]]):
        MAIN_ROUTER.include_router(router)
