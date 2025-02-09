import random

def ten_flips():
    heads_count = sum(random.choice([0, 1]) for _ in range(10))  
    return heads_count == 7

def prob_seven_out_of_ten(n):
    success_count = sum(ten_flips() for _ in range(n))
    return success_count / n  