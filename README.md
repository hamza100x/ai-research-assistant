---
title: AI Research Assistant
emoji: 🤖
colorFrom: purple
colorTo: blue
sdk: docker
pinned: false
---

# 🤖 AI Research Assistant

A multi-agent AI system that autonomously researches any topic and generates a structured report.

## How it works
1. **Researcher Agent** → searches the web using Tavily
2. **Analyst Agent** → extracts key information from results
3. **Writer Agent** → generates a clean structured report

## Tech Stack
- [LangGraph](https://langchain-ai.github.io/langgraph/) — multi-agent orchestration
- [LangChain](https://langchain.com/) — LLM framework
- [Groq](https://groq.com/) — free LLM inference (Llama 3.3 70B)
- [Tavily](https://tavily.com/) — web search for AI agents
- Python 3.13

## Run Locally

```bash
# Clone the repo
git clone https://github.com/hamza100x/ai-research-assistant.git
cd ai-research-assistant

# Create virtual environment
python -m venv venv
source venv/Scripts/activate

# Install dependencies
pip install langgraph langchain langchain-groq langchain-tavily fastapi uvicorn python-dotenv

# Add your API keys
cp .env.example .env
# Edit .env with your GROQ_API_KEY and TAVILY_API_KEY

# Run
python src/main.py
```

## API Keys needed
- [Groq API](https://console.groq.com) — free
- [Tavily API](https://tavily.com) — free tier

## Author
Hamza Danish — [GitHub](https://github.com/hamza100x) | [LinkedIn](https://www.linkedin.com/in/hamza100x/)