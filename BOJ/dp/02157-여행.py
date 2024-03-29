import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
airline = [[0] * (n + 1) for _ in range(n + 1)]
dp = [[0] * (m + 1) for _ in range(n + 1)]
for _ in range(k):
    a, b, c = map(int, input().split())
    airline[a][b] = max(airline[a][b], c)
for i in range(2, n + 1):
    dp[i][2] = airline[1][i]
for i in range(2, n + 1):
    for j in range(3, m + 1):
        for l in range(1, i):
            if airline[l][i] and dp[l][j - 1]:
                dp[i][j] = max(dp[l][j - 1] + airline[l][i], dp[i][j])
print(max(dp[n]))
