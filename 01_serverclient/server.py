import zmq

context = zmq.Context()

sock = context.socket(zmq.REP)
sock.bind("tcp://127.0.0.1:9900")

while True:
    message = sock.recv()
    sock.send("Echo: " + message)
    print "Echo: " + message
