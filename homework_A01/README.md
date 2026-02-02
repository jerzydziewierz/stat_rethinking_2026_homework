# Homework A01 - Random Allocation Game (RAG)

## Background

To study honesty, behavioral scientists have used an experiment called the Random Allocation Game (RAG). In a RAG, participants are given a single coin. Participants flip the coin, and if the result is heads, they win a small cash prize (like 10 Euros). Participants flip the coin in private—the experimenter cannot see or verify the result, and participants know this.

While it is impossible to know if any individual participant honestly obeys the result of the coin flip, in the aggregate the proportion of prize claims provides information about the frequency of honesty in the sample. For example, if everyone claims the prize, then probably a lot of them are liars.

## The Problem

Suppose 10 participants play a RAG and 8 of them claim the prize.

Using the "garden of forking data" approach, answer the following questions:

### Question 1
**How many ways are there to realize this sample (8 out of 10), if all participants are honest?**

### Question 2
**How many ways are there to realize this sample (8 out of 10), if 5 of the participants are honest?**

### Question 3
**Can you figure out the number of honest participants that maximizes the number of ways to realize the observed sample (8 out of 10)?**

## Approach

Start with the most naive method - enumerate all possible outcomes and count them. Don't jump to closed-form solutions yet!

Think about:
- What outcomes can honest participants produce?
- What outcomes can dishonest participants produce?
- How do you combine these to get 8 total prize claims?

## References

Review Chapters 1 and 2 (2nd edition) for the "garden of forking data" concept.
