from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.settings import Settings
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import StorageContext, load_index_from_storage
from dotenv import load_dotenv

import os

load_dotenv()

Settings.llm  = Gemini(
    model="models/gemini-1.5-flash",
    # api_key="some key",  # uses GOOGLE_API_KEY env var by default
)

#  Make sure to run pip install llama-index-embeddings-gemini

Settings.embed_model = GeminiEmbedding(model="models/text-embedding-004")

# Create embeddings from scratch
# documents = SimpleDirectoryReader("data").load_data()
# index = VectorStoreIndex.from_documents(documents, show_progress=True)
# index.storage_context.persist()


# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="prof_embeddings")

# load index
index = load_index_from_storage(storage_context)


query_engine = index.as_query_engine()
response = query_engine.query("List all ECE classes.")
print(response)
