from .get_db_table import get_db_table
from .pinecone_client import pinecone_client
from .generate_embeddings import generate_embedding


def insert_records(items):
    db, table = get_db_table()
    pc = pinecone_client()
    index = pc.Index(db)
    vectors = []
    for item in items:
        print(item["dish"])
        vector = generate_embedding(item["dish"])
        record = {
            "id": item["id"],
            "values": vector,
            "metadata": {"title": item["dish"], "image_path": f"{item['id']}.png"},
        }
        vectors.append(record)

    t = index.upsert(vectors=vectors, namespace=table)
    print("Upserted successfully!")
    return t
