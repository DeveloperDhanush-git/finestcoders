from collections import deque

def cleanable_cells(matrix):
    rows, cols = len(matrix), len(matrix[0])
    start = None
    
   
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 2:
                start = (r, c)
                break
        if start:
            break
    
    if not start:
        return 0
    
    visited = [[False]*cols for _ in range(rows)]
    q = deque([start])
    visited[start[0]][start[1]] = True
    cleaned_count = 1 
    
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    while q:
        r, c = q.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
   
            if 0 <= nr < rows and 0 <= nc < cols:
               
                if not visited[nr][nc] and matrix[nr][nc] == 0:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    cleaned_count += 1
    
    return cleaned_count




rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
print("Enter matrix row by row (values 0, 1, or 2):")
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)


print("Reachable cells to clean:", cleanable_cells(matrix))