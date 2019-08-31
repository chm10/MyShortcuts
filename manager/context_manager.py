#!/us/bin/env python3
import time 

class timer (object):

    def __enter__(self):
        self.start = time.time()
        print('Timer starts at: %s' % self.start)
        return self

    def __exit__(self, type, value, traceback):
        self.stop = time.time()
        print('Timer stops at: %s' % self.stop)
        print('Elapsed: %s' % (self.stop - self.start))
        return self
