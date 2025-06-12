from llama_cpp import Llama
from functools import lru_cache
import time

llm = Llama(model_path="models/qwen1_5-7b-chat-q5_k_m.gguf", n_ctx=2048)

@lru_cache(maxsize=100)
def ask_llm(prompt: str) -> str:
    start = time.time()
    response = llm(prompt=prompt, max_tokens=256)
    duration = time.time() - start

    with open("performance_log.csv", "a") as f:
        f.write(f'"{prompt}",{duration:.3f}\n')

    return response["choices"][0]["text"].strip()
