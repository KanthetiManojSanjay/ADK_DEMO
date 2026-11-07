from google.adk.agents import LlmAgent

# Define the agent
root_agent = LlmAgent(
    name="history_agent",
    model="gemini-3.5-flash",
    instruction="When asked about a topic, summarize the answer in bullet points and provide a 5 lines crisp summary at the end",
    description="An agent that helps with history lessons",
)
