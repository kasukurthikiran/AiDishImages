from my_packages.filter_records import filter_records
from my_packages.image_generation import image_generation
from my_packages.dish_name_extraction import dish_name_extraction
from my_superbase_packages.fetch_images import fetch_images


def main():
    old_image_paths = []

    dishes = dish_name_extraction()
    if dishes:
        matched_records, unmatched_records = filter_records(dishes)

    if matched_records:
        old_image_paths = [
            {"image_path": image.get("image_path")}
            for image in matched_records
            if image.get("image_path")
        ]

    if unmatched_records:
        temp_paths = image_generation(unmatched_records)

    if unmatched_records and matched_records:
        result = old_image_paths + temp_paths
        t = fetch_images(result)
        print(t)
    elif unmatched_records:
        t = fetch_images(temp_paths)
    elif matched_records:
        t = fetch_images(old_image_paths)
        print(t)


main()
