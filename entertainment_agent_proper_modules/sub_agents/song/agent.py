from google.adk.agents import LlmAgent

song_agent = LlmAgent(
    name="song_agent",
    model="gemini-3.5-flash",
    instruction="""Choose a random topic and write a 4 lines song. return to entertainment agent when shared a song""",
    description="An agent which is good at writing small songs",
)
