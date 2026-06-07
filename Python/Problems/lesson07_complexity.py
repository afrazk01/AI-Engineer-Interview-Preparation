"""
Lesson 7 — Complexity & data structures
Run:  python "Python/Problems/lesson07_complexity.py"
Goal: MEASURE that list membership is O(n) and set membership is O(1),
      and that the Q7 comprehension goes from O(n*m) to O(n+m) with a set.
"""
import time


def time_it(label, fn):
    start = time.perf_counter()
    result = fn()
    print(f"   {label:<34} {time.perf_counter() - start:.4f}s   (result={result})")


# ---------------------------------------------------------------------------
# 1. Membership: list (O(n) scan) vs set (O(1) hash lookup).
#    We look up a value that is at the END / not present -> worst case for list.
# ---------------------------------------------------------------------------
N = 2_000_000
big_list = list(range(N))
big_set  = set(big_list)
target   = N - 1            # last element -> list must scan everything

print("1: membership of the LAST element (worst case for list):")
time_it("list  (O(n): scans ~N items)", lambda: target in big_list)
time_it("set   (O(1): one hash lookup)", lambda: target in big_set)


# ---------------------------------------------------------------------------
# 2. The Q7 comprehension: O(n*m) with list_b vs O(n+m) with set_b.
# ---------------------------------------------------------------------------
n = 20_000
list_a = list(range(n))
list_b = list(range(n, 2 * n))      # disjoint -> every `in` check scans fully

print("\n2: [x for x in list_a if x in list_b]  (n =", n, "):")
time_it("x in list_b  (O(n*m))", lambda: len([x for x in list_a if x in list_b]))

set_b = set(list_b)
time_it("x in set_b   (O(n+m))", lambda: len([x for x in list_a if x in set_b]))


# ---------------------------------------------------------------------------
# 3. O(1) operations don't care about size: index & dict lookup.
# ---------------------------------------------------------------------------
small = list(range(10))
huge  = list(range(10_000_000))
d     = {i: i for i in range(10_000_000)}

print("\n3: O(1) ops — same speed regardless of size:")
time_it("index small[5]", lambda: small[5])
time_it("index huge[5_000_000]", lambda: huge[5_000_000])
time_it("dict lookup d[9_999_999]", lambda: d[9_999_999])
