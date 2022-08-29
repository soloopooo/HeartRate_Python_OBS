from multiprocessing import Process, Pipe
def fun1(conn):
    print('子进程发送消息：')
    conn.send('你好主进程')
    print('子进程接受消息：')
    print(conn.recv())
    conn.close()

if __name__ == '__main__':
    conn1, conn2 = Pipe() #关键点，pipe实例化生成一个双向管
    p = Process(target=fun1, args=(conn2,)) #conn2传给子进程
    p.start()
    print('主进程接受消息：')
    print(conn1.recv())
    print('主进程发送消息：')
    conn1.send("你好子进程")
    p.join()
    print('结束测试')