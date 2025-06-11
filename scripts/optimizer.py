from scipy.optimize import minimize

def optimize_portfolio(objective_fn, initial_weights, constraints, bounds, args=()):
    
    """ This will get the optimized the portfolio """
    
    return minimize(fun=objective_fn, x0=initial_weights, constraints=constraints, bounds=bounds, args=args)
