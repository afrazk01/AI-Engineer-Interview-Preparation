# Deep Learning + LLM Stack — Interview Notes

Covered in the Funavry cram (transformers, LSTMs, RAG, agents). These are the highest-yield
topics for a 3-YOE AI engineer and what real interviews drilled. Answer in 3 beats.

## Neural net fundamentals
- **Neuron:** weighted sum + bias → activation. Layers stack; "deep" = many hidden layers.
- **Forward pass:** input → layers → output → loss.
- **Backprop:** chain rule propagates loss gradient back to every weight.
- **Gradient descent:** w ← w − lr·∂L/∂w. Variants: batch / SGD / mini-batch (mini-batch = default).
- **Activations:** ReLU (default, cheap, can "die"), LeakyReLU (fixes dead neurons), sigmoid/tanh (saturate → vanishing gradient), softmax (multiclass output probs).
- **Vanishing/exploding gradients:** deep nets + saturating activations shrink/blow gradients. Fixes: ReLU, residual/skip connections, batchnorm, good init (He/Xavier), gradient clipping.
- **Optimizers:** SGD → +momentum → Adam (adaptive per-parameter LR, the default).
- **Regularization:** dropout (randomly zero activations), L2/weight decay, early stopping, data augmentation, batchnorm.
- **Loss:** MSE (regression), cross-entropy / BCE (classification).

## CNN (briefly)
- Convolution = sliding filter detects local patterns (edges→textures→objects); weight sharing → few params.
- Pooling downsamples (translation invariance). Good for images/spatial data.

## RNN / LSTM
- **RNN:** processes sequences step-by-step, hidden state carries memory. Suffers vanishing gradients on long sequences.
- **LSTM:** adds a **cell state** + 3 gates — **forget** (drop old info), **input** (write new), **output** (what to expose). Gates let gradients flow → long-range memory.
- **GRU:** simpler LSTM (reset + update gates), fewer params.
- Limitation: sequential → slow, limited long-range vs transformers.

## Transformers (most important)
- **Self-attention:** for each token, Query·Key dot products → softmax → weights over all tokens → weighted sum of Values. Lets every token look at every other token directly (long-range, parallel).
- **Scaled dot-product:** divide by √d_k to keep softmax stable.
- **Multi-head attention:** several attention heads in parallel learn different relations, then concatenate.
- **Positional encoding:** attention is order-agnostic, so inject position info (sinusoidal or learned).
- **Block:** attention → add & layernorm → feed-forward → add & layernorm (residuals everywhere).
- **Encoder** (BERT, bidirectional), **decoder** (GPT, causal/masked), **encoder-decoder** (T5, translation).
- Why beat RNN/LSTM: parallelizable (no sequential dependency) + direct long-range attention.

## RAG (Retrieval-Augmented Generation)
- **Pipeline:** documents → chunk → embed → vector DB → retrieve top-k by similarity → (rerank) → inject into prompt → LLM generates grounded answer.
- **Chunking:** balance size vs context; overlap preserves meaning across boundaries; skip overlap for self-contained records.
- **Retrieval strategies:** dense (embeddings) + sparse (BM25/keyword) = **hybrid**; **bi-encoder** for fast recall, **cross-encoder reranker** for accurate top-k ordering; query rewriting/expansion/HyDE.
- **Lost-in-the-middle:** LLMs attend to start/end of context more → place best chunks at edges, keep context tight.
- **Reduce latency:** cache embeddings + frequent queries, smaller/faster embed model, lower top-k, async retrieval, lighter reranker, stream output, pre-filter by metadata.
- **Eval (RAGAS):** faithfulness, answer relevancy, context precision, context recall.

## Agents
- **ReAct loop:** Thought → Action (tool) → Observation → … → Final Answer.
- **Tool/function calling:** LLM outputs structured call (name + JSON args); runtime executes, returns result, loop continues.
- **Memory:** short-term (conversation/scratchpad in context) vs long-term (vector store).
- **LangGraph:** **nodes** = steps/functions, **edges** = control flow (can be conditional), **state** = shared typed dict updated as it flows. Manage context by what you keep in state — trim or summarize history, store only needed keys, route with conditional edges.
- **Multi-agent:** planner / worker / critic specialization; orchestrator coordinates.
- **Failure modes:** infinite loops, hallucinated tool args, context overflow, error propagation. Mitigate with step limits, validation, retries, guardrails.
- **MCP (Model Context Protocol):** open standard for connecting LLMs to tools/data via uniform servers — plug-and-play tool integration.

## Real interview questions seen (Funavry) — be ready
- **Multimodal "data has images":** use multimodal embeddings (CLIP) to embed images+text in one space, OR caption images with a VLM then embed the captions.
- **Text-to-SQL on a big unknown schema:** SQL agent — first retrieve the relevant tables/columns (schema is too big to dump), feed that subset → generate SQL → execute → optionally self-correct on errors.
- **FastAPI vs Flask:** FastAPI = async, ASGI, Pydantic validation, auto OpenAPI docs, faster; Flask = sync, WSGI, simpler/older.
- **OOP 4 pillars:** encapsulation, abstraction, inheritance, polymorphism. **Diamond problem:** multiple inheritance ambiguity → Python resolves via MRO (C3 linearization); check `Cls.__mro__`.
- **Tokens:** sub-word units (BPE); models bill and limit by token count.
