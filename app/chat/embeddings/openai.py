from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

import os
load_dotenv()
embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))
