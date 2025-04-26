import os

script_dir = os.path.dirname(__file__)  # location of the running script
rel_path = os.path.join(script_dir, '../../Data/portfolio.dat')
abs_path = os.path.abspath(rel_path)
print("The absolute path of the portfolio file is: ", abs_path)

sum_portfolio = 0.0
with open(abs_path, "r") as f:
    for line in f:
        line = line.split()
        nshares, price = int(line[1]), float(line[2])
        sum_portfolio += nshares * price

print("The total cost of the portfolio is: ", sum_portfolio)