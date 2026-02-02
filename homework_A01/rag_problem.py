"""
Random Allocation Game (RAG) - Homework A01
Statistical Rethinking 2026

Problem: 10 participants play a RAG, 8 claim the prize.
Using "garden of forking data" approach, calculate the number of ways
to realize this outcome under different honesty assumptions.
"""
import numpy


# Constants
TOTAL_PARTICIPANTS = 10
PRIZE_CLAIMS = 8

def create_omega(n_total):
    """
    Create the sample space (omega) for n_total participants.
    Each participant can either claim the prize (1) or not (0).

    Args:
        n_total: Total number of participants
    :returns
        omega: A 2D numpy array where each row represents a possible outcome
                and each column represents a participant's actual result (0 or 1), irrespective of his claim
    """
    # approach: there have been n_total participants, and for each, the outcome is either 1 or 0.
    # let's have a (n_total)-bit binary number, where each bit represents the outcome of a participant.
    numbers = numpy.arange(2**n_total).astype(numpy.int32)
    # convert to binary representation

    omega  = numpy.zeros([2**n_total,n_total])
    for idx_number in range(omega.shape[0]):
        for idx_participant in range(omega.shape[1]):
            omega[idx_number, idx_participant] = (numbers[idx_number] >> idx_participant) & 1

    return(omega)


def count_ways_naive(n_honest, n_total, n_prizes):
    """
    Calculate the number of ways to get n_prizes claims from n_total participants,
    where n_honest are honest and the rest are dishonest.

    This is the NAIVE approach - enumerate all possibilities and count them.

    Args:
        n_honest: Number of honest participants
        n_total: Total number of participants
        n_prizes: Number of prize claims observed

    Returns:
        Number of ways to realize the observed outcome

    Think about:
    - Honest participants: flip a coin (heads=1, tails=0), report truthfully
    - Dishonest participants: always claim the prize (always 1)
    - Need to count all combinations that sum to n_prizes
    """
    # TODO: Implement your solution here
    # Hint: You might want to enumerate all possible coin flip outcomes for honest participants
    # and see which combinations work




def question_1(omega, n_claims=8):
    """
    Q1: How many ways if ALL participants are honest?
    """
    ways = 0
    for idx_case in range(omega.shape[0]):
        if numpy.sum(omega[idx_case,:]) == n_claims:
            ways += 1


    print(f"Q1: All honest, {n_claims=} -> {ways} ways out of {omega.shape[0]} total cases")
    print(f'Q1: Likehood of observing {n_claims} claims if all are honest: {ways/omega.shape[0]:.4f}')
    print(f'===' * 60)
    return ways


def question_2(n_honest = 5, n_claims=8):
    """
    Q2: How many ways if exactly 5 participants are honest?
    """
    n_dishonest = TOTAL_PARTICIPANTS - n_honest
    ways = 0
    for idx_case in range(omega.shape[0]):
        # new model: count real wins from honest participants. Then add to the dishonest ones.
        # assume that the first n_honest participants are honest
        n_real_wins_of_honest_people = numpy.sum(omega[idx_case,0:n_honest])
        n_fake_claims = n_dishonest  # all dishonest always claim the prize no matter if they win
        case_claimed_wins = n_real_wins_of_honest_people + n_fake_claims
        if case_claimed_wins == n_claims:
            ways += 1
    print(f"Q2: {n_honest=}, {n_claims=} -> {ways} ways -> which is likehood of {ways/omega.shape[0]:.4f} likelihood")
    return ways


def question_3():
    """
    Q3: What number of honest participants maximizes the number of ways?
    """
    print("\nQ3: Testing all possibilities...")
    max_ways = 0
    best_n_honest = 0

    # TODO: Loop through all possible values of n_honest and find which maximizes ways

    for n_honest in range(TOTAL_PARTICIPANTS + 1):
        # TODO: Calculate ways for this n_honest
        # TODO: Track the maximum
        pass

    print(f"\nMaximum ways: {max_ways} at n_honest = {best_n_honest}")
    return best_n_honest, max_ways


if __name__ == "__main__":
    print("=" * 60)
    print("Random Allocation Game - Garden of Forking Data")
    print("=" * 60)
    print(f"Setup: {TOTAL_PARTICIPANTS} participants, {PRIZE_CLAIMS} prize claims\n")
    print(f'===' * 60)
    omega = create_omega(TOTAL_PARTICIPANTS)

    question_1(omega)
    print(f'===' * 60)
    for n_honest in range(10+1):
        question_2(n_honest=n_honest)

    print(f'===' * 60)
    question_3()
