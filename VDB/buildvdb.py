from langchain.vectorstores import PGVector
import os
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()


CONNECTION_STRING = PGVector.connection_string_from_db_params(
     driver=os.environ.get("PGVECTOR_DRIVER", "psycopg2"),
     host=os.environ.get("PGVECTOR_HOST", "localhost"),
     port=int(os.environ.get("PGVECTOR_PORT", "5432")),
     database=os.environ.get("PGVECTOR_DATABASE", "postgres"),
     user=os.environ.get("PGVECTOR_USER", "postgres"),
     password=os.environ.get("PGVECTOR_PASSWORD", "trans"),
 )

MODEL_NAME = os.environ.get("MODEL_NAME", "intfloat/multilingual-e5-base")
MODEL_KWARGS = {'device': 'cpu'}
ENCODE_KWARGZ = {'normalize_embeddings': True}

HF = HuggingFaceEmbeddings(
    model_name=MODEL_NAME,
    model_kwargs=MODEL_KWARGS,
    encode_kwargs=ENCODE_KWARGZ,
    cache_folder = "../models"
)

COLLECTION_NAME = "TRANSLATION"

DB = PGVector.from_documents(
    embedding=HF,
    documents=[],
    collection_name=COLLECTION_NAME,
    connection_string=CONNECTION_STRING,
)