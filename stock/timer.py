import threading
import time


def hello(name):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), end='   ')
    print("hello %s" % name)

    global timer
    timer = threading.Timer(10, hello, ["Hawk"])
    timer.start()

if __name__ == "__main__":
    timer = threading.Timer(10, hello, ["Hawk"])
    timer.start()