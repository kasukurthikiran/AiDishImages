import threading
import time
import requests

# Addition
def addition():
    print("[Addition] Task started")
    result = 10 + 5
    time.sleep(1)
    print("[Addition] Result:", result)

# Subtraction
def subtraction():
    print("[Subtraction] Task started")
    result = 10 - 5
    time.sleep(1)
    print("[Subtraction] Result:", result)

# Multiplication
def multiplication():
    print("[Multiplication] Task started")
    result = 10 * 5
    time.sleep(1)
    print("[Multiplication] Result:", result)

# Fetching data from real API
def get_product_data():
    print("[API] Fetching product data from fakestoreapi.com ...")
    try:
        response = requests.get("https://fakestoreapi.com/products/1")
        if response.status_code == 200:
            product = response.json()
            print("[API] Product Data:")
            print(" - Title:", product['title'])
            print(" - Price:", product['price'])
            print(" - Category:", product['category'])
        else:
            print("[API] Failed to fetch data. Status code:", response.status_code)
    except Exception as e:
        print("[API] Error:", e)

# Create threads
t1 = threading.Thread(target=addition)
t2 = threading.Thread(target=subtraction)
t3 = threading.Thread(target=multiplication)
t4 = threading.Thread(target=get_product_data)

# Start all threads
t1.start()
t2.start()
t3.start()
t4.start()

# Wait for all threads to finish
t1.join()
t2.join()
t3.join()
t4.join()

print("✅ All tasks completed.")
