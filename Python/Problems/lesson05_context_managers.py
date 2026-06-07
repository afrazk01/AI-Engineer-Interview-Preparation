"""
Lesson 5 — Context managers
Run:  python "Python/Problems/lesson05_context_managers.py"
Goal: SEE that `with` guarantees teardown even on exceptions, and that the two
      ways (class vs @contextmanager) are equivalent.
Predict prints before running.
"""
import time
from contextlib import contextmanager


# ---------------------------------------------------------------------------
# 1. The guarantee: teardown runs EVEN IF the block raises.
# ---------------------------------------------------------------------------
class Resource:
    def __enter__(self):
        print("   __enter__: acquire resource")
        return self                          # bound to `as r`
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"   __exit__: release resource (exception was: {exc_type})")
        return False                         # False -> do NOT suppress exception

print("1: normal exit ---")
with Resource() as r:
    print("   inside block, all good")

print("2: exit via exception ---")
try:
    with Resource() as r:
        print("   inside block, about to fail")
        raise ValueError("boom")
except ValueError as e:
    print("   caught outside:", e)           # __exit__ STILL ran before this


# ---------------------------------------------------------------------------
# 2. __enter__ return value is what `as` binds. exc args describe the error.
# ---------------------------------------------------------------------------
class Suppressor:
    def __enter__(self):
        return "the-as-value"
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"   exit args: type={exc_type}, val={exc_val}")
        return True                          # True -> SUPPRESS the exception

print("3: as-binding + suppression ---")
with Suppressor() as x:
    print("   as bound to:", x)              # PREDICT ___
    raise RuntimeError("this gets swallowed")
print("   reached here? (yes, because __exit__ returned True)")  # PREDICT runs or not?


# ---------------------------------------------------------------------------
# 3. The @contextmanager (generator) version. yield splits setup/teardown.
# ---------------------------------------------------------------------------
@contextmanager
def timer(label):
    start = time.perf_counter()              # setup (before yield) == __enter__
    print(f"   [{label}] start")
    try:
        yield label                          # the `with` body runs here
    finally:
        dur = time.perf_counter() - start    # teardown (after yield) == __exit__
        print(f"   [{label}] done in {dur:.4f}s")

print("4: @contextmanager timer ---")
with timer("work") as lbl:
    total = sum(range(1_000_000))
    print("   computed inside:", lbl, total > 0)


# ---------------------------------------------------------------------------
# 4. finally still runs even if the body raises (prove the guarantee).
# ---------------------------------------------------------------------------
print("5: timer teardown survives exception ---")
try:
    with timer("risky"):
        raise KeyError("oops")
except KeyError:
    print("   caught KeyError; note the [risky] done line printed BEFORE this")
