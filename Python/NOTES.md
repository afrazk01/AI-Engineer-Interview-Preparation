# Python Core — Interview Notes (L1–L8)

Status: **DONE, mock 8/8.** Code per lesson in `Python/Problems/lesson01..07_*.py`.
Answer in 3 beats: direct → mechanism → rule.

## L1 — References & mutability
- Names are references to objects. `x = y` copies the reference, not the object.
- **Mutate** (`lst.append(1)`, `d[k]=v`) changes the shared object → all names see it.
- **Rebind** (`lst = [...]`) points the local name elsewhere → caller's name unaffected.
- Immutables (int, str, tuple) can't be mutated; "changing" them rebinds.
- Mutable default arg trap: default object created once at `def` time, shared across calls. Fix: `def f(a=None): a = [] if a is None else a`.

## L2 — Hashing: `__eq__` / `__hash__`
- Dict/set lookup = two steps: hash(key) → bucket, then `==` to confirm identity in bucket.
- Contract: if `a == b` then `hash(a) == hash(b)`. Define both together.
- Define `__eq__` without `__hash__` → object becomes unhashable (Python sets `__hash__=None`).
- Mutating an object after it's a dict key/set member breaks lookup (hash changed). Keys should be immutable.

## L3 — Generators & iterators
- `yield` produces values lazily, one at a time; suspends the frame (locals + position) and resumes on next `next()`.
- Memory-cheap (don't materialize) — good for streams/large/infinite sequences.
- Single-use: once exhausted, it's done; re-iterating yields nothing.
- `return` builds the whole result eagerly in memory.

## L4 — Decorators & `functools.wraps`
- `@d` over `func` == `func = d(func)`. A decorator takes a function, returns a wrapped function.
- Skeleton: `def d(fn): def wrapper(*args, **kwargs): ...; return fn(...); return wrapper`.
- `@functools.wraps(fn)` copies name/docstring/metadata to the wrapper.
- Closures: the wrapper closes over `fn` (and any decorator args). Used for retry, timing, caching, auth.

## L5 — Context managers
- `with` guarantees setup/teardown even if the body raises (no leaked files/locks/connections).
- Class form: `__enter__` (returns resource) / `__exit__` (cleanup; return True to swallow exception).
- Function form: `@contextlib.contextmanager` + `yield` (setup before yield, teardown after).

## L6 — GIL: threads vs async vs multiprocessing
- **GIL** = only one thread executes Python bytecode at a time; protects internal state (refcounting).
- **CPU-bound** → multiprocessing: separate processes, each its own GIL → true parallelism.
- **I/O-bound** → threads: while one waits on I/O, another runs (GIL released during I/O).
- **Many concurrent I/O** → asyncio: single thread, cooperative `await`, concurrent not parallel.
- Two canonical sentences to drill: "GIL means one thread runs bytecode at a time." / "Concurrency = dealing with many at once; parallelism = doing many at once."

## L7 — Complexity & data structures
- Big-O = growth shape, drop constants. O(1) < O(log n) < O(n) < O(n log n) < O(n²).
- list/tuple membership `in` = O(n); set/dict = O(1) average (hash).
- De-dupe / intersection: convert to set → O(n+m) instead of O(n*m).
- Sequential loops add; nested loops multiply. Binary search / halving = O(log n).

## L8 — Mock takeaway
- 8/8 cold recall passed. Concepts retained.
- **Weakness to keep drilling: first-pass completeness.** Answers were correct but thin until probed. Always give the 3-beat answer unprompted.
