from database.supabase import supabase


# -------------------------
# Documents
# -------------------------


def save_document(
    user_id: str,
    file_name: str,
    file_url: str
):

    result = (
        supabase
        .table("documents")
        .insert(
            {
                "user_id": user_id,
                "file_name": file_name,
                "file_url": file_url
            }
        )
        .execute()
    )

    return result.data



def get_documents(
    user_id: str
):

    result = (
        supabase
        .table("documents")
        .select("*")
        .eq(
            "user_id",
            user_id
        )
        .execute()
    )

    return result.data



# -------------------------
# Chat Memory
# -------------------------


def save_message(
    user_id: str,
    role: str,
    content: str
):

    result = (
        supabase
        .table("messages")
        .insert(
            {
                "user_id": user_id,
                "role": role,
                "content": content
            }
        )
        .execute()
    )

    return result.data




def get_chat_history(
    user_id: str,
    limit: int = 10
):

    result = (
        supabase
        .table("messages")
        .select("*")
        .eq(
            "user_id",
            user_id
        )
        .order(
            "created_at",
            desc=True
        )
        .limit(limit)
        .execute()
    )

    return result.data