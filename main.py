from fastapi import FastAPI,Depends
from fastapi.security import OAuth2AuthorizationCodeBearer,OpenIdConnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi import docs



swagger_init_oauth={"clientID":"FastAPI_POC_Swagger"}
scopesIDS={
    "FastAPI":"FastAPI"
}

oauth2_scheme=OAuth2AuthorizationCodeBearer(tokenUrl="https://webapi-auth-server-dev.azurewebsites.net/connect/token",authorizationUrl="https://webapi-auth-server-dev.azurewebsites.net/connect/authorize",scopes=scopesIDS)
app = FastAPI(dependencies=[Depends(oauth2_scheme)],swagger_ui_init_oauth=swagger_init_oauth)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/info")
async def get_info():
    return "This is data from the API"


@app.get("/token/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
