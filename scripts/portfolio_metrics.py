import numpy as np
from scipy import optimize

def portfolio_risk(weights, cov_matrix): 
    
    """Calculate expected portfolio risk."""
    return np.sqrt(np.dot(np.dot(weights.T, cov_matrix), weights))

def objective_function(weights, cov_matrix):
    
    """Objective function to minimize portfolio risk."""
    
    return portfolio_risk(weights, cov_matrix)

def portfolio_return(weights, mean_returns):
    
    """Calculate expected portfolio return."""
    
    return np.sum(mean_returns*weights)  
    
def constraints_sum_to_1(weights): 
    
    """Constraints ensure weights sum to 1."""
    
    return np.sum(weights)-1
    
def constraint_return_eq_target_return(weight, target_return, mean_returns):
    
    """Constraint to ensure portfolio return equals target return."""
    
    return portfolio_return(weight, mean_returns)-target_return

def get_efficient_frontier(mean_returns, cov_matrix, bounds, initial_weights, num_points=10):
    
    """Generate the efficient frontier by varying target returns and calculating the corresponding risk."""
    
    target_returns = np.linspace(min(mean_returns), max(mean_returns), 100)
    efficient_frontier_volatility = []
    for target_return in target_returns: # So basically calling all the functions again in the loop 
        def constraint_return_eq_target_return(weight, target_return):
            return portfolio_return(weight, mean_returns)-target_return
        
        constraints = [
            {'type': 'eq', 'fun': constraints_sum_to_1}, # checks that the value equals
            {'type': 'eq', 'fun': lambda w: constraint_return_eq_target_return(w, target_return)} 
        ] 

        result = optimize.minimize(
            objective_function, 
            initial_weights, 
            method = 'SLSQP',
            constraints=constraints, 
            bounds=bounds
        ) 
        
        if result.success:
            efficient_frontier_volatility.append(result.fun)
        else:
            efficient_frontier_volatility.append(np.nan)
            
    return target_returns , efficient_frontier_volatility

def neg_sharpe_ratio(weights,  risk_free_rate, cov_matrix, mean_returns):
    
    """ This will maximize the sharpe ratio by minimizing the negative sharpe ratio """
    
    portfolio_ann_return = portfolio_return(weights, mean_returns)
    portfolio_ann_volatility = portfolio_risk(weights, cov_matrix)
    sharpe_ratio = (portfolio_ann_return - risk_free_rate)/portfolio_ann_volatility
    return -sharpe_ratio