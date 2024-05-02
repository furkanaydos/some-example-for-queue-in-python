from collections import deque

def bfs(start, finish, maze):
    visited = [[False]*len(maze[0]) for _ in range(len(maze))]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([start])

    while queue:
        x, y = queue.popleft()

        if (x, y) == finish:
            return True

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and not visited[nx][ny]:
                if maze[nx][ny] in [' ', 'F']:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

    return False

def read_maze():
    start = tuple(map(int, input("Enter starting location as two space-separated integers (x,y): ").split()))
    finish = tuple(map(int, input("Enter finish location as two space-separated integers (x,y): ").split()))
    # Adjust for zero indexing
    start, finish = (start[0] - 1, start[1] - 1), (finish[0] - 1, finish[1] - 1)

    print("Enter the maze, row by row. Click enter twice to exit:")
    maze = []
    while True:
        row = input()
        if row:
            maze.append(list(row))
        else:
            break

    return start, finish, maze

def main():
    start, finish, maze = read_maze()
    if bfs(start, finish, maze):
        print("It is possible to reach from S to F.")
    else:
        print("It is not possible to reach from S to F.")

if __name__ == "__main__":
    main()