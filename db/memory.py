from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

def save_message(session_id, role, content):
    supabase.table("messages").insert({
        "session_id": session_id,
        "role": role,
        "content": content
    }).execute()

def get_history(session_id, limit=5):
    res = supabase.table("messages")\
        .select("role, content")\
        .eq("session_id", session_id)\
        .order("created_at", desc=True)\
        .limit(limit)\
        .execute()
    
    # Inverte para ficar em ordem cronológica corre
    return list(reversed(res.data)) if res.data else []
