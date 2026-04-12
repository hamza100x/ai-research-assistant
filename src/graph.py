from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, AIMessage
from agents import get_llm
from tools import get_search_tool
from typing import TypedDict, List
from dotenv import load_dotenv

load_dotenv()

# Define the state - this is shared between all agents
class ResearchState(TypedDict):
    query: str
    search_results: str
    analysis: str
    final_report: str

# Node 1 - Researcher
def researcher_node(state: ResearchState):
    search_tool = get_search_tool()
    results = search_tool.invoke(state["query"])
    
    # Convert results to string
    results_text = str(results)
    
    return {"search_results": results_text}

# Node 2 - Analyst
def analyst_node(state: ResearchState):
    llm = get_llm()
    
    prompt = f"""You are a research analyst. 
    Analyze these search results about: {state["query"]}
    
    Search Results:
    {state["search_results"]}
    
    Extract the most important and relevant information."""
    
    response = llm.invoke([HumanMessage(content=prompt)])
    return {"analysis": response.content}

# Node 3 - Writer
def writer_node(state: ResearchState):
    llm = get_llm()
    
    prompt = f"""You are a professional report writer.
    Write a clear and structured report about: {state["query"]}
    
    Based on this analysis:
    {state["analysis"]}
    
    Format it with sections: Summary, Key Findings, Conclusion."""
    
    response = llm.invoke([HumanMessage(content=prompt)])
    return {"final_report": response.content}

# Build the graph
def build_graph():
    graph = StateGraph(ResearchState)
    
    # Add nodes
    graph.add_node("researcher", researcher_node)
    graph.add_node("analyst", analyst_node)
    graph.add_node("writer", writer_node)
    
    # Add edges
    graph.set_entry_point("researcher")
    graph.add_edge("researcher", "analyst")
    graph.add_edge("analyst", "writer")
    graph.add_edge("writer", END)
    
    return graph.compile()