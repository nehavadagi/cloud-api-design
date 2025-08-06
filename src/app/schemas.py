from datetime import datetime
from pydantic import BaseModel
from typing import Optional

# Fallback for EmailStr if email-validator not available
try:
    from pydantic import EmailStr
except ImportError:
    class EmailStr(str):
        @classmethod
        def __get_validators__(cls):
            yield cls.validate

        @classmethod
        def validate(cls, v):
            if "@" not in v:
                raise ValueError("Invalid email format")
            return v

class UserBase(BaseModel):
    email: str  # Changed from EmailStr for compatibility

class UserCreate(UserBase):
    password: str

class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteOut(NoteBase):
    id: int
    created_at: datetime
    owner_email: str  # Changed from EmailStr