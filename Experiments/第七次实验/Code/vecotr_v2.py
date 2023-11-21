import math

class Vector:
    def __init__(self, components):
        self.components = components

    def add(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be the same dimension")
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def subtract(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be the same dimension")
        return Vector([a - b for a, b in zip(self.components, other.components)])

    def dot(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be the same dimension")
        return sum(a * b for a, b in zip(self.components, other.components))

    def norm(self):
        return math.sqrt(sum(x**2 for x in self.components))

    def __str__(self):
        return '(' + ','.join(map(str, self.components)) + ')'

    def equals(self, other):
        return self.components == other.components