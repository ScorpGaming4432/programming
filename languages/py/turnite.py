bsize = 100
board = [[0]*bsize]*bsize
directions = {0:{'x': 0, 'y':1}, 1:{'x': 1, 'y':0}, 2:{'x': 0, 'y':-1}, 3:{'x': -1, 'y':0}}
ant = {'x': round(len(board[0])/2), 'y': round(len(board)/2), 'd': 3}
step = 0
while step < 400:
    #show the board
    '''for pod in board:
        print(pod)
    print(step)'''

    #turn
    if board[ant['y']][ant['x']]:
        if ant['d'] == 0: ant['d'] = 3 #if N turn to W
        else: ant['d'] -= 1 # turn counterclockwise
    else:
        if ant['d'] == 3: ant['d'] = 0 #if W turn to N
        else: ant['d'] += 1 # turn clockwise

    #flip
    board[ant['y']] = board[ant['y']][:ant['x']] + [int(not(board[ant['y']][ant['x']]))] + board[ant['y']][ant['x']+1:]

    #move
    ant['x'], ant['y'] = ant['x'] + directions[ant['d']]['x'], ant['y'] + directions[ant['d']]['y']
    step += 1
else:
    #show the board
    for pod in board:
        print(pod)
    print('end:', step)