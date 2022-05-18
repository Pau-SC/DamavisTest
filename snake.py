from collections import deque
import sys

'''
Removes the tail, extends the head in the given direction, returning an updated version.

Parameter snake_deque: The deque representing the snake
Parameter direction: Can be either 'left', 'down', 'right' or 'up', deciding the movement.
'''
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

'''
Recursive funtion that looks through all the possible movements of the snake given a board and the deque object
made with the snake specified on the main function.
	Parameter board: Array containing 2 values, being the maximum x and y of the canvas where the snake exists.
					 Precondition: from 1x1 to 10x10
	Parameter snake_deque: deque() object version of snake, so it has a direction.
	Parameter depth_remaining: amount of movements left until the path is accepted.

'''
def number_of_available_different_paths_recursive(board, snake_deque, depth_remaining):
	result = 0
	if depth_remaining <= 0: #If depth is done, we found a path, so we add 1
		return 1
	else:
		snake_deque_copy = snake_deque.copy()
		snake_deque_checker = snake_deque.copy()
		snake_deque_checker.pop() #Snake can move where tail was, so we won't consider it an obstacle
		head_position = snake_deque_copy.popleft() #Find the snake's head with a copy
		snake_deque_copy.clear() #Will be repurposed for relative position within recursivity
		x, y = head_position[0], head_position[1]
		'''
		Check board size, then check if snake already exists, then move and call recursive.
		'''
		if x > 0: #Left
			if snake_deque_checker.count((x-1,y)) == 0:
				snake_deque_copy = move_snake(snake_deque, 'left')
				result += number_of_available_different_paths_recursive(board, snake_deque_copy, depth_remaining-1)
		if y > 0: #Down
			if snake_deque_checker.count((x,y-1)) == 0:
				snake_deque_copy = move_snake(snake_deque, 'down')
				result += number_of_available_different_paths_recursive(board, snake_deque_copy, depth_remaining-1)
		if board[0]-1 > x: #Right
			if snake_deque_checker.count((x+1,y)) == 0:
				snake_deque_copy = move_snake(snake_deque, 'right')
				result += number_of_available_different_paths_recursive(board, snake_deque_copy, depth_remaining-1)
		if board[1]-1 > y: #Up
			if snake_deque_checker.count((x,y+1)) == 0:
				snake_deque_copy = move_snake(snake_deque, 'up')
				result += number_of_available_different_paths_recursive(board, snake_deque_copy, depth_remaining-1)
		return result


'''
The main function, initializes a deque with the snake for usage and starts the recursive function.

Returns the number of available movements with the given depth, board and snake positions.

	Parameter board: Array containing 2 values, being the maximum x and y of the canvas where the snake exists.
					 Precondition: from 1x1 to 10x10
	Parameter snake: Array contains all the snake occupied positions in order.
					 Precondition: At least 3 elements, and a maximum of 7.
					 Precondition: Within board domain.
					 Precondition: Correct coordinates.
	Parameter depth: The amount of movements needed to be considered valid.
					 Precondition: Will be at least 1, and a maximum of 20.
'''
def number_of_available_different_paths(board, snake, depth):
	snake_deque = deque()
	for snake_positions in snake: 
		snake_deque.append((snake_positions[0], snake_positions[1])) #Create a deque object with the snake in order
	result = number_of_available_different_paths_recursive(board, snake_deque, depth)
	return result


if __name__ == "__main__":
	print('Used as module!')
