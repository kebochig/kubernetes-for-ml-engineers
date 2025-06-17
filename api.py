from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get('/health')
async def health():
    return {
        'status': 'healthy and running',
        'timestamp': datetime.now().isoformat()
    }