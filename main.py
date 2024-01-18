# status_handler.py for CONNECTIVITY
 
# run with: uvicorn status_handler:app
 
from fastapi import FastAPI, Header
from pydantic import BaseModel
 
from typing_extensions import Annotated
from typing import Union
 
app = FastAPI()
 
class ConnectivityEventDetail(BaseModel):
    deviceStatus: str
 
class Event(BaseModel):
    eventType: str
    eventTime: str
    eventDetail: ConnectivityEventDetail
 
class Notification(BaseModel):
    eventSubscriptionId: str
    event: Event
 

@app.get("/test")
def test():
   return {"message": "Hello, world"}


@app.post("/notifications")
def receive_notification(notification: Notification,
                         authorization: Annotated[Union[str, None], Header]):
    if authorization == "Bearer nacauth":
      if notification.event.eventDetail.deviceStatus == "REACHABLE":
        print("Device is available")
      elif notification.event.eventDetail.deviceStatus == "UNREACHABLE":
        print("Device is not available")