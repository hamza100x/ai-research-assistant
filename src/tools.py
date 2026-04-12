from langchain_tavily import TavilySearch
from dotenv import load_dotenv
import os

load_dotenv()

def get_search_tool():
    search = TavilySearch(
        max_results=5,
        tavily_api_key=os.getenv("TAVILY_API_KEY")
    )
    return search