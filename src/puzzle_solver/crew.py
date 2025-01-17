from json import tool
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import CodeInterpreterTool
from crewai.flow.flow import Flow, listen, router, start

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class AIProofPuzzler:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    usage_metrics = {"total_tokens": 0}

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

    @agent
    def question_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["question_writer"],
            verbose=True,
        )

    @agent
    def qa_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config["qa_engineer"],
            verbose=True,
            tools=[CodeInterpreterTool()],
        )

    @agent
    def solver(self) -> Agent:
        return Agent(
            config=self.agents_config["solver"],
            verbose=True,
            tools=[CodeInterpreterTool()],
        )

    @agent
    def scribe(self) -> Agent:
        return Agent(
            config=self.agents_config["scribe"],
            verbose=True,
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=[
                Task(config=self.tasks_config[task_name])
                for task_name in self.tasks_config
            ],
            process=Process.sequential,
            verbose=True,
            memory=True,
            output_log_file="output.log",
        )
