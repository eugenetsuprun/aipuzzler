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

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task

    @task
    def write_unit_tests(self) -> Task:
        return Task(
            config=self.tasks_config["write_unit_tests"],
        )

    @task
    def solve_puzzle(self) -> Task:
        return Task(
            config=self.tasks_config["solve_puzzle"],
        )

    @task
    def check_solution(self) -> Task:
        return Task(
            config=self.tasks_config["check_solution"],
            tools=[CodeInterpreterTool()],
        )

    @task
    def write_report(self) -> Task:
        return Task(
            config=self.tasks_config["write_report"],
        )

    @crew
    def crew(self) -> Crew:
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        manager = Agent(
            config=self.agents_config["manager"],
            verbose=True,
        )

        return Crew(
            agents=self.agents,
            tasks=[
                Task(config=self.tasks_config[task_name])
                for task_name in self.tasks_config
            ],
            process=Process.hierarchical,
            verbose=True,
            memory=True,
            output_log_file="output.log",
            manager_agent=manager,
        )
