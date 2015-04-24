import zmq
import time

context = zmq.Context()
sock = context.socket(zmq.PAIR)
sock.bind("tcp://127.0.0.1:9903")

while True:

    # send
    sock.send("Pair 1 to Pair 2")

    # receive
    msg = sock.recv()
    print msg

    # pause
    time.sleep(1)
