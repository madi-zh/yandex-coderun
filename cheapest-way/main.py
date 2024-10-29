import sys


def main():
    N, M = [int(i) for i in input().split(" ")]
    weights = []
    for _ in range(N):
        row_input = [int(i) for i in sys.stdin.readline().strip("\r\n").split(" ")]
        weights.append(row_input)
    if N == 1 and M == 1:
        print(weights[0][0])
        return

    costs = [[0] * M for i in range(N)]
    for row in range(N):
        for col in range(M):
            if row == 0 and col == 0:
                costs[row][col] = weights[row][col]
            elif row == 0 and col > 0:
                costs[row][col] = costs[row][col - 1] + weights[row][col]
            elif row > 0 and col == 0:
                costs[row][col] = costs[row - 1][col] + weights[row][col]
            else:
                costs[row][col] = min(
                    costs[row - 1][col] + weights[row][col],
                    costs[row][col - 1] + weights[row][col],
                )
    print(costs[N - 1][M - 1])


if __name__ == "__main__":
    main()
