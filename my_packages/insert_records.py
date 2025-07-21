import uuid

from get_db_table import get_db_table
from pinecone_client import pinecone_client
from generate_embeddings import generate_embedding


def insert_records(items):
    db, table = get_db_table()
    pc = pinecone_client()
    index = pc.Index(db)
    # items= [
    #     {"title": "Chicken Curry", "image_path": "images/chicken.jpg"},
    #     {"title": "Paneer Butter Masala", "image_path": "images/paneer.jpg"},
    #     {"title": "Mutton Biryani", "image_path": "images/biryani.jpg"},
    # ]

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


# from openai import OpenAI

# PINECONE_API_KEY = (
#     "pcsk_2SuSrJ_6swvEaWCyJ6noMSnS4nJX7JSaNYfzsRTrSLK3wT79TP6Rv9FfnWqucyCJf5mJDX"
# )
# INDEX_NAME = "d-index"
# NAMESPACE_NAME = "india-dishes"

# pc = Pinecone(api_key=PINECONE_API_KEY)
# index = pc.Index(INDEX_NAME)
# # Replace with your actual index name

# # Dish list to query
# dishes = [
#     {"title": "Chicken Curry", "image_path": "images/chicken.jpg"},
#     {"title": "Paneer Butter Masala", "image_path": "images/paneer.jpg"},
#     {"title": "hi", "image_path": "images/biryani.jpg"},
# ]

# threshold = 0.7
# okay_dishes = []
# not_okay_dishes = []
# openai_api_key = "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"  # Replace with your key

# client = OpenAI(api_key=openai_api_key)
# # Loop over each dish

# for dish in dishes:
#     # Generate embedding using OpenAI
#     embedding_response = client.embeddings.create(
#         input=dish["title"], model="text-embedding-3-small"
#     )
#     vector = embedding_response.data[0].embedding

#     # Query Pinecone
#     response = index.query(
#         vector=vector,
#         namespace="india-dishes",  # Use your namespace
#         top_k=1,  # We only care about the best match
#         include_metadata=True,
#         include_values=False,
#     )

#     match = response.matches[0]
#     score = match.score
#     print(f"{dish['title']} → Score: {score:.4f}")

#     # Compare score to threshold
#     if score >= threshold:
#         okay_dishes.append({**dish, "score": score})
#     else:
#         not_okay_dishes.append({**dish, "score": score})

# # Results
# print("\n✅ OKAY DISHES:")
# for d in okay_dishes:
#     print(f"{d['title']} → Score: {d['score']:.4f}")

# print("\n❌ NOT OKAY DISHES:")
# for d in not_okay_dishes:
#     print(f"{d['title']} → Score: {d['score']:.4f}")


# print(okay_dishes)
# print(not_okay_dishes)
