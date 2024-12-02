from crewai import Agent
from tools import scrape_tool, search_tool

buscador = Agent(
    role = 'Buscador de conteúdos e notícias',
    goal = 'Busque conteúdo online sobre o tema {tema}',
    backstory = 'Você está trabalhando na criação de artigos para o Instagram sobre {tema}.'
                'Você vai fazer uma busca na internet e coletará as informações.'
                'Seu trabalho servirá de base para o Redator de Conteúdo.',
    tools = [search_tool, scrape_tool],
    verbose = True
)

redator = Agent(
    role = 'Redator de conteúdos e notícias',
    goal = 'escreva um texto divertido e factualmente correto para o Instagram sobre o tema {tema}',
    backstory = 'Você está trabalhando na redação de artigos para o Instagram sobre {tema}.'
                'Você vai utilizar os dados coletados pelo Buscador de conteúdos e notícias, para escrever um texto'
                'interessante, divertido e factuamente correto para o instagram.'
                'Dê opiniões sobre o {tema}, mas ao faze-lo, deixe claro que são opiniões pessoais.',
    tools = [search_tool, scrape_tool],
    verbose = True
)

editor = Agent(
    role = 'Editor de conteúdos e notícias',
    goal = 'escreva um texto para o Instagram para que ele tenha um tom de voz mais informal.',
    backstory = 'Você está trabalhando na edição de artigos para o Instagram sobre {tema}.'
                'Você vai receber um texto do Buscador de conteúdos e notícias, e edita-lo para o tem de voz'
                'do Fabrício Carraro, que é mais informal e divertido.',
    tools = [search_tool, scrape_tool],
    verbose = True
)