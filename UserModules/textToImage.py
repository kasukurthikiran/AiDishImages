import ClientResponse



client = ClientResponse.client_response()

def generate_image(prompt: str, data_list: list[str]) -> list[dict]:
    
    results = []

    for dish in data_list:
        response = client.images.generate(
            model="dall-e-3",
            prompt=f"{prompt} - {dish}",
            size="1024x1024",
            quality = "standard",
            n=1,
            response_format="b64_json"
        )

        base64_image = response.data[0].b64_json
        results.append({
            "dish": dish,
            "image_base64": base64_image
        })
    return results
