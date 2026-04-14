import os
from dotenv import load_dotenv
from pathlib import Path

def load_frontend_config():
  # frontend folder ke andr .env dhoondega
    env_path =Path(__file__).parent / ".env"
    load_dotenv(dotenv_path=env_path)
    return {
        "FASTAPI_BASE_URL": os.getenv("FASTAPI_BASE_URL", "http://localhost:8000")
    }

# Load config once when the module is imported
FRONTEND_CONFIG = load_frontend_config()