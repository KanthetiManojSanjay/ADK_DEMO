from google.adk.agents import LlmAgent

story_agent = LlmAgent(
    name="story_agent",
    model="gemini-3.5-flash",    
    instruction="""Choose a random topic and write a 10 lines story. return to entertainment agent when shared a story""",
    description="An agent which is good at writing small stories",
    )
