from email import message
import math
from .GeneralDistribution import Distribution
from .ErlangDistribution import Erlang

class HypoExponential(Distribution):
    """ Hypoexponential Distribution Class for calculating and 
	visualizing a hypoexponential distribution.
	
	Attributes:
		lp1 (float) representing the decay parameter (λ) of the first composing Exponential Distribution
        lp2 (float) representing the decay parameter of the second composing Exponential Distribution
		data_list (list of floats) a list of floats extracted from the data file
	
    """
    def __init__(self, lp1, lp2):
        self.lp1 = lp1
        self.lp2 = lp2

        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())
    
    def calculate_mean(self):
        """Function to calculate the mean from the lp factors
        
        Args: 
            None
        
        Returns: 
            float: mean of the distribution
    
        """
        self.mean = (1/self.lp1) + (1/self.lp2)
        return self.mean

    def calculate_variance(self):
        """Function to calculate the variance from the lp factors
        
        Args: 
            None
        
        Returns: 
            float: variance of the distribution
    
        """
        self.variance = (1/(self.lp1*self.lp1))+(1/(self.lp2*self.lp2))
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
        coefficient = (self.lp1*self.lp2)/(self.lp1 - self.lp2)
        return coefficient*(math.exp(-x*self.lp2)-math.exp(-x*self.lp1))
    
    def __add__(self, other):
        raise NotImplementedError
    
    def __repr__(self):
        """Function to output the characteristics of the HypoExponential instance
		
		Args:
			None
		
		Returns:
			string: characteristics of the HypoExponential
		
		"""
        return "Lambda Parameter 1 {}, Lambda Parameter 2 {}".format(self.lp1, self.lp2)

class Exponential(Distribution):
    """ Exponential distribution Class for calculating and 
	visualizing a Exponential distribution.
	
	Attributes:
		lp (float) representing the decay parameter (λ) of the function
		data_list (list of floats) a list of floats extracted from the data file
	
    """
    def __init__(self, lp):
        self.lp = lp

        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())
    
    def calculate_mean(self):
        """Function to calculate the mean from lp
        
        Args: 
            None
        
        Returns: 
            float: mean of the distribution
    
        """
        self.mean = 1/self.lp
        return self.mean

    def calculate_variance(self):
        """Function to calculate the variance from lp
        
        Args: 
            None
        
        Returns: 
            float: variance of the distribution
    
        """
        self.variance = 1/(self.lp*self.lp)
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
        return self.lp * math.exp(-self.lp * x)
    
    def replace_stats_with_data(self):
    
        """Function to calculate p and n from the data set
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """
        n = len(self.data)
        if n > 0:
            mu = 1.0 * sum(self.data) / n
            self.lp = 1/mu
            self.calculate_mean()
            self.calculate_stdev()
        else:
            raise IndexError('No data has been loaded')

    def __add__(self, other):
        """Function to add together two independent exponential distributions
		
		Args:
			other (Exponential): ExponentialDistribution instance
			
		Returns:
			An ErlangDistribution if both exponentials have the same lambda parameter
            A HypoExponentialDistribution if both exponentials have differing lambda parameters
			
		"""
        if isinstance(other, Exponential):
            if other.lp == self.lp:
                result = Erlang(self.lp*self.lp, 2)
            else:
                result = HypoExponential(self.lp, other.lp)
            return result
        else:
            raise TypeError("You must add two exponential distributions together")
    
    def __repr__(self):
        """Function to output the characteristics of the Exponential instance
		
		Args:
			None
		
		Returns:
			string: characteristics of the Exponential
		
		"""
        return "Lambda parameter {}, mean {}, standard deviation {}".format(self.lp, self.mean, self.stdev)