from pydantic import BaseModel
from uuid import UUID

class ID(BaseModel):
    id: int

class UUID(BaseModel):
    uuid: UUID