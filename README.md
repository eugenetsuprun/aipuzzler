
# Can AI generate a coding puzzle so hard that it's impossible for AI to solve? But still easy for human software engineers?

🚧 This is a work in progress! The final report from this crew is incoherent. It generates a puzzle, solves it, and thinks that it succeeded in generating an AI-proof puzzle. Next up, I'm gonna modify the workflow such that:

* There is more rigor in generating an AI-proof puzzle and corresponding unit tests. The crew might try out different strategies here and have more of an editing process.
* The solver gets N attempts to solve the puzzle.
* The scribe is more clear eyed about the success of this process.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/puzzle_solver/config/agents.yaml` to define agents
- Modify `src/puzzle_solver/config/tasks.yaml` to define tasks
- Modify `src/puzzle_solver/crew.py` to add your own logic, tools and specific args
- Modify `src/puzzle_solver/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart the crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the puzzle-solver Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The puzzle-solver Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.
