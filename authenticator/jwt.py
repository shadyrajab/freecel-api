from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from client.instance import client
from fastapi import HTTPException, Depends

security = HTTPBearer()

def authenticate(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials:
        token = credentials.credentials
        if client.jwt_authenticate(token):
            return True

    raise HTTPException(status_code=401, detail="Autenticação necessária")