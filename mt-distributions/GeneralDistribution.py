import matplotlib.pyplot as plt

class Distribution:
	
	def __init__(self, mu=0, sigma=1):
	
		""" Generic distribution class for calculating and 
		visualizing a probability distribution.
	
		Attributes:
			mean (float) representing the mean value of the distribution
			stdev (float) representing the standard deviation of the distribution
			data_list (list of floats) a list of floats extracted from the data file
			"""
		
		self.mean = mu
		self.stdev = sigma
		self.data = []

	def pdf(self):
		pass

	def read_data_file(self, file_name):
	
		"""Function to read in data from a txt file. The txt file should have
		one number (float) per line. The numbers are stored in the data attribute.
				
		Args:
			file_name (string): name of a file to read from
		
		Returns:
			None
		
		"""
			
		with open(file_name) as file:
			data_list = []
			line = file.readline()
			while line:
				data_list.append(int(line))
				line = file.readline()
		file.close()
	
		self.data = data_list

	def plot_pdf(self, min_x, max_x, title):

		"""Function to plot the PDF of a Distribution in the range [min_x, max_x]
		
		Args:
			min_x (int|float) the minimum value to plot
			max_x (int|float) the maximum value to plot
		
		Returns:
			list: x values for the pdf plot
			list: y values for the pdf plot
			
		"""
		# Create the arrays of values to plot
		x = [i for i in range(min_x, max_x)]
		y = [self.pdf(i) for i in x]
		
		# Make the plots
		fig, ax = plt.subplots()
		ax.set_title(title)
		ax.plot(x, y)
		ax.set_ylabel('Density')
		plt.show()

		return x, y
