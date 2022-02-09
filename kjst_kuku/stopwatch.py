import time


class Stopwatch:

    def  __init__(self):
        self.t0 = time.time()

    def stop(self):
        self.elapsed = time.time() - self.t0
        return self.elapsed


if __name__ ==  "__main__":

    sw = Stopwatch()
    time.sleep(3)
    sw.stop()

    print(sw.elapsed)