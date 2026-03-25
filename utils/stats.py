def compute_variance(arr):
    """
    Compute sample variance from scratch.
    
    Formula: Var(X) = Σ(xᵢ - x̄)² / (n-1)
    
    Args:
        arr: list or array of numbers
        
    Returns:
        float: sample variance
    """
    n = len(arr)
    mean = sum(arr)/n

    sq_dv_sum = sum((x-mean)**2 for x in arr)
    
    return sq_dv_sum / (n - 1)

def compute_covariance(x,y):
    """Computes covariance.
    
    Formula: Cov(x,y) = Σ(xᵢ - x̄)(yᵢ - ȳ) / (n-1)
    
    Args:
        x: first array
        y: second array
        
    Returns:
        float covariance """
    assert len(x) == len(y)
    n = len(x)
    mean_x = sum(x)/n
    mean_y = sum(y)/n

    return sum((x[i]-mean_x)*(y[i]-mean_y) for i in range(n))/(n-1)

def compute_corelation(x,y):
    """Computes corelation between two data
    
    Formula: Correlation(x,y) = Cov(x/y)/(sqrt(var(x))*sqrt(var(y)))
    Args:
        x: first array
        y: second array
        
    Returns:
        float correlation"""
    return compute_covariance(x,y)/((compute_variance(x)*compute_variance(y))**0.5)
 
def log_returns(prices):
    return np.log(prices/prices.shift(1)).dropna()

def calculate_maxdd(prices):
    run_max = prices.cummax()
    dropdows = (prices-run_max)/run_max
    return dropdows.min()
#### Testing teh code ####
import numpy as np

# Test array
test_data = [1, 2, 3, 4, 5]
test_data_2 = [4 ,5 ,6 ,7 ,8]
my_var = compute_variance(test_data)
my_cov = compute_covariance(test_data,test_data_2)

np_var = np.var(test_data, ddof=1)
np_cov = np.cov(test_data,test_data_2, ddof=1)

print(f"My variance: {my_var}")
print(f"NumPy variance: {np_var}")
print(f"Match: {abs(my_var - np_var) < 1e-10}")

print(f"My covariance: {my_cov}")
print(f"Numpy covaraince: {np_cov}")
print(f"Match: {abs(my_cov - np_cov) < 1e-10}")
