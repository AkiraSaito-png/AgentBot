import os

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
SERPER_API_KEY = os.environ.get('SERPER_API_KEY')
os.environ['OPENAI_MODEL_NAME'] = 'gpt-4o'