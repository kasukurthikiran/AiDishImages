from pinecone import ServerlessSpec
from .pinecone_client import pinecone_client
from .get_db_table import get_db_table


def create_or_get_db():
    pinecone = pinecone_client()
    db_name, table_name = get_db_table()
    if db_name not in pinecone.list_indexes().names():
        pinecone.create_index(
            name=db_name,
            dimension=1536,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )
    index_name = pinecone.Index(
        name=db_name,
        pool_threads=50,
        connection_pool_maxsize=50,
    )
    return index_name
