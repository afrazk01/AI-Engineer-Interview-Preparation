# Interview Prep — Progress Tracker

> Lives in this folder so it's portable and version-controllable. Claude also keeps
> a project-scoped copy in `~/.claude/projects/.../memory/` that loads ONLY for this
> folder (never leaks to other projects).

**Owner:** Afraz — AI Engineer, ~3 YOE
**Started:** 2026-06-03
**Method:** explain-back in own words · write+run code per concept · cold spaced recall · spoken-answer practice. (No passive lectures — they don't stick.)

**Quick-review cram sheets** (read right before any interview call):
`INTERVIEW_QUICK_REVIEW.md` (master) · `Python/NOTES.md` · `Git/notes.md` · `Machine Learning/NOTES.md` · `Deep Learning/NOTES.md` · `DSA/NOTES.md`.

**Current focus (as of 2026-06-23):** DSA coding drills — strings/arrays/two-pointer/hashmaps. The one real gap from the Funavry interview was live coding problem recognition; theory was solid. Then resume ML at L4.

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

## Git Curriculum

Repo: `git@github.com:afrazk01/AI-Engineer-Interview-Preparation.git` (this folder is now the repo).
Afraz handles auth/push himself; Claude preps commits and explains.

- [x] **G1 — Repo basics** ✅ 3 areas, init, .gitignore, add, commit, remote, push.
- [x] **G2/G3 — Commit cycle + branching** ✅ (already knew; verified via diagnostic — skipped)
- [x] **G4 — Merge vs rebase** ✅ HANDS-ON: built real fork, merged (saw diamond + merge commit w/ 2 parents), rebased (saw linear history + new hashes). Golden rule: never rebase shared commits. Fixed "rebase squashes to one commit" misconception.
- [x] **G5 — Undoing: reset vs revert** ✅ revert=new inverse commit (safe/shared); reset=moves branch pointer. Modes: soft=keep staged, mixed=keep unstaged, hard=discard. Demoed soft→hard live to clean up. Quiz passed (--mixed).
- [x] **G6 — fetch vs pull + HEAD** ✅ fetch=download only (safe), pull=fetch+merge; ahead=push/behind=pull; HEAD→branch→commit, detached HEAD. Upstream tracking set.
- [x] **G7 — Merge conflicts** ✅ (concept: markers→edit→add→commit, or `merge --abort`; Afraz skipped hands-on, understands it)
- [ ] G8 — stash/cherry-pick/reflog/tags (overview given; revisit if needed)
- [ ] G9 — Git mock (deferred — may do later)
- _Git parked ~95% done 2026-06-08; moved to ML per Afraz._
- [ ] G7 — Merge conflicts (hands-on resolution)
- [ ] G8 — Interview concepts: HEAD, detached HEAD, cherry-pick, tags, reflog
- [ ] G9 — Git mock interview

---

## Machine Learning Curriculum (started 2026-06-08)

Method: teach LINEAR with intuition+math+code (Afraz rusty on ML, broad gaps in diagnostic). NO LaTeX — plain-text formulas only (terminal doesn't render LaTeX). Full topic list in `Machine Learning/SYLLABUS.md` (CampusX 134).

Diagnostic (2026-06-08): rusty intermediate. Supervised/unsupervised ok; RL wrong; bias-variance/metrics/regularization/etc forgotten. Decided to teach here, not take a course (passive lectures = his retention problem).

- [x] **ML-L1 — Types of ML + Bias-Variance** ✅ 3 types (fixed RL=agent/env/reward); bias=too simple=underfit=bad on both; variance=too complex=overfit=good train/bad test; sweet spot. Killed "bias = the b in y=mx+b" confusion.
- [x] **ML-L2 — Regression metrics** ✅ MAE (robust, avg magnitude), MSE (squares, penalizes big, smooth=training loss), RMSE (√MSE, readable), R² (vs predicting mean). MAE for outliers, MSE when big errors matter.
- [x] **ML-L3 — Regularization (Ridge/Lasso)** ✅ reg adds weight penalty to cut variance/overfitting; Ridge=MSE+λΣw² (shrinks, keeps all features); Lasso=MSE+λΣ|w| (zeros weights = feature selection); ElasticNet=both. Explain-back passed: (1) penalize big weights→smoother func→lower variance; (2) L1 constant ±λ gradient reaches 0 vs Ridge 2λw fades near 0; (3) high λ→penalty dominates→underfit. Tightened the variance bridge + "penalty dominates loss" phrasing. Tune λ via CV.
- [ ] ML-L4 — Classification metrics: accuracy/precision/recall/F1/confusion matrix
- [ ] (then) feature scaling, trees/bagging/boosting, gradient descent, clustering, PCA, imbalanced data, cross-validation — per syllabus

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

### 2026-06-08 → 06-11 — Git + ML start
- Git G1–G7 covered hands-on (predict→run→explain). Parked ~95% done.
- ML started: L1 (types + bias-variance), L2 (regression metrics), L3 (regularization). Resume at L4.

### 2026-06-11/12 — Funavry interview cram
- Deep-dived RAG (chunking, reranking, hybrid/BM25, query transform, lost-in-middle, RAGAS), agents (ReAct, tool-calling, memory, multi-agent, LangGraph), DL core (NN/backprop/activations/vanishing gradient/optimizers/regularization), transformers + attention, LSTM internals. Explain-backs solid.

### 2026-06-12 — Funavry interview DONE (1h20m, senior-level set)
- Theory SOLID across the board. One real gap: live coding problem recognition.
- They asked: **Longest Palindromic Substring** (misread + bugs — got stuck), LangGraph states/nodes + context mgmt, RAG retrieval strategies + latency, multimodal (images → CLIP / caption-then-embed), text-to-SQL agent on big schema, agents/MCP, OOP 4 pillars + diamond/MRO, tokens, FastAPI vs Flask, chunking overlap when/when-not.
- **Takeaway → next cycle = DSA coding drills.** See `DSA/NOTES.md`.

### 2026-06-23 — Notes + repo snapshot
- Wrote quick-review cram sheets across all areas (`INTERVIEW_QUICK_REVIEW.md` + per-folder `NOTES.md`).
- Committing + pushing everything to GitHub (moving to Mac, will pull there).
