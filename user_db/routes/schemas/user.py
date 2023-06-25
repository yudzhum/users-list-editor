from pydantic import BaseModel, Extra


class UserBase(BaseModel):
    name: str
    group: str


class UserCreateOrUpdate(UserBase):
    password: str


class UserOut(UserBase):
    class Config:
        extra = Extra.forbid

    id: int

