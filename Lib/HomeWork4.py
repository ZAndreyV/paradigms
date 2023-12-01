import math

def calculate_mean(array):
    return sum(array) / len(array)

def calculate_covariance(x, y):
    x_mean = calculate_mean(x)
    y_mean = calculate_mean(y)
    return (sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y))) / len(x)


def calculate_standard_deviation(array):
    return math.sqrt(sum((xi - calculate_mean(array)) ** 2 for xi in array) / len(array))

def calculate_correlation(x, y):
    covariance = calculate_covariance(x, y)
    x_std = calculate_standard_deviation(x)
    y_std = calculate_standard_deviation(y)
    return covariance / (x_std * y_std)


# Пример использования
# Два массива данных
x_values = [1, 2, 3, 4, 5, 3, 4]
y_values = [6, 7, 8, 9, 10]

# Расчет корреляции Пирсона
correlation = calculate_correlation(x_values, y_values)

# Вывод результата
print("Корреляция Пирсона:", correlation)
