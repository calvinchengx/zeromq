import zmq

context = zmq.Context()

sock = context.socket(zmq.SUB)

sock.setsockopt(zmq.SUBSCRIBE, "1")
sock.connect("tcp://127.0.0.1:9901")

while True:
    message = sock.recv()
    print message
