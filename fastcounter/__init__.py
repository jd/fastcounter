import itertools
import threading


class Counter(object):
    """A counter that is only suitable for application without any concurrency."""

    __slots__ = (
        "value",
        "_step",
    )

    def __init__(self, init=0, step=1):
        self.value = init
        self._step = step

    def increment(self):
        self.value += self._step


class FastReadCounter(Counter):

    __slots__ = (
        "value",
        "_lock",
        "_step",
    )

    def __init__(self, init=0, step=1):
        super().__init__(init, step)
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            self.value += self._step


class FastWriteCounter(Counter):

    __slots__ = (
        "_number_of_read",
        "_counter",
        "_lock",
        "_step",
    )

    def __init__(self, init=0, step=1):
        self._number_of_read = 0
        self._step = step
        self._counter = itertools.count(init, step)
        self._lock = threading.Lock()
        # Init the counter value
        next(self._counter)

    def increment(self):
        next(self._counter)

    @property
    def value(self):
        with self._lock:
            value = next(self._counter)
            self._number_of_read += self._step
        return value - self._number_of_read
