k = 4
n = 9875

def superDigit(n, k):
    def digit_sum(v):
        while v > 9:
            hold = 0
            for i in str(v):
                hold += int(i)
            v = hold
        return v
    x = digit_sum(int(str(n)*k))
    return x

print(superDigit(n, k))