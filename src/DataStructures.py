class Queue:

    def __init__(self, mode, current_queue=[]):
        self._queue = current_queue
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        if mode is None:
            raise "Please specify a queue mode FIFO or LIFO"
        else:
            self._mode = mode
    
    def enqueue(self, item):
        if self._mode == 'FIFO':
            return self._queue.append(item)
        else:
            return self._queue.insert(0, item)

    def dequeue(self):
        if self._mode == 'FIFO':
            return self._queue.pop(0)
        else:
            return self._queue.pop()
        
    def get_queue(self):
        return self._queue

    def size(self):
        return len(self._queue)