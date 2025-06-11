import matplotlib as plt

def plot_efficient_frontier(frontier_volatility, target_returns, eff_idx):
    
    plt.plot(frontier_volatility, target_returns[:len(frontier_volatility)], 'g--', linewidth=3, label='Efficient Frontier')
    plt.annotate('Efficient Frontier',
        xy=(frontier_volatility[eff_idx], target_returns[eff_idx]),
           xytext=(frontier_volatility[eff_idx]+0.1, target_returns[eff_idx]-0.1),
           arrowprops = dict(arrowstyle = '->', color = 'green'),
           color = 'green', fontsize=16)
    plt.legend()
    plt.show()
    
def plot_risk_free_portfolio(risk_free_rate):
    plt.scatter(0, risk_free_rate, color = 'red', s = 100, marker = 'o', label='Risk-Free Portfolio')
    plt.annotate('Risk-Free Portfolio',
            xy=(0,risk_free_rate),
            xytext=(0.02, risk_free_rate + 0.02),
            arrowprops = dict(arrowstyle = '->', color = 'red'),
            color = 'red', fontsize=16)
    plt.legend()
    plt.show()

def plot_market_portfolio(market_portfolio_volatility, market_portfolio_return):
    plt.scatter(market_portfolio_volatility, market_portfolio_return, color = 'red', s = 100, marker = 'o', label='Market Portfolio')
    plt.annotate('Market Portfolio',
        xy=(market_portfolio_volatility,market_portfolio_return),
           xytext=(market_portfolio_volatility + 0.03, market_portfolio_return + 0.02),
           arrowprops = dict(arrowstyle = '->', color = 'red'),
           color = 'red', fontsize=16)
    plt.legend()
    plt.show()

def plot_capital_market_line(cml_volatility, cml_returns, cml_idx):
    plt.plot(cml_volatility,cml_returns, 'b--', linewidth = 2, label = 'Capital Market Line (CML)')
    plt.annotate('Capital Market Line',
        xy=(cml_volatility[cml_idx], cml_returns[cml_idx]),
           xytext=(cml_volatility[cml_idx]+0.1, cml_returns[cml_idx]-0.1),
           arrowprops = dict(arrowstyle = '->', color = 'blue'),
           color = 'blue', fontsize=16)    
    plt.legend()
    plt.show()
    
