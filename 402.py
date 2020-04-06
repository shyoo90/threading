from flask import Flask, request
import threading
import queue
from concurrent.futures import ThreadPoolExecutor
import atexit
import sys
import time


app = Flask(__name__)

que = queue.Queue(maxsize=2)
lock1 = threading.Lock()
lock2 = threading.Lock()
condition1 = threading.Condition(lock1)
condition2 = threading.Condition(lock2)
iter = 0

@app.route("/c", methods=["GET","POST"])
def c():
    global que
    if request.method == 'POST':
        data = request.get_json()
        data = list(data.values())[0]
        if que.full():
            with condition1:
                condition1.wait()
            with condition2:
                que.put(data)
                condition2.notify()
        else:
            with condition2:
                que.put(data)
                condition2.notify()
    return ''

def d():
    global que
    global iter
    while True:
        if que.full():
            with condition1:
                a = que.get()
                iter +=1
                print(a, iter, file=sys.stderr)
                condition1.notify()
        else:
            with condition2:
                condition2.wait()
                a = que.get()
                iter +=1
                print(a, iter,  file=sys.stderr)
            with condition1:
                condition1.notify()


thread = threading.Thread(target = d, daemon=True)
thread.start()

if __name__ == "__main__":

    app.run('0.0.0.0',8080, threaded = True)
