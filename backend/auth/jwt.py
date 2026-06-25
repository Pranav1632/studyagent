from fastapi import (
    Depends,
    HTTPException
)

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)


from database.supabase import supabase



security = HTTPBearer()



def get_current_user(

    credentials: HTTPAuthorizationCredentials = Depends(security)

):


    token = credentials.credentials


    try:


        user = (
            supabase
            .auth
            .get_user(
                token
            )
        )


        return {

            "id":
            user.user.id,


            "email":
            user.user.email

        }



    except Exception:


        raise HTTPException(

            status_code=401,

            detail="Invalid authentication token"

        )