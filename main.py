# ↓ importing the file with the two search
from search import *
# ↓ importing the file with generator of values
from generator import *
# ↓ import the lib for get time
import time

seq = []  # seq = sequence = the vector

generator_vector(seq)  # generating the values for "seq"

start_time = time.time()  # started counting runtime
sequential_search(seq, 50)  # calling, searching  with sequential search
end_time = time.time()  # stopped counting runtime
timer = end_time - start_time  # subtraction to know the time
print(f'Time to execute in sequential search: {timer}')

start_time = time.time()  # started counting runtime
binary_search(seq, 50)  # calling, searching  with binary search
end_time = time.time()  # stopped counting runtime

timer = end_time - start_time  # subtraction to know the time
print(f'Time to execute in binary search: {timer}')
