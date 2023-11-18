from datasets import load_dataset, DatasetDict
import pandas as pd
from langchain.schema.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import PGVector
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()
import os

def load_and_process_data(languages):
    """
    Loads and processes datasets for specified language pairs.
    Removes unnecessary columns and adds a 'lang' column for each dataset.
    Merges all datasets into a single pandas DataFrame.
    """
    data = DatasetDict()
    for l1, l2 in languages:
        dataset = load_dataset("opus_books", f"{l1}-{l2}")["train"].remove_columns(["id"])
        dataset = dataset.map(lambda example: {**example, 'lang': f"{l1}-{l2}"})
        data[f"{l1}-{l2}"] = dataset
    return pd.concat([v.to_pandas() for _, v in data.items()], ignore_index=True)

def create_documents(df):
    """
    Converts each row in the DataFrame to a Document object.
    Adds a 'documents' column to the DataFrame with these objects.
    """
    df['translation'] = df['translation'].astype(str)
    df['documents'] = df.apply(lambda x: Document(page_content=x[0], metadata={'lang': x[1]}), axis=1)
    return df

def split_documents(documents):
    """
    Splits documents into smaller chunks using a RecursiveCharacterTextSplitter.
    This helps in processing large text documents.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=20, length_function=len)
    return text_splitter.split_documents(documents)

def setup_embeddings_and_db():
    """
    Sets up the embeddings using HuggingFaceEmbeddings and initializes the PGVector database.
    Returns a PGVector object for further operations.
    """
    model_name = "intfloat/multilingual-e5-base"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': True}

    hf_embeddings = HuggingFaceEmbeddings(model_name, model_kwargs, encode_kwargs, cache_folder="../models")

    return PGVector(connection_string=PGVector.connection_string_from_db_params(
        driver=os.environ.get("PGVECTOR_DRIVER", "psycopg2"),
        host=os.environ.get("PGVECTOR_HOST", "localhost"),
        port=int(os.environ.get("PGVECTOR_PORT", "5432")),
        database=os.environ.get("PGVECTOR_DATABASE", "postgres"),
        user=os.environ.get("PGVECTOR_USER", "postgres"),
        password=os.environ.get("PGVECTOR_PASSWORD", "trans"),
    ),
    embedding_function=hf_embeddings,
    collection_name="TRANSLATION",
    )

# Main execution
languages = [('en', 'fr'), ('en', 'ru'), ('fr', 'ru'), ('en', 'es')]
df = load_and_process_data(languages)
df = create_documents(df)
documents = split_documents(df['documents'].tolist())
db = setup_embeddings_and_db()
db.add_documents(documents)