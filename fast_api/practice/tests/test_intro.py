from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
app = FastAPI()

@app.get('/')
async def hello():
    return {"text": "hello world!"}

class Data(BaseModel):
    string: str
    default_none: Optional[int] = None
    lists: List[int]

@app.post('/post')
async def declare_request_body(data: Data):
    return {"text": f"hello, {data.string}, {data.default_none}, {data.lists}"}

from starlette.testclient import TestClient
from intro import app

# get and assign app to create test client
client = TestClient(app)

def test_read_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"text": "hello world!"}

def test_read_declare_request_body():
    response = client.post(
        "/post",
        json={
            "string": "foo",
            "lists": [1, 2],
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "text": "hello, foo, None, [1, 2]",
    }