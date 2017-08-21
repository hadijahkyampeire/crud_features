class User(object):
	"""
		The user class implements the functionality of a user on the shoppinglist application
	"""
	def __init__(self,first_name,last_name,email,password):
		"""The constructor initialises class variables"""
		self.name=first_name+" "+last_name
		self.email=email
		self.password=password
		self.login_status=False

	def login(self,email,password):
		"""The login method checks if the user email and password match the ones provided by the app"""
		if email==self.email and password==self.password:
			self.login_status=True
			return True
		else:
			print(self.email)
			print(self.password)
			return False