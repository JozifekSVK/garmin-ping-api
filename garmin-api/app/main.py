import pandas as pd
from fastapi import FastAPI

from app.modules import db_handler, fit_files_downloaded


app = FastAPI()

@app.post("/fit-file")
async def receive_data(request_data: dict) -> dict:
    
    df = {
        "userId":[],
        "userAccessToken":[],
        "summaryId":[],
        "fileType":[],
        "callbackURL":[],
        "startTimeInSeconds":[],
        "activityId":[],
        "activityType":[],
        "activityName":[],
        "manual":[]
    }

    for activity in request_data["activityFiles"]:

        print(activity)
        print(df)
        for key in activity.keys():
            df[key].append(activity[key])

    df = pd.DataFrame(df)
    print(df)

    db_handler.warehouse_ch_load(df)
    fit_files_downloaded.download_data(df)
    
    return {
        "msg": "we got data succesfully"
    }

@app.get("/")
async def read_root():

    return {"Hello": "this is garmin connect api"}
