# RAG Problem Discussion - Homework A01

## Session Date: 2026-02-02

## Problem Summary

**Random Allocation Game (RAG):**
- 10 participants flip a coin privately
- If heads, they win a prize (10 Euros)
- Participants can lie (claim heads when they got tails)
- **Observed data:** 8 out of 10 claimed the prize

**Questions:**
1. How many ways to get 8 claims if ALL are honest?
2. How many ways if exactly 5 are honest?
3. What number of honest participants maximizes the number of ways?

---

## Key Concepts Learned

### Likelihood vs Probability vs Posterior

- **Likelihood** = P(data | hypothesis) = "probability of the data given the hypothesis"
  - Example: P(8 claims | all honest) = 45/1024 ≈ 0.044
  - This is what we're calculating with the "garden of forking data"

- **Posterior** = P(hypothesis | data) = "probability of the hypothesis given the data"
  - Requires Bayes' rule: combines likelihood with prior beliefs
  - NOT what we're calculating here (yet)

### The Generative Model

**First attempt (WRONG):**
```python
case_claimed_wins = numpy.maximum(n_real_wins, n_dishonest)
```
- Treated participants as undifferentiated mass
- Didn't model WHO is honest, just counts
- Produced nonsensical results (e.g., n_honest=2 gave 1013 ways)

**Key insight:** A bad model reveals itself through its implications, even with zero data!

**Corrected model:**
```python
n_real_wins_of_honest_people = numpy.sum(omega[idx_case, 0:n_honest])
n_fake_claims = n_dishonest  # dishonest always claim
case_claimed_wins = n_real_wins_of_honest_people + n_fake_claims
```

### The Exchangeability Argument

**Question raised:** Should we multiply by C(10, n_honest) to account for all ways to choose which participants are honest?

**Answer:** No! Because participants are **exchangeable**.

**Reasoning:**
1. The data is just "8 claims" (not which specific people claimed)
2. All configurations of which-5-are-honest give the SAME count (320)
3. These configurations are symmetric and observationally equivalent

**Mathematical proof that it doesn't matter:**
- Your approach: 320/1024 = 0.3125
- Full combinatorial: (C(10,5) × 320) / (C(10,5) × 1024) = 0.3125

The C(10,5) cancels out! The "sorting chairs before flipping" simplification is valid.

---

## Current Results

```
Q1: All honest (10/10) -> 45 ways -> likelihood 0.0439

Q2 results:
n_honest=0  -> 0 ways   -> likelihood 0.0000 (all claim 10, not 8)
n_honest=1  -> 0 ways   -> likelihood 0.0000
n_honest=2  -> 256 ways -> likelihood 0.2500
n_honest=3  -> 384 ways -> likelihood 0.3750
n_honest=4  -> 384 ways -> likelihood 0.3750
n_honest=5  -> 320 ways -> likelihood 0.3125
n_honest=6  -> 240 ways -> likelihood 0.2344
n_honest=7  -> 168 ways -> likelihood 0.1641
n_honest=8  -> 112 ways -> likelihood 0.1094
n_honest=9  -> 72 ways  -> likelihood 0.0703
n_honest=10 -> (not yet tested, should be 45)
```

**Sanity checks passed:**
- n_honest=0: All 10 dishonest → 10 claims → 0 ways ✓
- n_honest=2: Need 0 heads from 2 honest → 2^8 outcomes work → 256 ✓
- n_honest=5: Need 3 heads from 5 → C(5,3) × 2^5 = 10 × 32 = 320 ✓

---

## TODO: Question 3

Find n_honest that **maximizes** the number of ways (maximum likelihood estimate).

From the Q2 results, it looks like **n_honest = 3 or 4** (both give 384 ways).

Need to:
1. Fix the loop to include n_honest=10
2. Implement Q3 to find and report the maximum
3. Think about what this means: the MLE suggests 3-4 honest people!

---

## Code Location

`/home/mib07150/git/private/statistical-rethinking/exercises/homework_A01/rag_problem.py`

---

## References

- Statistical Rethinking 2026, Homework A01
- Chapters 1 & 2 (2nd edition) - "Garden of Forking Data"
- Lecture videos: Section A playlist
