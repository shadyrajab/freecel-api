from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from client.client import Client
from fastapi import HTTPException, Depends

security = HTTPBearer()

async def authenticate(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials:
        token = credentials.credentials
        async with Client() as client:
            if await client.jwt_authenticate(token):
                return True

    raise HTTPException(status_code=401, detail="Autenticação necessária")