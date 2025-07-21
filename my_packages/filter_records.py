from pinecone import Pinecone
import os
from generate_embeddings import get_embedding
from get_db_table import get_db_table
from dotenv import load_dotenv

threshold = os.getenv("threshold")


def filter_records(items):
    load_dotenv()
    matched_records = []
    unmatched_records = []
    db, table_name = get_db_table()
    index = Pinecone(db)
    for item in items:
        vector = get_embedding(item)
        response = index.query(
            vector=vector,
            namespace=table_name,
            top_k=1,
            include_metadata=True,
            include_values=False,
        )

        matches = response.get("matches", [])
        if matches:
            match = matches[0]
            score = match.get("score", 0)

            if score >= threshold:
                metadata = match.get("metadata", {})
                matched_records.append(
                    {
                        "dish": item,
                        "image_path": metadata["image_path"],
                        "score": score,
                    }
                )
                # print(dish)
            else:
                unmatched_records.append(item)
        else:
            unmatched_records.append(item)
    # print("matched_dish_items", matched_dish_items)
    # print("not_matched_dish_items", not_matched_dish_items)
    return matched_records, unmatched_records


# print(
#     querypineindex(
#         [
#             "Prawn Cutlet",
#             "Shami Kebab Bhurji",
#             "Kathkoyla Murgh",
#             "Kochupata Chingri Bhapa",
#             "Spicy Shredded Fish",
#             "hasan",
#             "saikiarn",
#         ]
#     )
# )

# t = querypineindex(
#     [
#         {"title": "Chicken Curry", "image_path": "images/chicken.jpg"},
#         {"title": "Paneer Butter Masala", "image_path": "images/paneer.jpg"},
#         {"title": "hi", "image_path": "images/biryani.jpg"},
#     ]
# )
# print(t)
