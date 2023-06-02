import random
import curses

s = curses.initscr()
curses.curs_set(False)
curses.noecho()
height , width = s.getmaxyx()
s.keypad(True)
s.timeout(150)

snake = [[height//2, width//2],
         [height//2, width//2-1],
         [height//2, width//2-2],
         [height//2, width//2-3],
         [height//2, width//2-4]]
n_snake = 5
for i in range(n_snake):
    s.addstr(snake[i][0], snake[i][1], '*')
s.refresh()
direction = 'right' # left, up, down
cake = [0,1]
ok = False
while not ok:
    cake = [random.randrange(1,height-1), random.randrange(1, width-1)]
    ok = True
    for i in range(n_snake):
        if cake[0] == snake[i][0] and cake[1] == snake[i][1]:
            ok = False
s.addstr(cake[0], cake[1], 'c')
point = 0
while True:
    ch = s.getch()
    if ch == curses.KEY_DOWN and direction != 'up':
        direction = 'down'
    if ch == curses.KEY_UP and direction != 'down':
        direction = 'up'
    if ch == curses.KEY_LEFT and direction != 'right':
        direction = 'left'
    if ch == curses.KEY_RIGHT and direction != 'left':
        direction = 'right'
    if ch == curses.KEY_F2:
        break;

    old_snake = [snake[n_snake-1][0], snake[n_snake-1][1]]
    for i in range(n_snake-1,0,-1):
        snake[i][0] = snake[i-1][0]
        snake[i][1] = snake[i-1][1]
    if direction == 'right':
        snake[0][1] += 1
    if direction == 'left':
        snake[0][1] -= 1
    if direction == 'up':
        snake[0][0] -= 1
    if direction == 'down':
        snake[0][0] += 1
    s.addstr(snake[0][0], snake[0][1], '*')
    ok = True
    for i in range(1,n_snake):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            ok = False
    if not ok:
        break;
    if snake[0][0] == cake[0] and snake[0][1] == cake[1] :
        point += 1
        ok = False
        while not ok:
            cake = [random.randrange(1, height-1), random.randrange(1, width-1)]
            ok = True
            for i in range(n_snake):
                if cake[0] == snake[i][0] and cake[1] == snake[i][1]:
                    ok = False
        s.addstr(cake[0], cake[1], 'c')
        if point % 2 == 0:
            n_snake += 1
            snake += [old_snake]
        else:
            s.addstr(old_snake[0], old_snake[1], ' ')
    else:
        s.addstr(old_snake[0], old_snake[1], ' ')

    if not (0 < snake[0][0] < height-1 and 0 < snake[0][1] < width -1):
        break;

curses.endwin()
print('You have {} points'.format(point))
