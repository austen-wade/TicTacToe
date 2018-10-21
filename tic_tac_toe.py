import time
from random import randint

class Game():

	def __init__(self, size):
		self.size = size
		self.spaces = size * size
		self.board_arr = []
		i = 0
		while i < self.spaces:
			self.board_arr.append(" ")
			i += 1
		self.status = "Continue"

	def start(self):
		if self.goes_first() == True:
			while not self.status != "Continue":
				if self.player_go():
					break
				if self.computer_go():
					break
		else:
			while not self.status != "Continue":
				if self.computer_go():
					break
				if self.player_go():
					break

	def goes_first(self):

		print("Let's flip a coin to see who goes first.")

		time.sleep(1)
		print("1...")
		time.sleep(0.5)
		print("2...")
		time.sleep(0.5)
		print("3...")
		time.sleep(0.5)

		rnd = randint(1, 2)
		if rnd == 2:
			print("Heads!")
			time.sleep(0.5)
			print("Player goes first.")
			time.sleep(0.5)
			return True
		else:
			print("Tails!")
			time.sleep(0.5)
			print("Computer goes first.")
			time.sleep(0.5)
			return False

	def player_go(self):
		play_switch = True
		while play_switch == True:
			try:
				user_move = int(input("Select which square you would like to set [0-9]:\n"))
				if self.board_arr[user_move] != "x" and self.board_arr[user_move] != "o":
					self.board_arr[user_move] = "x"
					self.display()
					play_switch = False
					if self.check_win('x'):
						if self.winner == True:
							print("Player Wins")
						else:
							print("Computer Wins")
						return True
					else:
						self.full()
				else:
					print("That square is taken.")
					play_switch = True
			except:
				print("Pick a valid number.")

	def computer_go(self):
		print("The computer is thinking...")
		time.sleep(1.25)
		com_switch = True
		while com_switch == True:
				computer_o = randint(0,self.spaces-1)
				if self.board_arr[computer_o] != "x" and self.board_arr[computer_o] != "o":
					self.board_arr[computer_o] = "o"
					self.display()
					com_switch = False
					if self.check_win('o'):
						if self.winner == False:
							print("Player Wins")
						else:
							print("Computer Wins")
						return True
					else:
						self.full()
				else:
					com_switch = True

	def display(self):
		print("\n")
		i = 1
		while i != self.size+1:
			print(self.board_arr[(self.size*i)-self.size:self.size*i])
			i += 1
		print("\n")

	def check_win(self, var):
		d_check = self.board_arr[:self.spaces+1:self.size + 1]
		ad_check = self.board_arr[self.size - 1:(self.size * 2)+1:self.size - 1]

		# diagonal
		if set(d_check) == {'{}'.format(var)}:
			self.winner = True
			return True
		# anti-diagonal
		if set(ad_check) == {'{}'.format(var)}:
			self.winner = True
			return True

		count = 0
		while count < self.size:
			v_check = set(self.board_arr[count::self.size])
			h_check = set(self.board_arr[count*self.size:count*self.size+self.size:1])
			# vertical
			if v_check == {'{}'.format(var)}:
				self.winner = True
				return True

			# horizontal doesn't catch a middle win
			if h_check == {'{}'.format(var)}:
				self.winner = True
				return True

			count += 1

	def full(self):
		if set(self.board_arr) == {"x", "o"} or set(self.board_arr) == {"o", "x"}:
			print("The board is full. \nTIE")
			exit()

game = Game(3)
game.start()