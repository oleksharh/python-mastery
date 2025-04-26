import os

script_dir = os.path.dirname(__file__)  # location of the running script
rel_path = os.path.join(script_dir, '../../Data/portfolio.dat')
rel_path_ex_4 = os.path.join(script_dir, '../../Data/portfolio3.dat')
rel_path_ex_4_2 = os.path.join(script_dir, '../../Data/portfolio2.dat')
abs_3_path = os.path.abspath(rel_path)
abs_4_path = os.path.abspath(rel_path_ex_4)
abs_4_2_path = os.path.abspath(rel_path_ex_4_2)

def portfolio_cost(filename):
    sum_portfolio = 0.0
    with open(filename, "r") as f:
        for line in f:
            line = line.split()
            try:
                nshares, price = int(line[1]), float(line[2])
                sum_portfolio += nshares * price
            except ValueError:
                print(f"Error converting line to numbers: {line}")
                continue
        
    return sum_portfolio

print("The total cost of the portfolio is: ", portfolio_cost(abs_4_path))
print("The total cost of the portfolio is: ", portfolio_cost(abs_4_2_path))

