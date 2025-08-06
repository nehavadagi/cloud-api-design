from fastapi import APIRouter, HTTPException
from datetime import datetime
from .schemas import UserCreate, NoteCreate, NoteOut

router = APIRouter()

# Initialize with sample data
fake_db = {
    "notes": {
        1: {
            "id": 1,
            "title": "First Note",
            "content": "This is a sample note",
            "owner_email": "test@example.com",
            "created_at": datetime.now().isoformat()
        }
    },
    "users": {}
}

@router.post("/register", response_model=UserCreate)
async def register_user(user: UserCreate):
    if user.email in fake_db["users"]:
        raise HTTPException(400, "Email already registered")
    fake_db["users"][user.email] = user.dict()
    return user

@router.get("/notes/{note_id}", response_model=NoteOut)
async def get_note(note_id: int):  # <-- This enforces integer validation
    if note_id not in fake_db["notes"]:
        raise HTTPException(404, "Note not found")
    return fake_db["notes"][note_id]