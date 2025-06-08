from supabase import create_client
import os
from dotenv import load_dotenv
load_dotenv()

# Load from .env or hardcode
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_message(role, content):
    response = supabase.table("messages").insert({
        "role": role,
        "content": content
    }).execute()
    return response
