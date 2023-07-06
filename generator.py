import numpy as np

def generate():
    unsorted_array = np.random.randint(1,100,100)
    return unsorted_array

if __name__ == "__main__":
    unsorted_array = generate()
    print(unsorted_array)