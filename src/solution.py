class Solution():
    def __init__(self, solver_function):
        self.f = solver_function

    def solve(self):
        with open("input.txt", "r") as file:
            content = file.read()
        result = self.f(content)
        print(result)
