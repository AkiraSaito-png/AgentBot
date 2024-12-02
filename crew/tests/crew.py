from crewai import  Crew
from agent import buscador, redator, editor
from task import buscar, redigir, editar

equipe = Crew(
    agents = [buscador, redator, editor],
    tasks = [buscar, redigir, editar],
    verbose = True
)