import zmq
import sys

context = zmq.Context()

sock = context.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:9900")

sock.send(" ".join(sys.argv[1:]))
print sock.recv()
