import socket
from multiprocessing import shared_memory

def udp_conn(ip:str,port:int) -> None:
    dat = shared_memory.SharedMemory(name='udpData',create=True,size = 8192)
    dat_buf = dat.buf
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    addr = (ip,port)
    udp_socket.bind(addr)
    udp_socket.settimeout(3)
    while True:
        try:
            recv_data, client_addr = udp_socket.recvfrom(1024)
            length = len(recv_data)
            dat_buf[0:length] = recv_data
        except Exception:
            length = len(b'_,failed,_,_,0\n')
            dat_buf[0:length+1] = b'_,failed,0,,"0"\n'
            pass
        except KeyboardInterrupt:
            break
        except:
            pass
        #udp_socket.close()
    #print ("{:s} <- {:s}".format(recv_data.decode('utf-8'), str(client_addr)))