# A-R Hedar and M Fukushima, "Derivative-Free Filter Simulated Annealing
# Method for Constrained Continuous Global Optimization", Journal of
# Global Optimization, 35(4), 521-549 (2006).
# 
# code for function PrPc and PrPf
# translated from Matlab Code written by A. Hedar (Nov. 23, 2005).
# http://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/go.htm
"Pressure Vessel Design"

def objective(x):
    x0,x1,x2,x3 = x
    return 0.6224*x0*x2*x3 + 1.7781*x1*x2**2 + 3.1661*x0**2*x3 + 19.84*x0**2*x2

bounds = [(0,1e6)]*4
# with penalty='penalty' applied, solution is:
xs = [0.72759093, 0.35964857, 37.69901188, 240.0]
ys = 5804.3762083

from mystic.symbolic import generate_constraint, generate_solvers, solve
from mystic.symbolic import generate_penalty, generate_conditions

equations = """
-x0 + 0.0193*x2 <= 0.0
-x1 + 0.00954*x2 <= 0.0
-pi*x2**2*x3 - (4/3.)*pi*x2**3 + 1296000.0 <= 0.0
x3 - 240.0 <= 0.0
"""
#cf = generate_constraint(generate_solvers(solve(equations))) #XXX: inequalities
pf = generate_penalty(generate_conditions(equations), k=1e12)

from mystic.constraints import as_constraint

cf = as_constraint(pf)



if __name__ == '__main__':

    from mystic.solvers import diffev2
    from mystic.math import almostEqual

    result = diffev2(objective, x0=bounds, bounds=bounds, penalty=pf, npop=40, gtol=500, disp=False, full_output=True)

    assert almostEqual(result[0], xs, rel=1e-2)
    assert almostEqual(result[1], ys, rel=1e-2)



# EOF