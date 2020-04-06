"""Overloading a circuit breaker"""

class CircuitBreaker:

    def _init_(self, max_amps):
        self.capacity = max_amps
        self.load = 0

    def connect (self,amp):
        if self.load + amps.capacity:
            self.load += amps

cb = CircuitBreaker(20)
