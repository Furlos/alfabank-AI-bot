import requests

def make_request(message:str):
    url = "http://model-runner.docker.internal/engines/v1/chat/completions"
    payload = {"model": "ai/smollm2:360M-Q4_K_M",
               "messages": [{"role": "user", "content": f"{message}"}]}
    response = requests.post(url, json=payload)
    return response.json()["choices"][0]["message"]["content"]
