from crewai import Task
from tools import yt_tool
from agents import blog_researcher_agent, blog_writer

## Research task

research_task = Task(
    description=(
        "Identity the video {topic}."
        "Get detailed information about the video from the channel."
    ),
    expected_output='A comprehensive 3 paragraphs long report based on the {topic} of video content',
    tools = [yt_tool],
    agent = blog_researcher_agent
)

write_task = Task(
    description=(""),
    expected_output='Summarize the info from the youtube channel video on the topic{topic} and create the content for the blog',
    tools = [yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog-post.md'
)