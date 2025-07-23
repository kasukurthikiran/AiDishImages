import requests
from .table_headers import table_headers
from .get_db_table import get_db_table


def create_table():
    url, headers = table_headers()
    index_name, table_name = get_db_table()

    data = {
        "name": table_name,
        "schema": {
            "fields": {
                "image_path": {"filterable": True},
                "title": {"filterable": True},
            }
        },
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("success")
        return response.status_code
    else:
        return response.status_code
