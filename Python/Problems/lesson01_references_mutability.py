"""
Lesson 1 — References & Mutability
Run:  python "lesson01_references_mutability.py"
Goal: SEE that names point at objects. Predict each print BEFORE running.
"""

# ---------------------------------------------------------------------------
# 1. A name is an arrow to an object, not a box holding a value.
# ---------------------------------------------------------------------------
a = [1, 2, 3]
b = a               # copies the arrow, not the list
b.append(4)
print("1:", a)      # PREDICT before running ___

# id() shows the object's identity (its address). Same id = same object.
print("2:", id(a) == id(b))   # PREDICT ___


# ---------------------------------------------------------------------------
# 2. Mutable vs immutable. Reassigning an int makes a NEW object.
# ---------------------------------------------------------------------------
x = 10
y = x
y = y + 1           # ints are immutable: this rebinds y to a new object 11
print("3:", x, y)   # PREDICT ___   (does x change?)


# ---------------------------------------------------------------------------
# 3. The mutable-default-argument trap (your Q2).
#    Default [] is created ONCE at definition time and reused every call.
# ---------------------------------------------------------------------------
def add_buggy(item, bucket=[]):
    bucket.append(item)
    return bucket

print("4:", add_buggy(1))   # PREDICT ___
print("5:", add_buggy(2))   # PREDICT ___  (surprised?)


def add_fixed(item, bucket=None):
    if bucket is None:      # sentinel -> fresh list each call
        bucket = []
    bucket.append(item)
    return bucket

print("6:", add_fixed(1))   # PREDICT ___
print("7:", add_fixed(2))   # PREDICT ___


# ---------------------------------------------------------------------------
# 4. Passing a mutable into a function mutates the caller's object.
# ---------------------------------------------------------------------------
def wipe(lst):
    lst.clear()             # mutates in place -> visible outside

nums = [1, 2, 3]
wipe(nums)
print("8:", nums)           # PREDICT ___


# ---------------------------------------------------------------------------
# 5. But REBINDING inside a function does NOT affect the caller.
# ---------------------------------------------------------------------------
def rebind(lst):
    lst = [99]              # new local arrow; caller's arrow untouched

keep = [1, 2, 3]
rebind(keep)
print("9:", keep)           # PREDICT ___  (the subtle one)

def rebind2(lst):
    lst = [99]
    return lst

print("10:", rebind2(keep))  # PREDICT ___  (the subtle one, again)     

print("-----------------------------------------")
def f(d):
    d["x"] = 1      # line A
    d["y"] = 3      # line C
    d = {"y": 2}    # line B


m = {}
f(m)
print(m)