"""
Sample Package for API router
Alex Scotland, 2024

This file goes over the setup of a fastapi plugin.
"""
# Imports the base necessities
from fastapi import Response, APIRouter

# Assign the API Router to variable ROUTER.
# This is necessary - as in `src.routers.__init__.py` we look for `.ROUTER`
ROUTER = APIRouter(
    prefix="/sample",
    tags=["This is a sample PackageRouter"]
)


# Build your api end points as you would!
@ROUTER.get("/test/")
def test():
    return Response("Hello")

@ROUTER.get("/test_external_url/")
def test_external_url():
    import requests
    # This will return the response from the URL
    if requests.get("http://www.google.com").ok:
        return Response("Success")
    return Response("Failure")
