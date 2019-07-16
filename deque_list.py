class Deque:
	def __init__(self):
		self.deque = []

	def addFront(self, item):
		self.deque.insert(0,item)

	def addTail(self, item):
		self.deque.append(item)

	def removeFront(self):
		if self.size() != 0:
			return self.deque.pop(0)
		else:
			return None

	def removeTail(self):
		if self.size() != 0:
			return self.deque.pop()
		else:
			return None 

	def size(self):
		return len(self.deque)

	def palindromeTest(self, string):
		for i in range(len(string)):
			self.addTail(string[i])
		while self.size() > 1:
			firstSymbol = self.removeFront()
			lastSymbol = self.removeTail()
			if firstSymbol != lastSymbol:
				return False
		return True
