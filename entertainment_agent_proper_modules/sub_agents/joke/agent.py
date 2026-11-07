from google.adk.agents import LlmAgent

joke_agent = LlmAgent(
    name="joke_agent",
    model="gemini-3.5-flash",        
    instruction="""Tell a joke when asked.return to entertainment agent when shared a joke""",
    description="An agent which create jokes",
    )
