# Local LLM Deployment
This mini project deploys a GGUF-format open-source LLM locally using llama.cpp and exposes it via a FastAPI API.

### Setup
After cloning the repository, create a "models" folder and put your model of choice in there. For this project the model used is Qwen1.5-7B Chat GGUF downloaded from Hugging Face. You can run the API using the command: 
```
uvicorn app:app --reload
```
Then you can use the API to send a prompt. For example, 
``` 
curl -X POST http://127.0.0.1:8000/ask \
     -H "Content-Type: application/json" \
     -d '{"prompt": "What is quantum finance?"}'
```

For performance metrics, a "performance_log.csv" file will be created with each prompt recorded and the latency. For example, it may register the sample prompt provided above as 
```
"What is quantum finance?", 0.724"
```
