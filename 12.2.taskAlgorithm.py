class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def front(self):
        return self.queue[0] if self.queue else None

    def is_empty(self):
        return not bool(self.queue)

    def size(self):
        return len(self.queue)


def merge_queues(a, b):
    c = Queue()
    while not a.is_empty() or not b.is_empty():
        if a.is_empty():
            while not b.is_empty():
                c.push(b.front())
                b.pop()
            return c
        if b.is_empty():
            while not a.is_empty():
                c.push(a.front())
                a.pop()
            return c
        if a.front() <= b.front():
            c.push(a.front())
            a.pop()
        else:
            c.push(b.front())
            b.pop()
    return c


def queue_of_queues():
    xs = Queue()
    numbers = list(map(int, input("Please enter some numbers with spaces: \n").split()))
    for n in numbers:
        x = Queue()
        x.push(n)
        xs.push(x)

    while xs.size() > 1:
        a = xs.front()
        xs.pop()
        if a.is_empty():
            continue
        b = xs.front()
        xs.pop()
        if b.is_empty():
            continue
        c = merge_queues(a, b)
        xs.push(c)

    while not xs.front().is_empty():
        print(xs.front().front(), end=' ')
        xs.front().pop()


queue_of_queues()
