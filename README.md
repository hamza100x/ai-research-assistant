# 🤖 AI Research Assistant

A multi-agent AI system that autonomously researches any topic and generates a structured report using 3 specialized AI agents.

🌐 **Live Demo:** https://hamza100x-ai-research-assistant.hf.space/ui

## How It Works
User Query → Researcher Agent → Analyst Agent → Writer Agent → Structured Report


1. **Researcher Agent** → searches the web in real-time using Tavily
2. **Analyst Agent** → reads and extracts key information using Llama 3.3
3. **Writer Agent** → generates a clean structured report with Summary, Key Findings and Conclusion

## Tech Stack

| Tool | Purpose |
|---|---|
| [LangGraph](https://langchain-ai.github.io/langgraph/) | Multi-agent orchestration |
| [LangChain](https://langchain.com/) | LLM framework |
| [Groq](https://groq.com/) | Free LLM inference (Llama 3.3 70B) |
| [Tavily](https://tavily.com/) | Real-time web search for AI agents |
| [FastAPI](https://fastapi.tiangolo.com/) | REST API backend |
| [Docker](https://docker.com/) | Containerization |
| Python 3.11 | Core language |

## Run Locally

```bash
# Clone the repo
git clone https://github.com/hamza100x/ai-research-assistant.git
cd ai-research-assistant

# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows
source venv/bin/activate       # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Add your API keys
cp .env.example .env
# Edit .env with your keys

# Run
uvicorn src.main:app --reload
# Open http://127.0.0.1:7860/ui
```

## Run with Docker

```bash
docker build -t ai-research-assistant .
docker run -p 7860:7860 --env-file .env ai-research-assistant
```

## API Keys Required
- [Groq API](https://console.groq.com) — free
- [Tavily API](https://tavily.com) — free tier (1000 searches/month)

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| POST | `/research` | Run research pipeline |
| GET | `/ui` | Chat interface |

## Author
**Hamza Danish** — M.Sc. Artificial Intelligence @ BTU Cottbus-Senftenberg

- GitHub: [hamza100x](https://github.com/hamza100x)
- LinkedIn: [hamza100x](https://www.linkedin.com/in/hamza100x/)
- Email: hamzadanish453@gmail.com