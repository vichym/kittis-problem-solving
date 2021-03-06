class Solution:
    def __init__(self):
        self.lowest = 0
        self.highest = 10

    @staticmethod
    def read_input():
        guess = int(input())
        if guess == 0:
            return [guess, ""]
        else:
            result = input()
            return [guess, result]

    def calculate(self):
        for _ in range(2500):
            guess, result = self.read_input()
            if guess == 0 :
                break
            if result == "too high" and guess < self.highest:
                self.highest = guess - 1
            elif result == "too low" and guess > self.lowest:
                self.lowest = guess + 1
            else:
                if self.lowest <= guess <= self.highest:
                    print("Stan may be honest")
                else:
                    print("Stan is dishonest")

                self.reset()

    def reset(self):
        self.lowest = 0
        self.highest = 10

if __name__ == '__main__':
    solution = Solution()
    solution.calculate()