def print_pattern(n):
    for i in range(1, n + 1):
        val = 1
        for k in range(1, i):
            val += (n - k)
        row = []
        for j in range(i):
            row.append(str(val))
            val -= (n - j)
        print(" ".join(row))

if __name__=="__main__":
    n=6
    print_pattern(n)