# A-R Hedar and M Fukushima, "Derivative-Free Filter Simulated Annealing
# Method for Constrained Continuous Global Optimization", Journal of
# Global Optimization, 35(4), 521-549 (2006).
# 
# code for function PrTc and PrTf
# translated from Matlab Code written by A. Hedar (Nov. 23, 2005).
# http://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/go.htm
"a Tension-Compression String"

def objective(x):
    x0,x1,x2 = x
    return x0**2 * x1 * (x2 + 2)

bounds = [(0,100)]*3
# with penalty='penalty' applied, solution is:
xs = [0.05168906, 0.35671773, 11.28896619]
ys = 0.01266523

from mystic.symbolic import generate_constraint, generate_solvers, solve
from mystic.symbolic import generate_penalty, generate_conditions

equations = """
1.0 - (x1**3 * x2)/(71785*x0**4) <= 0.0
(4*x1**2 - x0*x1)/(12566*x0**3 * (x1 - x0)) + 1./(5108*x0**2) - 1.0 <= 0.0
1.0 - 140.45*x0/(x2 * x1**2) <= 0.0
(x0 + x1)/1.5 - 1.0 <= 0.0
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
