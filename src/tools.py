from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv
import os

load_dotenv()

def get_search_tool():
    search = TavilySearchResults(
        max_results=5,
        tavily_api_key=os.getenv("TAVILY_API_KEY")
    )
    return search