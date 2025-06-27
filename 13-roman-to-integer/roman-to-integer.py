class Solution:
    def romanToInt(self, s: str) -> int:
        roman = list(s)
   
        number = list(map(lambda x: 1 if x == "I" else x, roman))
        number = list(map(lambda x: 5 if x == "V" else x, number))
        number = list(map(lambda x: 10 if x == "X" else x, number))
        number = list(map(lambda x: 50 if x == "L" else x, number))
        number = list(map(lambda x: 100 if x == "C" else x, number))
        number = list(map(lambda x: 500 if x == "D" else x, number))
        number = list(map(lambda x: 1000 if x == "M" else x, number))

        total = 0
        i = 0
        while i < len(number):
            if i + 1 < len(number) and number[i] < number[i + 1]:
                total += number[i + 1] - number[i]
                i += 2
            else:
                total += number[i]
                i += 1

        return total
