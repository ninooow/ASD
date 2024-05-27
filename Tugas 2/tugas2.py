def DIJKSTRA(graph, N, S):
    distances = {i:[float('inf'), 0] for i in range(1,N+1)}
    visited = {i:False for i in range(1,N+1)}
    distances[S] = [0,S]
    for i in range(N):
        min_distance = float('inf')
        min_vertex = -1
        for vertex in distances :
            if visited[vertex] == False and distances[vertex][0]< min_distance:
                min_distance = distances[vertex][0]
                min_vertex = vertex
        visited[min_vertex]=True
        for neighbors, weight in graph[min_vertex]:
            new_distance = min_distance + weight
            if new_distance < distances[neighbors][0]:
                distances[neighbors] = [new_distance,min_vertex]
    return distances
def DFS(graph, start, target_distance):
    stack = [(start, 0, [start], set([start]))]    
    while stack:
        current_node, current_distance, path, visited = stack.pop()        
        if current_distance == target_distance:
            return path        
        for neighbor, weight in graph[current_node]:
            if neighbor not in visited:
                new_distance = current_distance + weight
                if new_distance <= target_distance:
                    new_path = path + [neighbor]
                    new_visited = visited.copy()
                    new_visited.add(neighbor)
                    stack.append((neighbor, new_distance, new_path, new_visited))    
    return None
def BFS (graph,N, S):
    distances = {i:[-1,0] for i in range(1,N+1)}
    visited = {i:False for i in range(1,N+1)}
    distances[S] = [0,S]
    visited[S]=True
    queue = [S]
    while len(queue)!=0:
        current = queue.pop(0)
        for i in data:
            if current == i[0] and visited[i[1]] == False:
                queue.append(i[1])
                distances[i[1]] = [distances[current][0]+1, current]
                visited[i[1]] = True
            elif current == i[1] and visited[i[0]] == False:
                queue.append(i[0])
                distances[i[0]] = [distances[current][0]+1, current]
                visited[i[0]] = True
    return distances


data = []
with open('data.txt', 'r') as file:
    for baris in file:
        data.append(list(map(int,baris.split(" "))))
N, M, S = data[0][0], data[0][1], data[len(data)-1][0]
data.pop(0)
data.pop()
graph = {i : [] for i in range(1,N+1)}
for x, y, z in data :
    graph[x].append((y,z))
    graph[y].append((x,z))


# NO SATU
distances_noSatu = DIJKSTRA(graph, N, S)
longest_noSatu = max(distances_noSatu, key=lambda k: distances_noSatu[k][0])
print(f"Vertex yang memiliki jarak terpendek tertinggi dari {S} yaitu  {longest_noSatu}, dengan jarak { distances_noSatu[longest_noSatu][0]}.")
print()

# NO DUA
target_distance = 2024
path_noDua = DFS(graph, S, target_distance)
path_noDua_str = [str(item) for item in path_noDua]
if path_noDua is not None:
    print(f"Terdapat vertex yang berjarak {target_distance} dari {S}, yaitu {path_noDua[-1]} dengan path: {' -> '.join(path_noDua_str)}")
else:
    print(f"Tidak ada vertex yang berjarak {target_distance} dari {S}.")
print()

# NO TIGA
distances_noTiga = BFS(graph, N, S)
long = max(distances_noTiga.values(), key=lambda item: item[0])
long_vertex = [value for value in distances_noTiga if distances_noTiga[value][0]==long[0]]
print(f"Jarak terjauh dari vertex {S} yaitu {long[0]} sebanyak {len(long_vertex)}, sebagai berikut.")
print(long_vertex)