from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import deta, time

app = FastAPI()

log = deta.Base("log")

bangs = {
    "g": "google.com/search?q=",
    "m": "www2.movieorca.com/search/",
}


@app.get("/search")
def index(q: str):
    log.put({"search_term": q, "date": time.strftime("%H:%M:%S%z,%d-%b-%Y")})
    site = None
    flag = False
    prefix = "!!"

    if q.startswith(prefix):
        q = q[2:]
        flag = True
        for bang in bangs.keys():
            if q.startswith(bang):
                flag = False
                site = bangs[bang]
                q = q[len(bang)+1:]
                if bang == "m":
                    q=q.replace(" ", "-")
    
    if not site:
        site = "start.duckduckgo.com?q="
    if flag:
        q = prefix + q
        
    
    return RedirectResponse(f"https://{site}{q}")
