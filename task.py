from crewai import Task
from agent import buscador, redator, editor

buscar = Task(
    description = (
        "1. priorize as últimas tendencias, os principais atores e as notícias mais relevantes sobre o {tema}.\n"
        "2. Identifique o público-alvo, consideirando seus interesses e pontos de dor.\n"
        "3. Inclua palavras-chave de SEO e dados ou fontes relevantes."
    ),
    agent = buscador,
    expected_output = 'Um plano de tendências sobre o {tema}, com as palavras mais relevantes de SEO e as últimas notícias.'
)

redigir = Task(
    description = (
        "1. Use os dados coletados de conteúdos para criar um post de Instagram atraente sobre o {tema}.\n"
        "2. incorpore palavras-chave de SEO de forma natural.\n"
        "3. Certifique-se de que o post esteja estruturado de forma cativante com uma conclusão que faça o leitor refletir."
    ),
    agent = redator,
    expected_output = 'Um texto de Instagram sobre o {tema}.'
)

editar = Task(
    description = ("Revisar a postagem do Instagram em questão quanto a erros gramaticais e alinhamento com a voz do Fabrício Carraro."),
    agent = editor,
    expected_output = 'Um texto de Instagram pronto para a publicação, seguindo o tom de voz esperado. O texto deve estar separado em paragrafos e não usa bullet point.'
)