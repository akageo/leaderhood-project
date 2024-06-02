def variance(numbers): 
    mean = sum(numbers) / len(numbers)
    variance = sum([(i-mean)**2 for i in numbers]) / len(numbers)
    return variance