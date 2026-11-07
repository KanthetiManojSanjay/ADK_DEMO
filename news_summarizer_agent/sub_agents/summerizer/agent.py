from google.adk.agents import LlmAgent

summarizer_agent = LlmAgent(
    name="summarizer_agent_agent",
    model="gemini-3.5-flash",
    # instruction="""Summarize the content shared by the previous agent and provide a summary in maximum 300 words""",
    instruction="""Summarize the content {{news_output}} and provide a summary in maximum 300 words""",
    description="An agent which is good at summarizing content shared with it",
)
