from crewai import Crew, Process
from agents import blog_researcher_agent, blog_writer
from tasks import research_task, write_task


#Forming the tech-focused crew with some enhanced configurations
crew = Crew(
    agents = [blog_researcher_agent, blog_writer],
    tasks = [research_task, write_task],
    process=Process.sequential, #Optional: sequential task execution is default
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

## start the task execution process with enhanced feedback
result = crew.kickoff(inputs={"topic":"Explain philosophy"})
print(result)

