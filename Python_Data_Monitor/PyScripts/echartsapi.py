from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import time
from fastapi.middleware.cors import CORSMiddleware
from udpconnection import udp_conn
from multiprocessing import Process, shared_memory
import re
  

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/hr_json")
def hr_js():
    dat = shared_memory.SharedMemory(name="udpData")
    dat_buf = dat.buf
    k_l = ['tick','time','hr','?','_','IBI']
    timenow = time.time()
    data = dat_buf.tobytes()
    data = data.decode('utf-8')
    data = re.sub(u'\u0000','',data)
    data = data.strip('\n')
    dlist = data.split(",")
    ddict = {}
    ddict[k_l[0]]=timenow
    i=0
    leng=len(dlist)
    if leng>5:
        leng=5 # Prevent OutIndex.
    try:
        while i<leng:
            ddict[k_l[i+1]]=dlist[i]
            i+=1
    except Exception:
        i = 0
    return ddict

app.mount("/js", StaticFiles(directory="www\\js"), name="js")
app.mount("/", StaticFiles(directory="www\\html",html=True), name="html")

class Server(uvicorn.Server):
    def install_signal_handlers(self):
        pass

config = uvicorn.Config("echartsapi:app", host="127.0.0.1", port=8919, log_level="info")
server = Server(config=config)

if __name__ == "__main__":
    processa = Process(target=udp_conn,args=("127.0.0.1",8909))
    processb = Process(target = Server.run,args=(server,))
    processa.start()
    processb.start()
    processa.join()
    processb.join()
        
