import sys


def _read_matrix():
    N, M = [int(i) for i in input().split(" ")]
    weights = []
    for _ in range(N):
        row_input = [int(i) for i in sys.stdin.readline().strip("\r\n").split(" ")]
        weights.append(row_input)
    return weights, N, M

def main():
    weights, N, M = _read_matrix()

    if N == 1 and M == 1:
        print(weights[0][0])
        return

    costs = [[0] * M for i in range(N)]
    steps = [[""] * M for i in range(N)]
    for row in range(N):
        for col in range(M):
            if row == 0 and col == 0:
                costs[row][col] = weights[row][col]
                steps[row][col] = ""
            elif row == 0 and col > 0:
                costs[row][col] = costs[row][col - 1] + weights[row][col]
                steps[row][col] = "L"
            elif row > 0 and col == 0:
                costs[row][col] = costs[row - 1][col] + weights[row][col]
                steps[row][col] = "U"
            else:
                costs[row][col] = max(
                    costs[row - 1][col] + weights[row][col],
                    costs[row][col - 1] + weights[row][col],
                )
                if costs[row][col] == costs[row - 1][col] + weights[row][col]:
                    steps[row][col] = "U"
                else:
                    steps[row][col] = "L"
                
    print(costs[N - 1][M - 1])
    walk_path = ""
    while N > 0 and M > 0:
        if steps[N - 1][M - 1] == "U":
            N -= 1
            walk_path += "D "
        elif steps[N - 1][M - 1] == "L":
            M -= 1
            walk_path += "R "
        if steps[N - 1][M - 1] == "":
            break

    print(walk_path[::-1].lstrip(" "))

if __name__ == "__main__":
    main()

