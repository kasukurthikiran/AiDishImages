import uuid

from .get_db_table import get_db_table
from .pinecone_client import pinecone_client
from .generate_embeddings import generate_embedding


def insert_records(items):
    db, table = get_db_table()
    pc = pinecone_client()
    index = pc.Index(db)

    vectors = []

    for item in items:
        vector = generate_embedding(item["title"])
        record = {
            "id": str(uuid.uuid4()),
            "values": vector,
            "metadata": {"title": item["title"], "image_path": item["image_path"]},
        }
        vectors.append(record)

    index.upsert(vectors=vectors, namespace=table)
    print("Upserted successfully!")
