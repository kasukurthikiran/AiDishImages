from my_packages.filter_records import filter_records
from my_packages.image_generation import image_generation

final_result = []


matched_records, unmatched_records = filter_records

if matched_records:
    final_result.append(matched_records)

if unmatched_records:
    metadatas = image_generation(unmatched_records)
    final_result.append(metadatas)


# print()
