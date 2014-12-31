# A-R Hedar and M Fukushima, "Derivative-Free Filter Simulated Annealing
# Method for Constrained Continuous Global Optimization", Journal of
# Global Optimization, 35(4), 521-549 (2006).
# 
# code for function PrG9c and PrG9f
# translated from Matlab Code written by A. Hedar (Nov. 23, 2005).
# http://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/go.htm

def objective(x):
    x0,x1,x2,x3,x4,x5,x6 = x
    return (x0-10)**2 + 5*(x1-12)**2 + x2**4 + 3*(x3-11)**2 + \
           10*x4**6 + 7*x5**2 + x6**4 - 4*x5*x6 - 10*x5 - 8*x6

bounds = [(-10.,10.)]*7
# with penalty='penalty' applied, solution is:
xs = [2.330499, 1.951372, -0.4775414, 4.365726, -0.6244870, 1.038131, 1.594227]
ys = 680.6300573

from mystic.symbolic import generate_constraint, generate_solvers, solve
from mystic.symbolic import generate_penalty, generate_conditions

equations = """
2*x0**2 + 3*x1**4 + x2 + 4*x3**2 + 5*x4 - 127.0 <= 0.0
7*x0 + 3*x1 + 10*x2**2 + x3 - x4 - 282.0 <= 0.0
23*x0 + x1**2 + 6*x5**2 - 8*x6 - 196.0 <= 0.0
4*x0**2 + x1**2 - 3*x0*x1 + 2*x2**2 + 5*x5 - 11*x6 <= 0.0
"""
#cf = generate_constraint(generate_solvers(solve(equations))) #XXX: inequalities
pf = generate_penalty(generate_conditions(equations), k=1e12)

from mystic.constraints import as_constraint

cf = as_constraint(pf)



if __name__ == '__main__':

    from mystic.solvers import diffev2
    from mystic.math import almostEqual

    result = diffev2(objective, x0=bounds, bounds=bounds, penalty=pf, npop=40, gtol=200, disp=False, full_output=True)

    assert almostEqual(result[0], xs, rel=1e-2)
    assert almostEqual(result[1], ys, rel=1e-2)



# EOF
