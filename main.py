from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Zenether Dictionary API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Word(BaseModel):
    id: int
    english: str
    zenether: str
    pos: str
    pronunciation: str
    notes: Optional[str] = None
    theme: Optional[str] = None
    frequency: Optional[int] = None

# Sample dictionary (expandable)
dictionary = [
    Word(id=1, english="light", zenether="azha", pos="noun", pronunciation="AH-zha", notes="Sacred, creation word", theme="cosmos", frequency=1),
    Word(id=2, english="speak", zenether="vera", pos="verb", pronunciation="VEH-ra", notes="to say", theme="communication", frequency=2),
    Word(id=3, english="star", zenether="janu", pos="noun", pronunciation="YAH-nu", notes="celestial", theme="celestial", frequency=3),
]

@app.get("/words/", response_model=List[Word])
def get_words():
    return dictionary

@app.get("/words/search/", response_model=List[Word])
def search_words(q: str = Query(...)):
    return [w for w in dictionary if q.lower() in w.english.lower() or q.lower() in w.zenether.lower()]

@app.get("/words/{word_id}/", response_model=Word)
def get_word(word_id: int):
    return next(w for w in dictionary if w.id == word_id)

@app.get("/themes/", response_model=List[str])
def get_themes():
    return list({w.theme for w in dictionary if w.theme})
