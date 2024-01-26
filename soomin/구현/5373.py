# 큐빙: https://acmicpc.net/problem/5373
test_n = int(input())

def run(cube, stdface, faces, clockwise):
    face_rotation = [6, 3, 0, 7, 4, 1, 8, 5, 2]
    if not clockwise:
        faces.reverse()
        face_rotation.reverse()
        
    # rotate standard face
    temp = cube[stdface][0:9]
    for i, temp_idx in enumerate(face_rotation):
        cube[stdface][i] = temp[temp_idx]
        
    # rotate side faces
    temp = []
    for face, indexes in faces:
        temp.append([cube[face][idx] for idx in indexes])
        
    for i, (face, indexes) in enumerate(faces):
        for j, idx in enumerate(indexes):
            cube[face[0]][idx] = temp[i-1][j]
    
# test cases
for _ in range(test_n):
    # cube
    cube = {'U': ['w'] * 9, 'D': ['y'] * 9, 'F': ['r'] * 9, 'B': ['o'] * 9, 'L': ['g'] * 9, 'R': ['b'] * 9}
    # get inputs
    n = int(input())
    trials = input().split()
    for trial in trials:
        # execute
        if trial[0] == 'U':
            faces = [('L', [0, 1, 2]), ('B', [0, 1, 2]), ('R', [0, 1, 2]), ('F', [0, 1, 2])]
        elif trial[0] == 'D':
            faces = [('L', [6, 7, 8]), ('F', [6, 7, 8]), ('R', [6, 7, 8]), ('B', [6, 7, 8])]
        elif trial[0] == 'F':
            faces = [('L', [8, 5, 2]), ('U', [6, 7, 8]), ('R', [0, 3, 6]), ('D', [2, 1, 0])]
        elif trial[0] == 'B':
            faces = [('L', [0, 3, 6]), ('D', [6, 7, 8]), ('R', [8, 5, 2]), ('U', [2, 1, 0])]
        elif trial[0] == 'L':
            faces = [('B', [8, 5, 2]), ('U', [0, 3, 6]), ('F', [0, 3, 6]), ('D', [0, 3, 6])]
        elif trial[0] == 'R':
            faces = [('F', [8, 5, 2]), ('U', [8, 5, 2]), ('B', [0, 3, 6]), ('D', [8, 5, 2])]
        
        run(cube, trial[0], faces, (trial[1] == '+'))
        
    # print
    for i in range(3):
        print(''.join(cube['U'][i*3:i*3+3]))