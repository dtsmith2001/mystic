# A-R Hedar and M Fukushima, "Derivative-Free Filter Simulated Annealing
# Method for Constrained Continuous Global Optimization", Journal of
# Global Optimization, 35(4), 521-549 (2006).
# 
# code for function PrG10c and PrG10f
# translated from Matlab Code written by A. Hedar (Nov. 23, 2005).
# http://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/go.htm

def objective(x):
    x0,x1,x2,x3,x4,x5,x6,x7 = x
    return x0 + x1 + x2

bounds = [(100,10000)] + [(1000,10000)]*2 + [(10,1000)]*5
# with penalty='penalty' applied, solution is:
xs = [579.3167, 1359.943, 5110.071, 182.0174, \
      295.5985, 217.9799, 286.4162,395.5979]
ys = 7049.3307

from mystic.symbolic import generate_constraint, generate_solvers, solve
from mystic.symbolic import generate_penalty, generate_conditions

equations = """
-1 + 0.0025*(x3 + x5) <= 0.0
-1 + 0.0025*(-x3 + x4 + x6) <= 0.0
-1 + 0.01*(-x4 + x7) <= 0.0
100*x0 - x0*x5 + 833.33252*x3 - 83333.333 <= 0.0
x1*x3 - x1*x6 - 1250*x3 + 1250*x4 <= 0.0
x2*x4 - x2*x7 - 2500*x4 + 1250000 <= 0.0
"""
#cf = generate_constraint(generate_solvers(solve(equations))) #XXX: inequalities
pf = generate_penalty(generate_conditions(equations), k=1e12)

from mystic.constraints import as_constraint

cf = as_constraint(pf)



if __name__ == '__main__':

    from mystic.solvers import diffev2
    from mystic.math import almostEqual

    result = diffev2(objective, x0=bounds, bounds=bounds, penalty=pf, npop=80, gtol=500, disp=False, full_output=True)

    assert almostEqual(result[0], xs, rel=1e-2)
    assert almostEqual(result[1], ys, rel=1e-2)



# EOF