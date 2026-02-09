from pydantic import BaseModel, Field
from typing import Optional


class AddressBase(BaseModel):
    name: str = Field(..., example="Your name")
    street: str = Field(..., example="Your Street")
    city: str = Field(..., example="Your City")
    latitude: float = Field(..., ge=-90, le=90, example=19.0760)
    longitude: float = Field(..., ge=-180, le=180, example=72.8777)


class AddressCreate(AddressBase):
    pass


class AddressUpdate(BaseModel):
    name: Optional[str]
    street: Optional[str]
    city: Optional[str]
    latitude: Optional[float] = Field(None, ge=-90, le=90)
    longitude: Optional[float] = Field(None, ge=-180, le=180)


class AddressResponse(AddressBase):
    id: int

    class Config:
        orm_mode = True
