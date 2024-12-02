from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeElementFromWebsiteTool

search_tool = SerperDevTool()
scrape_tool = ScrapeElementFromWebsiteTool()

# Uncomment the following line to use an example of a custom tool
# from crew.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class CrewCrew():
	"""Crew crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def Analista(self) -> Agent:
		return Agent(
			config=self.agents_config['Analista'],
			tools = [search_tool, scrape_tool],
			verbose=True
		)

	@agent
	def Criador_memes(self) -> Agent:
		return Agent(
			config=self.agents_config['Criador_memes'],
			verbose=True
		)
	
	@agent
	def Editor(self) -> Agent:
		return Agent(
			config=self.agents_config['Editor'],
			verbose=True
		)

	@task
	def Analista(self) -> Task:
		return Task(
			config=self.tasks_config['Analista'],
			agent=self.Analista()
		)

	@task
	def Criador_memes(self) -> Task:
		return Task(
			config=self.tasks_config['Criador_memes'],
			agent=self.Criador_memes(),
		)
	
	@task
	def Editor(self) -> Task:
		return Task(
			config=self.tasks_config['Editor'],
			agent=self.Editor(),
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Crew crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=3,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)