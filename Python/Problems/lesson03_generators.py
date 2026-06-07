"""
Lesson 3 — Generators & Iterators
Run:  python "Python/Problems/lesson03_generators.py"
Goal: SEE that yield pauses/resumes, state is kept between calls, and values
      are produced lazily (on demand). Predict prints before running.
"""

# ---------------------------------------------------------------------------
# 1. The iterator protocol that `for` uses under the hood.
# ---------------------------------------------------------------------------
nums = [10, 20, 30]
it = iter(nums)
print("0:", it)                 # get an iterator from an iterable
print("1:", next(it))           # PREDICT ___
print("2:", next(it))           # PREDICT ___
print("3:", next(it))           # PREDICT ___
try:
    next(it)                    # nothing left
except StopIteration:
    print("4:", "StopIteration -> loop would end here")


# ---------------------------------------------------------------------------
# 2. yield = pause button. Calling the function runs NO code yet.
# ---------------------------------------------------------------------------
def count_up(n):
    print("   [generator body STARTED]")   # watch WHEN this prints
    i = 0
    while i < n:
        yield i                 # pause, hand out i, freeze state
        i += 1
    print("   [generator body ENDED]")

g = count_up(3)
print("5: created generator, body not run yet?")   # body print appears AFTER this
print("6:", next(g))            # PREDICT: prints body-started THEN 0
print("7:", next(g))            # PREDICT ___  (resumes; no 'STARTED' again)
print("8:", next(g))            # PREDICT ___


# ---------------------------------------------------------------------------
# 3. State is remembered between calls (a running total).
# ---------------------------------------------------------------------------
def running_total(items):
    total = 0
    for x in items:
        total += x
        yield total             # local 'total' survives across next() calls

print("9:", list(running_total([1, 2, 3, 4])))   # PREDICT ___


# ---------------------------------------------------------------------------
# 4. A generator is single-use: once exhausted, it's empty.
# ---------------------------------------------------------------------------

gen = (x * x for x in range(3))     # generator EXPRESSION: () not []
print("10:", list(gen))             # PREDICT ___
print("11:", list(gen))             # PREDICT ___  (gotcha: run it twice?)
print("11A:", list(gen))
# ---------------------------------------------------------------------------
# 5. Memory: generator expression vs list comprehension.
#    Both sum the same thing; only one builds a giant list in RAM.
# ---------------------------------------------------------------------------
import sys
list_version = [x for x in range(100_000)]
gen_version  = (x for x in range(100_000))
print("12: list bytes :", sys.getsizeof(list_version))   # big
print("13: gen  bytes :", sys.getsizeof(gen_version))    # tiny & constant


# ---------------------------------------------------------------------------
# 6. AI-style streaming: yield tokens one at a time as they're "produced".
# ---------------------------------------------------------------------------
def stream_tokens(sentence):
    for word in sentence.split():
        yield word              # imagine each arriving from an LLM over time

for tok in stream_tokens("generators stream tokens lazily"):
    print("14:", tok)           # printed as each is produced, not all at once
