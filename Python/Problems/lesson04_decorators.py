"""
Lesson 4 — Decorators & functools.wraps
Run:  python "Python/Problems/lesson04_decorators.py"
Goal: SEE that @decorator is just  name = decorator(name),
      that *args/**kwargs make it general, and what functools.wraps fixes.
Predict prints before running.
"""
import functools
import time


# ---------------------------------------------------------------------------
# 1. Functions are objects: store one in another name (no parentheses).
# ---------------------------------------------------------------------------
def shout(text):
    return text.upper()

f = shout                       # the function object itself
print("1:", f("hi"))            # PREDICT ___


# ---------------------------------------------------------------------------
# 2. A decorator: takes a function, returns a NEW wrapped function.
# ---------------------------------------------------------------------------
def log_calls(func):
    @functools.wraps(func)              # copy func's identity onto wrapper
    def wrapper(*args, **kwargs):       # accept ANY arguments
        print(f"   -> calling {func.__name__} with {args} {kwargs}")
        result = func(*args, **kwargs)  # forward them; call the original
        print(f"   -> {func.__name__} returned {result}")
        return result                   # MUST return, or caller gets None
    return wrapper


@log_calls                      # means:  add = log_calls(add)
def add(a, b):
    return a + b

print("2:", add(3, 4))          # PREDICT: two log lines, then 7


# ---------------------------------------------------------------------------
# 3. Prove @ is just  name = decorator(name).
# ---------------------------------------------------------------------------
def mul(a, b):
    return a * b

mul = log_calls(mul)            # exactly what @log_calls would do
print("3:", mul(5, 6))          # PREDICT ___


# ---------------------------------------------------------------------------
# 4. functools.wraps: identity preserved vs masked.
# ---------------------------------------------------------------------------
def bad_decorator(func):
    def wrapper(*args, **kwargs):       # NO @wraps here
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def greet():
    "say hello"                         # docstring
    return "hello"

@log_calls                              # this one HAS @wraps
def farewell():
    "say bye"
    return "bye"

print("4: bad  name:", greet.__name__,    "| doc:", greet.__doc__)     # masked
print("5: good name:", farewell.__name__, "| doc:", farewell.__doc__)  # preserved


# ---------------------------------------------------------------------------
# 5. THE Q5 ASK: a retry decorator. Retries up to N times with a delay.
#    Note the EXTRA layer: retry(times, delay) RETURNS a decorator.
# ---------------------------------------------------------------------------
def retry(times=3, delay=0.1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_err = None
            for attempt in range(1, times + 1):
                try:
                    print("time values:", times, delay)
                    return func(*args, **kwargs)        # success -> return now
                except Exception as e:
                    last_err = e
                    print(f"   attempt {attempt} failed: {e}")
                    if attempt < times:
                        time.sleep(delay)
            raise last_err                              # all attempts failed
        return wrapper
    return decorator


attempts = {"n": 0}
@retry(times=3, delay=0.05)
def flaky():
    attempts["n"] += 1
    if attempts["n"] < 3:
        raise ValueError(f"boom #{attempts['n']}")
    return "succeeded on attempt 3"

print("6:", flaky())            # PREDICT: 2 failure lines, then success
