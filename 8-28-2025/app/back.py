from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles



# Create FastAPI app
app = FastAPI()

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

# Enable CORS so frontend (HTML/JS) can call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins (change for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data model for numbers
class Numbers(BaseModel):
    a: int
    b: int

# Root route
@app.get("/")
def home():
    return {"message": "FastAPI backend is running!"}

# Add numbers route
@app.post("/add")
def add_numbers(nums: Numbers):
    return {"result": nums.a + nums.b}
