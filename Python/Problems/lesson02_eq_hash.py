"""
Lesson 2 — __eq__ and __hash__
Run:  python "Python/Problems/lesson02_eq_hash.py"
Goal: SEE why dict/set need both hash() and ==, and what breaks without each.
Predict every print BEFORE running.
"""

# ---------------------------------------------------------------------------
# 1. Why list/dict are unhashable: their hash would change if they mutate.
# ---------------------------------------------------------------------------
print("1:", hash("abc"))          # str is immutable -> hashable
print("2:", hash((1, 2)))         # tuple of immutables -> hashable
try:
    hash([1, 2])                  # list is mutable -> NOT hashable
except TypeError as e:
    print("3:", "list error:", e)


# ---------------------------------------------------------------------------
# 2. Define __eq__ but NOT __hash__  ->  instances become unhashable.
# ---------------------------------------------------------------------------
class PersonBad:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return isinstance(other, PersonBad) and self.name == other.name

try:
    s = {PersonBad("ana")}        # PREDICT: works or error?
    print("4:", s)
except TypeError as e:
    print("4:", "error:", e)


# ---------------------------------------------------------------------------
# 3. Define BOTH, consistently. Now equal objects collapse in a set.
# ---------------------------------------------------------------------------
class Person:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name
    def __hash__(self):
        return hash(self.name)
    def __repr__(self):
        return f"Person({self.name!r})"

a, b = Person("ana"), Person("ana")
print("5:", a == b)               # PREDICT ___
print("6:", hash(a) == hash(b))   # PREDICT ___  (contract!)
print("7:", {a, b})               # PREDICT: how many in the set?

d = {a: "first"}
print("8:", d[b])                 # PREDICT: can b find a's entry?


# ---------------------------------------------------------------------------
# 4. BREAK THE CONTRACT on purpose: equal objects, different hashes.
#    This is the silent bug Python's default tries to protect you from.
# ---------------------------------------------------------------------------
class Broken:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return isinstance(other, Broken) and self.name == other.name
    def __hash__(self):
        return id(self)           # WRONG: equal objects get different hashes

x, y = Broken("ana"), Broken("ana")
print("9:", x == y)               # PREDICT ___
dd = {x: "stored"}
print("10:", y in dd)             # PREDICT: y == x but can the dict find it?
