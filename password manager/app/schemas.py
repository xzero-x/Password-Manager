from pydantic import BaseModel

class CredentialBase(BaseModel):
    service_name: str


class CredentialCreate(CredentialBase):
    username: str
    password: str

class Credential(CredentialBase):
    id: int
    owner_id: int

    class Config:
        orm_mode: True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode: True