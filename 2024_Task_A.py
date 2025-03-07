import heapq


def min_time_to_finish(N, track):
    INF = float("inf")
    min_time = [[INF] * (N + 1) for _ in range(N + 1)]
    pq = [(0, 1, 0)]
    min_time[1][0] = 0

    while pq:
        time, cell, boost = heapq.heappop(pq)

        if cell == N:
            return time

        if min_time[cell][boost] < time:
            continue

        for next_cell in [cell - 1, cell + 1]:
            if 1 <= next_cell <= N:
                move_time = 1 if boost > 0 else 2
                new_boost = max(0, boost - 1)
                if time + move_time < min_time[next_cell][new_boost]:
                    min_time[next_cell][new_boost] = time + move_time
                    heapq.heappush(pq, (time + move_time, next_cell, new_boost))

        if track[cell][0] == "J":
            dest = track[cell][1]
            if time + 1 < min_time[dest][0]:
                min_time[dest][0] = time + 1
                heapq.heappush(pq, (time + 1, dest, 0))

        if track[cell][0] == "S":
            boost_time = track[cell][1]
            if time < min_time[cell][boost_time]:
                min_time[cell][boost_time] = time
                heapq.heappush(pq, (time, cell, boost_time))

    return -1


N = int(input().strip())
track = {}
for i in range(1, N + 1):
    data = input().split()
    if data[0] == "S":
        track[i] = ("S", int(data[1]))
    elif data[0] == "J":
        track[i] = ("J", int(data[1]))
    else:
        track[i] = ("X", None)

print(min_time_to_finish(N, track))
