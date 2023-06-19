from pydantic import BaseModel


class UserCreateOrUpdate(BaseModel):
    name: str
    group: str
    password: str

