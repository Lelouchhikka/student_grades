from pydantic import BaseModel

class ScoreBase(BaseModel):
    subject: str
    score: int

class ScoreCreate(ScoreBase):
    student_id: int

class Score(ScoreBase):
    id: int
    student_id: int

    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    name: str
    age: int
    grade: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    scores: list[Score] = []

    class Config:
        orm_mode = True
