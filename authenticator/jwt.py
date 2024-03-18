from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from client.client import Client

security = HTTPBearer()


async def authenticate(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials:
        token = credentials.credentials
        async with Client() as client:
            user = await client.jwt_authenticate(token)
            if user:
                return user

    raise HTTPException(status_code=401, detail="Autenticação necessária")
