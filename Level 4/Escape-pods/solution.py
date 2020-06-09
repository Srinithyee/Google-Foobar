def bfs(matrix, source, destination):
    visited = [-1 for i in range(len(matrix))]
    visited[source] = source
    queue = [source]
    while len(queue) > 0:
        first = queue.pop(0)
        for i in range(len(matrix)):
            if (matrix[first][i][1] - matrix[first][i][0]) != 0 and visited[i] == -1:
                if i == destination:
                    visited[destination] = first
                    path = [destination]
                    temp = destination
                    while temp != source:
                        temp = visited[temp]
                        path.append(temp)
                    path.reverse()
  
                    temp = 1
                    maximum_val = float("inf")
                    cur = source
                    while temp != len(path):
                        entry = matrix[cur][path[temp]]
                        diff = abs(entry[1]) - entry[0]
                        maximum_val = min(maximum_val, diff)
                        cur = path[temp]
                        temp += 1
                    temp = 1
                    cur = source
                    while temp != len(path):
                        entry = matrix[cur][path[temp]]
                        if entry[1] < 0: 
                            entry[1] += maximum_val
                        else:
                            entry[0] += maximum_val
                        entry = matrix[path[temp]][cur]
                        if entry[1] <= 0: 
                            entry[1] -= maximum_val
                        else:
                            entry[0] += maximum_val
                        cur = path[temp]
                        temp += 1
                    return True
                else:
                    visited[i] = first
                    queue.append(i)
    return False


def solution(entrances, exits, path):
    maximum = sum(list(map(sum, path)))
    temp = []
    for i in range(len(path)):
        temp.append([])
        for j in range(len(path[i])):
            temp[i].append([0, path[i][j]])
        temp[i].append([0, 0])

        if i in exits:
            temp[i].append([0, maximum])
        else:
            temp[i].append([0, 0])
    temp.append([])
    temp.append([])
    for i in range(len(path[0]) + 2):
        if i in entrances:
            temp[-2].append([0, maximum])
        else:
            temp[-2].append([0, 0])
        temp[-1].append([0, 0])
    while bfs(temp, len(temp)-2, len(temp)-1):
        pass
    bunnies = 0
    for i in range(len(temp)):
        bunnies += temp[-2][i][0]
    return bunnies