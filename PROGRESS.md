# Interview Prep — Progress Tracker

> Lives in this folder so it's portable and version-controllable. Claude also keeps
> a project-scoped copy in `~/.claude/projects/.../memory/` that loads ONLY for this
> folder (never leaks to other projects).

**Owner:** Afraz — AI Engineer, ~3 YOE
**Started:** 2026-06-03
**Method:** explain-back in own words · write+run code per concept · cold spaced recall · spoken-answer practice. (No passive lectures — they don't stick.)

---

## Baseline (Python diagnostic, 2026-06-03)

Level: **junior-to-early-mid**. Lecture exposure, weak retention & mechanism-level depth.

| Q | Topic | Result |
|---|-------|--------|
| 1 | `__eq__`/`__hash__` | Miss |
| 2 | Mutable default arg | Half (missed root cause: shared default) |
| 3 | Generators | Half |
| 4 | GIL | Miss (thought it was "Language", backwards) |
| 5 | Decorators | Miss |
| 6 | Shallow vs deep copy | **Good** |
| 7 | Comprehension complexity | Half (said O(n), is O(n*m)) |
| 8 | Context managers | Half |

---

## Python Curriculum

- [x] **L1 — References & mutability** ✅ passed cold check (mutate vs rebind, default trap, immutability rationale, return semantics)
- [x] **L2 — Hashing: `__eq__`/`__hash__`** ✅ two-step lookup (hash→bucket, ==→confirm), eq/hash contract, traced contract-violation bug
- [x] **L3 — Generators & iterators** ✅ yield vs return, lazy/memory use-cases, single-use gotcha, under-the-hood frame suspension model
- [x] **L4 — Decorators & `functools.wraps`** ✅ @=func=decorator(func), *args/**kwargs skeleton, wraps preserves metadata, traced retry decorator + closures (Q5 miss now fixed)
- [x] **L5 — Context managers** ✅ `with` guarantees teardown even on exception; class (`__enter__`/`__exit__`) + `@contextmanager` (Q8 fixed)
- [x] **L6 — GIL: threads vs async vs multiprocessing** ✅ GIL=one thread runs bytecode (protects refcounting); CPU→multiproc (own GIL/parallel), I/O→threads, many I/O→asyncio (concurrent not parallel). Q4 fixed. NOTE: articulation rough — drill the two canonical sentences in L8 mock.
- [x] **L7 — Complexity & data structures** ✅ Big-O shapes, list vs set membership (O(n) vs O(1)), Q7 fixed (O(n*m)→O(n+m) via set), sequential=add/nested=multiply, logs & binary search O(log n)
- [x] **L8 — Mock interview (cold recall L1–L7)** ✅ 8/8 passed. Concepts retained. Weakness: first-pass completeness — answers were thin until probed. Drill: answer in 3 beats (direct answer → why/mechanism → fix/rule) unprompted.

Then: Git → DSA → ML → DL.

---

## Session Log

### 2026-06-03 — Session 1
- Ran 8-question Python diagnostic (see baseline above).
- Set up method + curriculum.
- Started L1; file: `Python/Problems/lesson01_references_mutability.py`.
- **L1 PASSED.** Afraz ran the file, explored `return` semantics on his own, corrected the "return modifies caller" misconception, passed the mutate-vs-rebind cold check. Strong active engagement.
- **L2 PASSED.** File `Python/Problems/lesson02_eq_hash.py`. Afraz reached correct two-step lookup model on his own after one tightening; traced why #10 (`y in dd`) is False. Likes line-by-line walkthroughs of code.
- **L3 PASSED.** File `lesson03_generators.py`. Afraz explained yield/return + use-cases correctly, experimented independently (extra `list(gen)` confirming single-use), asked for under-the-hood mechanism (got frame-suspension explanation). Minor wording fix: generator remembers *frame/locals/position*, not "what it returned".
- **L4 PASSED.** File `lesson04_decorators.py`. Afraz stated `@decorator == func=decorator(func)` cleanly, explained wraps, asked for line-by-line of retry decorator (got it, incl. closures explanation). Closures introduced here — reuse in L6 (async). Q5 baseline miss now closed.
- **L4 PASSED** (see above).

### Sessions 2-3 (through 2026-06-06)
- **L5, L6, L7 PASSED.** All 8 original baseline misses now closed.
  - L5 context managers: `with` guarantees teardown on exception.
  - L6 GIL: concept solid, articulation rough — drill the two canonical sentences + concurrency-vs-parallelism in mock.
  - L7 complexity: Big-O, list O(n) vs set O(1) membership, Q7 fix, logs/binary search.
- Added `Machine Learning/SYLLABUS.md` (CampusX 100 Days, 134 videos) for the ML phase later.
- **Next:** L8 — full mock interview, cold recall across L1-L7. Then Git.
