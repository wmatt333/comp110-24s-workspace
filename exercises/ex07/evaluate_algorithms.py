__author__ = "730544766"


import matplotlib.pyplot as plt
from exercises.ex07.runtime_analysis_functions import evaluate_runtime, evaluate_memory_usage
START_SIZE: int = 0
END_SIZE: int = 1000


usage = evaluate_memory_usage("insertion_sort", START_SIZE, END_SIZE)
plt.plot(usage)
plt.title("Memory Usage Analysis of Insertion Sort - 730544766")
plt.show()