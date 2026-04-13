import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from graph import build_graph

app = FastAPI(title="AI Research Assistant")

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the request structure
class ResearchRequest(BaseModel):
    query: str

# Define the response structure
class ResearchResponse(BaseModel):
    report: str

@app.get("/")
def home():
    return {"message": "AI Research Assistant is running"}

@app.post("/research")
def research(request: ResearchRequest):
    graph = build_graph()
    result = graph.invoke({
        "query": request.query,
        "search_results": "",
        "analysis": "",
        "final_report": ""
    })
    return ResearchResponse(report=result["final_report"])