import math
from .GeneralDistribution import Distribution
from .utils import factorial

class Erlang(Distribution):
    """ Erlang Distribution Class for calculating and 
	visualizing a Erlang distribution.
	
	Attributes:
		lp (float) representing the decay parameter (λ) of the function
        k (integer) representing the amount of independent exponencial random variables in this distribution. AKA the 'shape'
		data_list (list of floats) a list of floats extracted from the data file
	
    """
    def __init__(self, lp, k):
        self.lp = lp
        self.k = k

        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())
    
    def calculate_mean(self):
        """Function to calculate the mean from k and lp
        
        Args: 
            None
        
        Returns: 
            float: mean of the distribution
    
        """
        self.mean = self.k/self.lp
        return self.mean

    def calculate_variance(self):
        """Function to calculate the variance from k and lp
        
        Args: 
            None
        
        Returns: 
            float: variance of the distribution
    
        """
        self.variance = self.k/(self.lp*self.lp)
        return self.variance
    
    def calculate_stdev(self):
        """Function to calculate the standard deviation from the variance
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the distribution
    
        """
        self.calculate_variance()
        self.stdev = math.sqrt(self.variance)
        return self.stdev
    
    def pdf(self, x):
        """Probability density function calculator for the distribution.
        
        Args:
            x (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        numerator = math.pow(self.lp, self.k)*math.pow(x,self.k-1)*math.exp(-x*self.lp)
        denominator = factorial(self.k - 1)
        return numerator/denominator
    
    def  __add__(self, other):
        if isinstance(other, Erlang):
            if other.lp == self.lp:
                return Erlang(self.lp, self.k+other.k)
            else:
                raise AttributeError('Erlang distributions must have the same lambda parameter to be added')

    def __repr__(self):
	
        """Function to output the characteristics of the Gaussian instance
		
		Args:
			None
		
		Returns:
			string: characteristics of the Gaussian
		
		"""
        return "mean {}, standard deviation {}".format(self.mean, self.stdev)
