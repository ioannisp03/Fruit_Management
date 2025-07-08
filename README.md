Fruit Management App
A simple web application for managing a fruit inventory built with FastAPI and React.

Features
Add fruits to the inventory
View all fruits in a clean list
Real-time updates when adding new items
RESTful API backend
Responsive frontend interface
Tech Stack
Backend: FastAPI, Pydantic, Uvicorn
Frontend: React, Axios, Vite
Data: In-memory storage
CORS: Cross-origin support enabled
Project Structure
Quick Start
Backend: cd backend && pip install -r [requirements.txt] && python main.py

Frontend: cd frontend && npm install && npm run dev

API Testing: Use the included test_api.http file

API Endpoints
GET /fruits - Get all fruits
POST /fruits - Add a new fruit
