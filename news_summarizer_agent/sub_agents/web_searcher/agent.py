from google.adk import Agent
from google.adk.tools import google_search

# Define the agent
news_reader_agent = Agent(
    name="news_reader_agent",
    model="gemini-3.5-flash",
    description="An agent who checks in internet and gathers the latest news ",
    instruction="""You are a news researcher. When given a topic, search the web using the tools provided and return the results..""",
    tools=[google_search],
    # news_output outputkey is stored as state which can be viewed in adk web and this key is used in summarizer agent
    output_key='news_output',
)
