# Interview Quick-Review (Cram Sheet)

> Open this 30 min before any call. One-screen recall of everything covered.
> Per-topic depth: `Python/NOTES.md`, `Git/notes.md`, `Machine Learning/NOTES.md`,
> `Deep Learning/NOTES.md`. Progress + history in `PROGRESS.md`.
>
> **Answer in 3 beats every time:** (1) direct answer → (2) why/mechanism → (3) rule/trade-off.
> This is the one repeated weakness — first-pass answers come out thin until probed. Front-load the mechanism.

---

## What's been covered (map)
- **Python core** — L1–L8 done, mock 8/8. Refs/mutability, eq/hash, generators, decorators, context managers, GIL/concurrency, complexity.
- **Git** — ~95% done. 3 areas, commit cycle, branching, merge vs rebase, reset vs revert, fetch vs pull, conflicts, HEAD.
- **ML** — L1–L3 done (types, bias-variance, regression metrics, regularization). L4 classification metrics = resume point.
- **DL / LLM stack** — covered in Funavry cram: NN/backprop/activations/optimizers/regularization, transformers+attention, RAG depth, agents.
- **Real interview asked (Funavry, see notes):** longest palindromic substring, LangGraph states/nodes, RAG latency, multimodal, text-to-SQL agent, MCP, OOP/MRO.
- **Growth area:** live coding problem recognition (strings/arrays/two-pointer). Theory is solid; drill DSA next.

---

## Python — one-liners
- **Mutate vs rebind:** `lst.append()` mutates the shared object (caller sees it); `lst = [...]` rebinds the local name (caller doesn't).
- **Mutable default arg:** default is created ONCE at def time and shared across calls. Fix: `def f(x=None): x = x or []`.
- **`__eq__`/`__hash__`:** dict/set lookup = hash→bucket, then `==` to confirm. If you define `__eq__`, define `__hash__` (equal objects must hash equal). Mutable objects shouldn't be hashable.
- **Generators:** `yield` suspends the frame (locals + position), lazy, memory-cheap, single-use. `return` builds the whole thing eagerly.
- **Decorators:** `@d` == `func = d(func)`. Skeleton wraps `*args, **kwargs`; use `functools.wraps` to keep name/docstring.
- **Context managers:** `with` guarantees teardown even on exception (`__enter__`/`__exit__`, or `@contextmanager` + yield).
- **GIL:** only one thread runs Python bytecode at a time (protects refcounting). CPU-bound → multiprocessing (own GIL, true parallel). I/O-bound → threads/asyncio (concurrent, not parallel).
- **Complexity:** list membership O(n), set/dict O(1). Sequential loops add, nested multiply. Binary search O(log n).

## Git — one-liners
- **3 areas:** Working dir →`add`→ Staging →`commit`→ Repo.
- **Merge vs rebase:** merge = new merge commit, preserves history (2 parents). Rebase = replays commits, linear history, NEW hashes. **Never rebase shared/pushed commits.**
- **Reset vs revert:** revert = new inverse commit (safe on shared). reset = moves branch pointer; soft (keep staged), mixed (keep unstaged, default), hard (discard).
- **Fetch vs pull:** fetch = download only (safe). pull = fetch + merge. Ahead→push, behind→pull.
- **HEAD:** pointer to current branch→commit. Detached HEAD = pointing straight at a commit.
- **Conflict:** edit between `<<<< ==== >>>>` markers → `add` → `commit`, or `merge --abort`.

## ML — one-liners
- **3 types:** supervised (labels), unsupervised (structure/clusters), reinforcement (agent/env/reward, learns by trial).
- **Bias-variance:** bias = too simple = underfit (bad on train AND test). Variance = too complex = overfit (great train, bad test). Want the sweet spot.
- **Regression metrics:** MAE (robust to outliers, avg magnitude), MSE (squares → penalizes big errors, smooth training loss), RMSE (√MSE, same units), R² (vs just predicting the mean).
- **Regularization:** add weight penalty → smaller weights → smoother function → lower variance. Ridge = +λΣw² (shrinks, keeps all). Lasso = +λΣ|w| (zeros weights = feature selection). ElasticNet = both. High λ → penalty dominates → underfit. Tune λ via CV.
- **Classification metrics (review L4):** precision = TP/(TP+FP) "of predicted-positive, how many right"; recall = TP/(TP+FN) "of actual-positive, how many caught"; F1 = harmonic mean. Confusion matrix: TP/FP/FN/TN.

## DL / LLM stack — one-liners
- **Backprop:** chain rule from loss back to weights; gradient descent steps weights down the gradient.
- **Activations:** ReLU (default, cheap, dead-neuron risk), sigmoid/tanh (saturate → vanishing gradient), softmax (output probs).
- **Vanishing gradient:** deep/saturating activations shrink gradients → early layers stop learning. Fixes: ReLU, residual connections, batchnorm, careful init.
- **Optimizers:** SGD → momentum → Adam (adaptive per-param LR, default).
- **Regularization (DL):** dropout, weight decay (L2), early stopping, data augmentation.
- **Transformer:** self-attention (Q·K → softmax → weighted V) lets every token attend to every other; multi-head = parallel attention subspaces; positional encodings add order; encoder/decoder blocks + FFN + residual + layernorm. Beats RNN/LSTM on long-range + parallelism.
- **LSTM:** RNN with gates (forget/input/output) + cell state to carry long-range memory and fight vanishing gradients. Still sequential (slow vs transformer).

## RAG — one-liners
- **Pipeline:** chunk → embed → vector store → retrieve top-k → (rerank) → stuff into prompt → generate.
- **Chunking:** size + overlap; overlap preserves context across boundaries; skip overlap for self-contained records.
- **Retrieval quality:** hybrid (dense + BM25/keyword), rerank with cross-encoder (slow, accurate) after bi-encoder recall (fast), query rewriting/expansion.
- **Lost-in-middle:** models weight start/end of context more → put best chunks at edges, keep context tight.
- **Reduce latency:** smaller/faster embed model, cache embeddings + frequent queries, lower top-k, async retrieval, smaller reranker, streaming output.
- **Eval:** RAGAS — faithfulness, answer relevancy, context precision/recall.

## Agents — one-liners
- **ReAct loop:** Thought → Action (tool call) → Observation → repeat → Answer.
- **Tool-calling:** LLM emits structured call (name + args); runtime executes, feeds result back.
- **Memory:** short-term (conversation/scratchpad) vs long-term (vector store).
- **LangGraph:** graph of **nodes** (functions/steps) + **edges**; **state** = a shared typed dict passed/updated through nodes. Manage context by what you keep in state (trim/summarize history, store only needed keys).
- **MCP (Model Context Protocol):** open standard to connect LLMs to external tools/data sources via a uniform server interface.
- **Multi-agent:** specialized agents (planner/worker/critic) coordinate; failure modes = loops, hallucinated tool args, context blowup.

## Patterns for the easy coding round (drill these)
- **Two-pointer:** reverse, palindrome check, pair-sum on sorted.
- **Expand-around-center:** longest palindromic substring (the one that tripped me up). Reach for `max(key=len)`.
- **Hashmap:** two-sum, counts/anagrams, dedupe.
- **Sliding window:** longest substring without repeats, max subarray.
- Read the problem twice; restate it before coding; name the pattern out loud.
