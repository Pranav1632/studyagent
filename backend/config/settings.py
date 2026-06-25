import os
from dotenv import load_dotenv


# Load .env file
load_dotenv()


class Settings:
    """
    Global application settings.

    All environment variables are loaded here.
    Import settings anywhere in backend.
    """


    # -------------------------
    # Gemini API
    # -------------------------

    GOOGLE_API_KEY: str = os.getenv(
        "GOOGLE_API_KEY"
    )


    # -------------------------
    # Supabase
    # -------------------------

    SUPABASE_URL: str = os.getenv(
        "SUPABASE_URL"
    )

    SUPABASE_KEY: str = os.getenv(
        "SUPABASE_KEY"
    )


    # -------------------------
    # ChromaDB
    # -------------------------

    CHROMA_PATH: str = os.getenv(
        "CHROMA_PATH",
        "./chroma_db"
    )


    # -------------------------
    # Upload Storage
    # -------------------------

    TEMP_STORAGE: str = os.getenv(
        "TEMP_STORAGE",
        "./storage/temp"
    )


    # -------------------------
    # AI Model Config
    # -------------------------

    GEMINI_MODEL: str = (
        "gemini-2.5-flash"
    )


    EMBEDDING_MODEL: str = (
    "models/gemini-embedding-001"
)


settings = Settings()