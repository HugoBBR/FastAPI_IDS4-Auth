from configparser import ConfigParser
import os
from fastapi import FastAPI,Depends,Response,status,Security
from fastapi.security import OAuth2AuthorizationCodeBearer,OpenIdConnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi import docs
import urllib.parse
from validator import VerifyToken
from fastapi_auth0 import Auth0, Auth0User
from dotenv import load_dotenv

load_dotenv()

auth0Domain = os.getenv('AUTH0_DOMAIN')
auth0APIAudince=os.getenv('AUTH0_API_AUDIENCE')
print(auth0Domain)
swagger_init_oauth={"clientID":"FastAPI_POC_Swagger"}


auth=Auth0(domain=auth0Domain,api_audience=auth0APIAudince,scopes={'api:read':''})
app = FastAPI(swagger_ui_init_oauth=swagger_init_oauth)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/user",dependencies=[Depends(auth.implicit_scheme)])
async def get_user(user:Auth0User=Security(auth.get_user, scopes=['api:read'])):
    return {"message":f'{user}'}

@app.get("/info",dependencies=[Depends(auth.implicit_scheme)])
async def get_info(user:Auth0User=Security(auth.get_user, scopes=['api:read'])):
    return "This is data from the api"

@app.get("/token/")
async def read_items(token: str = Depends(auth.implicit_scheme)):
    return {"token": token}

