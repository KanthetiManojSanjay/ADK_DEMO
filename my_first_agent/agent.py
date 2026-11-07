from google.adk.agents import Agent


def morning_greet(name: str) -> str:
    return f"Good Morning, {name}! How can I assist you today? My mood is amazing"


def evening_greet(name: str) -> str:
    return f"Good Evening, {name}! My mood is bit low"


root_agent = Agent(
    name="my_first_agent",
    model="gemini-3.5-flash",
    description="An example agent that will answer user query related to Google Cloud",
    instruction="""
    First ask user the name and start conversation by greeting based on greet.
    If user says Good Morning, use morning_greet to greet user
    If user says Good Evening, use evening_greet to greet user
    """,
    tools=[morning_greet, evening_greet])
