"use client";


import { supabase } from "@/lib/supabase";


export default function LoginPage(){


async function googleLogin(){


await supabase.auth.signInWithOAuth({

    provider:"google",

    options:{

        redirectTo:
        "http://localhost:3000"

    }

});


}



return (

<div>


<h1>
AI Study Assistant
</h1>


<button onClick={googleLogin}>

Login with Google

</button>


</div>

);

}