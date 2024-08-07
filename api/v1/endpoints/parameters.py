from fastapi import APIRouter, HTTPException, Response
from bson import json_util
from typing import List
from models.testdata import TestData
from services.docker_service import create_user, run_docker_container
from db.session import collection
import webbrowser

router = APIRouter()


@router.post("/send-parameters/")
async def post_parameter(data: List[TestData]):
    user = create_user()
    for item in data:
        item.userId = user.userId
    print(user.userId)

    container_id = run_docker_container(
        user.userId, data[0].virtualUsers, data[0].testDuration
    )

    data_dicts = [item.dict() for item in data]
    await collection.insert_many(data_dicts)
    print(data_dicts)
    print(container_id)
    newData = [str(element) for element in data_dicts]
    return {"userId": newData}


@router.get("/get-parameters/{userId}")
async def get(userId: str):
    items = await collection.find({"userId": userId}).to_list(length=None)
    items = json_util.dumps(items)
    return Response(content=items, media_type="application/json")


@router.post("/open-dashboard/")
async def open_dashboard():
    webbrowser.open(
        "http://localhost:8061/d/edktnuemfuc5cb/k6-load-testing-results?orgId=1&refresh=5s&var-Measurement=All"
    )
    return {"message": "Dashboard opened in browser"}
