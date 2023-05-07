from langchain.serpapi import SerpAPIWrapper
from langchain.agents import tool


@tool
def get_profile_url(text: str) -> str:
    """Search for a LinkedIn profile URL from text."""
    search = SerpAPIWrapper()
    response = search.run(f"{text}")
    return response
