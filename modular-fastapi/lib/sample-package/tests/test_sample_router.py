from fastapi import FastAPI
from fastapi.testclient import TestClient
from ..routers.sample_router import ROUTER

# This will create a FastAPI instance of just the router
temp_app = FastAPI()
temp_app.include_router(ROUTER)

client = TestClient(temp_app)


def test_sample_router():
    response = client.get(f"{ROUTER.prefix}/test/")
    assert response.status_code == 200
