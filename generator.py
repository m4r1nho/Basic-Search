import random  # importing


# a function for create  random numbers for the vector
def generator_vector(vector):
    for i in range(1000000):  # vector with 1 Million values
        value = random.randint(-100, 10000)  # values between -100 and 10K
        vector.append(value)
