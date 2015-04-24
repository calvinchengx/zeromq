import zmq
import time

context = zmq.Context()

sock = context.socket(zmq.PUSH)
sock.bind("tcp://127.0.0.1:9902")

id = 0

while True:
    time.sleep(1)
    id, now = id + 1, time.ctime()

    message = "{id} - {time}".format(id=id, time=now)

    sock.send(message)

    print "Sent: {msg}".format(msg=message)
