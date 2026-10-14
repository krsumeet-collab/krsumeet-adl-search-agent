from google.adk.artifacts import InMemoryArtifactService
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from google.adk.agents import LlmAgent

from .prompt import ADL_SEARCH_AGENT_PROMPT
from .adl_tool import adl_connector_tool

MODEL = "gemini-2.5-pro"

adl_search_agent = LlmAgent(
    name="adl_search_agent",
    model=MODEL,
    description="""
    **Data Retrieval Agent for Azure Data lake Synapse**
    """,
    instruction=ADL_SEARCH_AGENT_PROMPT,
    tools=[adl_connector_tool]
)

root_agent = adl_search_agent