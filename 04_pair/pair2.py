import zmq
import time

context = zmq.Context()
sock = context.socket(zmq.PAIR)
sock.connect("tcp://127.0.0.1:9903")

while True:

    # receive
    msg = sock.recv()
    print msg

    # send
    sock.send("Pair 2 to Pair 1")

    # pause
    time.sleep(1)
