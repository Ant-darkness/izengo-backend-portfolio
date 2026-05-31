from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from dotenv import load_dotenv
import os

load_dotenv()


from data import (
    PROFILE,
    ABOUT,
    SKILLS,
    PROJECTS,
    QUALIFICATIONS,
    CONTACT
)

app = FastAPI(
    title="Portfolio API",
    version="1.0.0"
)


FRONTEND_URL = os.getenv("FRONTEND_URL")

origins = []

if FRONTEND_URL:
    origins.append(FRONTEND_URL)

# ALWAYS allow localhost for development
origins.append("http://localhost:5173")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Portfolio API Running"
    }


@app.get("/api/profile")
def get_profile():
    return PROFILE


@app.get("/api/about")
def get_about():
    return ABOUT


@app.get("/api/skills")
def get_skills():
    return SKILLS


@app.get("/api/projects")
def get_projects():
    return PROJECTS


@app.get("/api/qualifications")
def get_qualifications():
    return QUALIFICATIONS


@app.get("/api/contact")
def get_contact():
    return CONTACT


@app.get("/api/resume")
def check_resume():
    return {
        "available": True
    }


@app.get("/api/resume/download")
def download_resume():
    return FileResponse(
        path="resume.pdf",
        filename="Izengo_Maganga_CV.pdf",
        media_type="application/pdf"
    )
