class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop(0)
        salary.pop(-1)
        return sum(salary)/len(salary)


class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = float('inf')
        max_salary = float('-inf')

        total = 0

        for num in salary:
            if num < min_salary:
                min_salary = num

            if num > max_salary:
                max_salary = num

            total += num

        total -= (min_salary + max_salary)

        return total / (len(salary) - 2)