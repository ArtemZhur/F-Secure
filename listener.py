
class Listener():
    def __init__(self, queue, log):
        self.queue = queue
        self.log = log

    def listener(self):
        '''listens for messages on the q, writes to file. '''
        file = open(self.log, 'w+')
        while True:
            m = self.queue.get()
            print(m)
            file.write(str(m) + '\n')
            file.flush()
        file.close()