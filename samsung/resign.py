if __name__ == "__main__":
    n = int(input())
    t, p, f, dp_f, dp_s = [0], [0], [0], [0], [0]
    dp_f, dp_s = [0] * (n + 1), [0] * (n + 1)

    for i in range(1, n + 1):
        line = input()
        t.append(int(line.split(" ")[0]))
        p.append(int(line.split(" ")[1]))
        f.append(i + t[i] - 1)

    for i in range(1, n + 1):
        if f[i] > n:
            continue
        for j in range(i):
            if dp_f[j] < i and dp_s[j] + p[i] > dp_s[i]:
                dp_f[i] = f[i]
                dp_s[i] = dp_s[j] + p[i]
        
    print(max(dp_s))