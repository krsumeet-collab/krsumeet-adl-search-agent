"""The application package."""
import os
import google.auth
from dotenv import load_dotenv
from .agent import root_agent

__all__ = ["root_agent"]

load_dotenv()

_, project_id = google.auth.default()
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
os.environ["GOOGLE_CLOUD_LOCATION"] = "us-central1"
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")