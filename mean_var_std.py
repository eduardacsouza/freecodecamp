import numpy as np


def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(numbers).reshape(3, 3)

    calculations = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum
    }

    results = {}

    for key, func in calculations.items():
        results[key] = [
            func(matrix, axis=0).tolist(),
            func(matrix, axis=1).tolist(),
            func(matrix).item()
        ]

    return results
