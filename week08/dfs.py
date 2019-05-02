def dfs_iterative(graph, start):
    stack, visited = [start], []

    while stack:
        vertex = stack.pop()
        if vertex in visited:
            continue
        visited.append(vertex)
        for neighbour in graph[vertex]:
            stack.append(neighbour)

    return visited

if __name__=='__main__':
    data = {1: [2, 3], 2: [4, 5],
            3: [5], 4: [6], 5: [6,1],
            6: [7], 7: []}
    print(dfs_iterative(data,2))