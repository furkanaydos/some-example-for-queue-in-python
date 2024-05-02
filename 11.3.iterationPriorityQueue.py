class Customer:
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"Customer(priority={self.priority}, name='{self.name}')"

class PriorityQueue:
    def __init__(self):
        self._queue = []

    def push(self, priority, name):
        customer = Customer(priority, name)
        self._queue.append(customer)
        self._queue.sort(reverse=True)

    def pop(self):
        if not self._queue:
            return None
        return self._queue.pop(0)

    def peek(self):
        if not self._queue:
            return None
        return self._queue[0]

def test_priority_queue():
    q = PriorityQueue()

    q.push(1, "Norman Nobody")
    q.push(60, "Marilyn Monroe")
    q.push(100, "Marie Curie")
    q.push(80, "Freddie Mercury")
    q.push(90, "Martin Luther King")
    q.push(1, "Samuel Someguy")
    q.push(90, "Mohandas Gandhi")
    q.push(100, "Albert Einstein")
    q.push(80, "John Lennon")

    while True:
        customer = q.pop()
        if customer is None:
            break
        print(customer)

test_priority_queue()