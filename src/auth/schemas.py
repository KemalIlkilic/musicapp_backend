from pydantic import BaseModel, Field


class UserCreateModel(BaseModel):
    name: str = Field(max_length=25)
    email : str = Field(max_length=50)
    password : str = Field(min_length=4)


class UserLoginModel(BaseModel):
        email : str = Field(max_length=50)
        password : str = Field(min_length=4)
