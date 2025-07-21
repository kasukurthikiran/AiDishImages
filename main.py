from my_packages.filter_records import filter_records
from my_packages.image_generation import image_generation
from my_packages.insert_records import insert_records
from my_packages.dish_name_extraction import dish_name_extraction


def main():
    final_result = []
    dishes = dish_name_extraction()
    if dishes:
        matched_records, unmatched_records = filter_records(dishes)

        if matched_records:
            final_result.append(matched_records)

        if unmatched_records:
            metadatas = image_generation(unmatched_records)
            final_result.append(metadatas)
            insert_records(unmatched_records)
        print(final_result)


if __name__ == "__main__":
    main()
