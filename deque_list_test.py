import unittest

class TestDeque(unittest.TestCase):
	def setUp(self):
		self.deque = Deque()

	def testSizeEmpty(self):
		assert self.deque.size() == 0

	def testAddFrontEmpty(self):
		self.deque.addFront(1)
		assert self.deque.size() == 1
		assert self.deque.deque[0] == 1

	def testAddFrontFull(self):
		self.deque.addFront(1)
		self.deque.addFront(0)
		assert self.deque.size() == 2
		assert self.deque.deque[0] == 0

	def testAddTailEmpty(self):
		self.deque.addTail(1)
		assert self.deque.size() == 1
		assert self.deque.deque[0] == 1

	def testAddTailFull(self):
		self.deque.addTail(1)
		self.deque.addTail(0)
		assert self.deque.size() == 2
		assert self.deque.deque[1] == 0

	def testRemoveFrontFull(self):
		self.deque.addFront(1)
		self.deque.addFront(0)
		self.deque.removeFront()
		assert self.deque.size() == 1
		assert self.deque.deque[0] == 1		

	def testRemoveFrontEmpty(self):
		x = self.deque.removeFront()
		assert x == None

	def testRemoveTailFull(self):
		self.deque.addFront(1)
		self.deque.addFront(0)
		self.deque.removeTail()
		assert self.deque.size() == 1
		assert self.deque.deque[0] == 0	

	def testRemoveTailEmpty(self):
		x = self.deque.removeTail()
		assert x == None

	def testPalindromeTest(self):
		x = self.deque.palindromeTest("AKA")
		assert x == True

if __name__ == '__main__':
	unittest.main()
