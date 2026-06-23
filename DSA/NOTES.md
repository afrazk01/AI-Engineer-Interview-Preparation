# DSA — Coding Drill Notes (NEXT FOCUS)

**Why this is the priority:** in the Funavry interview, theory was solid but the live coding
problem (Longest Palindromic Substring) tripped me up — misread it, didn't reach for the
known pattern. The concept knowledge is strong; the coding muscle is the growth area.
Drill pattern recognition on easy/medium strings + arrays.

## Pre-coding checklist (do this every time)
1. Read the problem twice. Restate it in my own words.
2. Name the pattern out loud (two-pointer? hashmap? sliding window?).
3. State brute force + its complexity, then optimize.
4. Reach for built-ins: `max(seq, key=len)`, `sorted`, `set`, `collections.Counter`.

## Core patterns to drill

### Two-pointer
- Reverse a string/array, palindrome check, pair-sum on sorted array, remove duplicates.
- `l, r = 0, len(s)-1; while l < r: ... l+=1; r-=1`

### Expand-around-center (the one I missed)
- **Longest palindromic substring.** For each center (and each gap between chars), expand outward while equal; track longest.
```python
def longest_palindrome(s):
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]
    best = ""
    for i in range(len(s)):
        for cand in (expand(i, i), expand(i, i+1)):   # odd + even centers
            if len(cand) > len(best):
                best = cand
    return best
```

### Hashmap / counting
- Two-sum (`seen = {}`; check `target - x`), anagram check (`Counter(a) == Counter(b)`), dedupe, frequency.

### Sliding window
- Longest substring without repeating chars, max-sum subarray of size k.
- Grow right, shrink left when constraint breaks.

## Easy warm-ups they actually ask (Funavry intel)
- Reverse a string / reverse an integer (`int(str(n)[::-1])`, handle sign).
- Sum/loop over integers, array max/min, FizzBuzz, check palindrome.

## Common bugs I made — watch for
- `enumerate(len(x)-1)` — enumerate takes an iterable, not an int. Use `range(len(x))` or `enumerate(x)`.
- `[new_list][i]` — wrapping in a list literal then indexing. Just `new_list[i]`.
- Off-by-one in two-pointer / slice bounds.

## Suggested drill order (LeetCode easy→medium)
Strings: reverse string, valid palindrome, longest palindromic substring, valid anagram,
longest substring without repeating chars.
Arrays/hash: two sum, contains duplicate, best time to buy/sell stock, maximum subarray,
group anagrams, product of array except self.
Two-pointer: 3sum, container with most water.
