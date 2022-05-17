from collections import deque
import sys

def move_snake(snake_deque, direction):
	snake_deque_copy = snake_deque.copy()
	head_position = snake_deque_copy.popleft() #Find the snake's head
	x, y = head_position[0], head_position[1] #Movement origin, changes to destination
	if direction == 'left':
		x -= 1
	if direction == 'down':
		y -= 1
	if direction == 'right':
		x += 1
	if direction == 'up':		
		y += 1
	snake_deque_copy.clear()
	snake_deque_copy = snake_deque.copy()
	snake_tail = snake_deque_copy.pop()
	snake_deque_copy.appendleft((x,y))
	return snake_deque_copy


def number_of_available_different_paths_recursive(board, snake_deque, depth_remaining):
	result = 0
	if depth_remaining <= 0: #If depth is done, add 1
		return 1
	else:
		snake_deque_copy = snake_deque.copy()
		snake_deque_checker = snake_deque.copy()
		head_position = snake_deque_copy.popleft() #Find the snake's head
		snake_deque_copy.clear()
		x, y = head_position[0], head_position[1]
		if x > 0: #Left
			if snake_deque_checker.count((x-1,y)) == 0:
				snake_deque_copy = move_snake(snake_deque, 'left')
				print('L')
				result += number_of_available_different_paths_recursive(board, snake_deque_copy, depth_remaining-1)
		if y > 0: #Down
			if snake_deque_checker.count((x,y-1)) == 0:
				snake_deque_copy = move_snake(snake_deque, 'down')
				print('D')
				result += number_of_available_different_paths_recursive(board, snake_deque_copy, depth_remaining-1)
		if board[0]-1 > x: #Right
			if snake_deque_checker.count((x+1,y)) == 0:
				snake_deque_copy = move_snake(snake_deque, 'right')
				print('R')
				result += number_of_available_different_paths_recursive(board, snake_deque_copy, depth_remaining-1)
		if board[1]-1 > y: #Up
			if snake_deque_checker.count((x,y+1)) == 0:
				snake_deque_copy = move_snake(snake_deque, 'up')
				print('U')
				result += number_of_available_different_paths_recursive(board, snake_deque_copy, depth_remaining-1)
		return result



def number_of_available_different_paths(board, snake, depth):
	snake_deque = deque()
	for snake_positions in snake: 
		i, j = snake_positions[0], snake_positions[1]
		snake_deque.append((snake_positions[0], snake_positions[1])) #Create a deque object with the snake in order
	result = number_of_available_different_paths_recursive(board, snake_deque, depth)
	return result


if __name__ == "__main__":
	boardInput = sys.argv[1]
	snakeInput = sys.argv[2]
	depthInput = sys.argv[3]
	result = number_of_available_different_paths(boardInput, snakeInput, depthInput)
	print(result)
