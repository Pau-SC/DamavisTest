from snake import *
import unittest
''' Testing Unit '''
class myTests(unittest.TestCase):
	def test1(self):
		'''
		board: [4, 3]
		snake: [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
		depth: 3

		result = 7
		'''
		self.assertEqual(number_of_available_different_paths([4,3], [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]], 3), 7)

	def test2(self):
		'''
		board: [2, 3]
		snake: [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
		depth: 10

		result = 1
		'''
		self.assertEqual(number_of_available_different_paths([2,3], [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]], 10), 1)	

	def test3(self):
		'''
		board: [10, 10]
		snake: [[5,5], [5,4], [4,4], [4,5]]
		depth: 4

		result = 81
		'''
		self.assertEqual(number_of_available_different_paths([10,10], [[5,5], [5,4], [4,4], [4,5]], 4), 81)	



if __name__ == "__main__":
	unittest.main()
