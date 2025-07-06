import uvicorn
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware  # Fixed import path
from pydantic import BaseModel
from typing import List

app = FastAPI()