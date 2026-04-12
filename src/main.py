import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from graph import build_graph

def run_research(query: str):
    print(f"\n🔍 Researching: {query}\n")
    
    graph = build_graph()
    
    result = graph.invoke({
        "query": query,
        "search_results": "",
        "analysis": "",
        "final_report": ""
    })
    
    print("📋 FINAL REPORT:")
    print("="*50)
    print(result["final_report"])
    print("="*50)

if __name__ == "__main__":
    query = "latest trends in AI agents 2025"
    run_research(query)