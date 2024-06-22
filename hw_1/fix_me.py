def calculate_average(nums):
    total = sum(nums)
    count = len(nums)
    average = total / count
    return average


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)

# в лекции говорилось только про ruff, формататировал с его помощью - All checks passed!
# flake8 или pylint не использовал.
# при этом pycharm подчеркивает аргумент nums при определении функции, и, например,
# у функции отсутствуют аннотации и докстринга.
# для сдачи такого форматирования достаточно?
