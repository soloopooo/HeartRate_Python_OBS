
import contextlib
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import time
from fastapi.middleware.cors import CORSMiddleware
import socket
from multiprocessing import Process, shared_memory
import re
  

def udp_conn(ip:str,port:int) -> None:
    dat = shared_memory.SharedMemory(name='udpData',create=True,size = 64)
    dat_buf = dat.buf
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    addr = (ip,port)
    udp_socket.bind(addr)
    udp_socket.settimeout(3)
    while True:
        recv_data, client_addr = udp_socket.recvfrom(1024)
        length = len(recv_data)
        dat_buf[0:length] = recv_data
        #udp_socket.close()
    #print ("{:s} <- {:s}".format(recv_data.decode('utf-8'), str(client_addr)))

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
    while i<leng:
        ddict[k_l[i+1]]=dlist[i]
        i+=1
    return ddict

@app.get("/",response_class=HTMLResponse)
def main():
    html_main = open('www\\index.html','r').read()
    return html_main
@app.get("/speedometer",response_class=HTMLResponse)
def speedo():
    html_speedo = open('www\\speedometer.html','r').read()
    return html_speedo
@app.get("/spline",response_class=HTMLResponse)
def spline():
    html_spline = open('www\\spline.html','r').read()
    return html_spline

app.mount("/js", StaticFiles(directory="www\\js"), name="js")  

class Server(uvicorn.Server):
    def install_signal_handlers(self):
        pass

    @contextlib.contextmanager
    def run_in_process(self):
        processb = Process(target=self.run)
        processb.start()
        try:
            while not self.started:
                time.sleep(1e-3)
            yield
        finally:
            dat = shared_memory.SharedMemory(name="udpData")
            dat.close()
            self.should_exit = True
            processb.join()

config = uvicorn.Config("echartsapi:app", host="127.0.0.1", port=8919, log_level="info")
server = Server(config=config)

if __name__ == "__main__":
    processa = Process(target=udp_conn,args=("127.0.0.1",8909))
    processb = Process(target = Server.run,args=(server,))
    processa.start()
    processb.start()
    processa.join()
    processb.join()
        
