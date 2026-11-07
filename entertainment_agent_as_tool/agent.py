from google.adk.agents import LlmAgent
from .sub_agents.joke import joke_agent
from .sub_agents.song import song_agent
from .sub_agents.story import story_agent
from google.adk.tools.agent_tool import AgentTool

# Define the root  agent
root_agent = LlmAgent(
    name="entertainment_agent",
    model="gemini-3.5-flash",
    instruction="""You are a entertainer which uses other available agents to write stories, songs or jokes 
         Instructions:
         - Please greet the user and offer the services you provide and ask for thier choice
         - Based on user preference use of the sub agents to get the output and present to the user""",
    description="An agent which entertains people with songs, stories or jokes",
    # sub agents are called as function calls so that subagents just does the job and return
    # the output to the root agent and dont think beyond that.
    # The root agent is the one which interacts with the user and provides the output to the user
    tools=[
        AgentTool(agent=joke_agent),
        AgentTool(agent=song_agent),
        AgentTool(agent=story_agent),
    ],
)
