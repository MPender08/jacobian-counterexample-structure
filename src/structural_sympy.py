#!/usr/bin/env python3
"""Exact structural checks for the three-dimensional Keller map.

All assertions are over QQ or a rational function field.  The script prints a
compact audit trail; failure of any claimed identity raises AssertionError.
"""

from __future__ import annotations

import platform
from sympy import (
    Matrix, Poly, Rational, Symbol, discriminant, expand, factor, groebner,
    simplify, symbols,
)


def zero(expr):
    return expand(expr) == 0


def det3(c1, c2, c3):
    return Matrix.hstack(c1, c2, c3).det()


def section(name):
    print(f"\n[{name}]")


x, y, z = symbols("x y z")
a, b, c = symbols("a b c")
u = 1 + x*y
F1 = u**3*z + y**2*u*(4 + 3*x*y)
F2 = y + 3*x*u**2*z + 3*x*y**2*(4 + 3*x*y)
F3 = 2*x - 3*x**2*y - x**3*z
F = Matrix([F1, F2, F3])
A = F.subs(z, 0)
B = F.diff(z)

section("environment")
import sympy
print("python", platform.python_version())
print("sympy", sympy.__version__)

section("base map")
detF = factor(F.jacobian([x, y, z]).det())
assert detF == -2
print("det JF =", detF)

section("general A+zB determinant coefficients")
# A universal symbolic check with twelve algebraically independent derivative
# placeholders.  It verifies the displayed coefficient formula without using
# any special property of the example.
Ax = Matrix(symbols("Ax1:4")); Ay = Matrix(symbols("Ay1:4"))
Bx = Matrix(symbols("Bx1:4")); By = Matrix(symbols("By1:4"))
B0 = Matrix(symbols("B1:4")); Z = Symbol("Z")
universal = det3(Ax + Z*Bx, Ay + Z*By, B0)
C0 = det3(Ax, Ay, B0)
C1 = det3(Bx, Ay, B0) + det3(Ax, By, B0)
C2 = det3(Bx, By, B0)
assert zero(universal - (C0 + Z*C1 + Z**2*C2))
print("det J(A+zB) = C0 + z*C1 + z^2*C2")
print("C0=det(Ax,Ay,B); C1=det(Bx,Ay,B)+det(Ax,By,B); C2=det(Bx,By,B)")

section("special B and rank geometry")
Bx0, By0 = B.diff(x), B.diff(y)
minors = [factor(Matrix.hstack(Bx0, By0).extract(rows, [0, 1]).det())
          for rows in ([0, 1], [0, 2], [1, 2])]
assert minors == [-9*x*u**4, 9*x**3*u**2, 18*x**4*u]
assert zero(det3(Bx0, By0, B))
radial = (B - Rational(1, 3)*x*Bx0 - Rational(1, 3)/x*By0).applyfunc(simplify)
assert radial == Matrix([0, 0, 0])
print("B =", list(B))
print("2x2 minors of dB =", minors)
print("rank(dB)=2 iff x(1+xy) != 0; rank=1 on x=0 or 1+xy=0")
print("on x!=0: B=(x/3)Bx+(1/(3x))By")

section("cubic cone and normalization")
p, q, s0 = symbols("p q s")
w, v, t = symbols("w v t")
M = Matrix([p**3, 3*q*p**2, -q**3])
cone = v**3 + 27*w**2*t
assert zero(cone.subs({w:M[0], v:M[1], t:M[2]}))
assert factor(cone) == cone
mp, mq = M.diff(p), M.diff(q)
assert (M - p*mp/3 - q*mq/3).applyfunc(expand) == Matrix([0, 0, 0])
# The missing Veronese generator s=p*q^2 gives the normalization.
rels = [v**2-9*w*s0, v*s0+3*w*t, 3*s0**2+v*t]
assert all(zero(r.subs({w:p**3, v:3*p**2*q, t:-q**3, s0:p*q**2})) for r in rels)
print("cone equation =", cone)
print("singular-locus equations from gradient: v=0, w=0")
print("normalization generators: w=p^3, v=3p^2q, s=pq^2, t=-q^3")
print("normalization relations =", rels)

section("target invariants and cone bridge")
Q = 27*a**2*c**2 - 18*a*b*c + 16*a + b**3*c - b**2
R = 4 - 3*b*c
L = 27*a*c**2 - 9*b*c + 8
P = expand(Q*x**3 + R*x - 2*c)
assert zero(R**3 + 27*Q*c**2 - L**2)
assert factor(discriminant(P, x)) == -4*L**2*Q
print("Q =", Q)
print("R =", R)
print("L =", L)
print("R^3+27Qc^2-L^2 =", expand(R**3 + 27*Q*c**2 - L**2))
print("disc_x(Qx^3+Rx-2c) =", factor(discriminant(P, x)))
print("same cubic form: C(B1,B2,B3)=0 and C(c,R,Q)=L^2")

section("projective-root model")
svar, S, T = symbols("svar S T")
root_cubic = 2*a*svar**3 - b*svar**2 + 2*svar - c
homogeneous_cubic = 2*a*S**3 - b*S**2*T + 2*S*T**2 - c*T**3
incidence_identity = 2*F1*x**3 - F2*x**2*u + 2*x*u**2 - F3*u**3
assert zero(incidence_identity)
root_disc = factor(discriminant(root_cubic, svar))
assert zero(root_disc + 4*Q)
special = factor(root_cubic.subs({a:-Rational(1,4), b:0, c:0}))
assert special == -svar*(svar-2)*(svar+2)/2
print("Phi(S,T) =", homogeneous_cubic)
print("Phi_F(x,1+xy) = 0")
print("disc_s Phi(s,1) = -4Q")
print("target (-1/4,0,0):", special, "with simple roots 0,2,-2")
print("affine source equals the simple-root locus in the incidence cover (literature result)")

section("source pullbacks and primitive cubic")
k = expand(F3/x)  # polynomial although written this way
d = expand(3*k*u - 2)
Rsrc = expand(R.subs({a:F1, b:F2, c:F3}))
Qsrc = expand(Q.subs({a:F1, b:F2, c:F3}))
Lsrc = expand(L.subs({a:F1, b:F2, c:F3}))
assert zero(k - (2 - 3*x*y - x**2*z))
assert zero(Rsrc - (d**2 - 6*k))
assert zero(x**2*Qsrc - (8*k - d**2))
assert zero(Lsrc - d*(9*k-d**2))
assert zero(d**3 - 3*Rsrc*d - 2*Lsrc)
print("k =", k)
print("d =", d)
print("F3=xk; R=d^2-6k; x^2Q=8k-d^2; L=d(9k-d^2)")
print("primitive equation: d^3-3Rd-2L=0")
Td = Symbol("T")
disc_d = factor(discriminant(Td**3 - 3*R*Td - 2*L, Td))
assert zero(disc_d + 108*(L**2-R**3))
assert zero(disc_d + 2916*Q*c**2)
print("disc_d = -108(L^2-R^3) = -2916*Q*c^2")
print("quadratic resolvent: Z^2-54L Z+729R^3")

section("birational factorization and Jacobian compensation")
q0, k0, d0 = symbols("q0 k0 d0")
phi = Matrix([x, k, d])
det_phi = factor(phi.jacobian([x, y, z]).det())
assert zero(det_phi - 3*x**3*k)
psi = Matrix([
    -(d0+2)*(d0**2+d0-9*k0-2)/(27*k0**2*q0**2),
    -(d0**2-6*k0-4)/(3*k0*q0),
    k0*q0,
])
det_psi = factor(psi.jacobian([q0, k0, d0]).det())
assert det_psi == -Rational(2, 3)/(k0*q0**3)
composition = psi.subs({q0:x, k0:k, d0:d})
assert all(simplify(composition[i]-F[i]) == 0 for i in range(3))
assert simplify(det_phi * det_psi.subs({q0:x, k0:k, d0:d})) == -2
print("Phi=(q,k,d), det JPhi =", det_phi)
print("Psi(q,k,d) =", list(psi))
print("det JPsi =", det_psi)
print("Psi o Phi = F; determinant product = -2")

section("finite cubic model")
# pi(d,R,c)=(R,(d^3-3Rd)/2,c); target change tau=(R,L,c)
Rv, cv = symbols("Rv cv")
pi = Matrix([Rv, (d0**3-3*Rv*d0)/2, cv])
det_pi = factor(pi.jacobian([d0, Rv, cv]).det())
assert zero(det_pi + Rational(3, 2)*(d0**2-Rv))
tau = Matrix([R, L, c])
det_tau = factor(tau.jacobian([a, b, c]).det())
assert zero(det_tau - 81*c**3)
print("pi(d,R,c)=(R,(d^3-3Rd)/2,c), det Jpi =", det_pi)
print("tau(a,b,c)=(R,L,c), det Jtau =", det_tau)
print("boundary d^2=R maps to L=-d^3, hence L^2=R^3 (equiv. Q=0)")

section("Galois square class")
disc_Q_as_quad_a = factor(discriminant(Poly(Q, a), a))
assert disc_Q_as_quad_a == -4*(3*b*c-4)**3
print("disc_a(Q) =", disc_Q_as_quad_a)
print("Q is irreducible over C[b,c] because this is not a square in C(b,c)")
print("generic cubic Galois group = S3; quadratic subfield = K(sqrt(-Q))")
print("over Q!=0 the simple-root incidence cover is finite etale of degree 3")

section("exact structured family")
# Same-day manuscript family, H=0.  General H follows by the source
# automorphism z -> cz+H; here c0 is retained explicitly.
lam, alpha, gamma = symbols("lambda alpha gamma", nonzero=True)
U = lam + x*y
W = gamma*z
BB = U**2*W + 3*y**2*(4*lam+3*x*y)/(alpha*lam**2)
Fam = Matrix([
    U*BB,
    y + alpha*x*BB,
    2*x/lam - 3*x**2*y/lam**2 - alpha*x**3*W/3,
])
det_fam = factor(Fam.jacobian([x, y, z]).det())
assert det_fam == -2*gamma*lam**2
print("det J F_{lambda,alpha,gamma,0} =", det_fam)
print("adding arbitrary H(x,y) in W=gamma*z+H is source-triangular equivalence")

section("plane-coordinate pullback family")
X, Y = symbols("X Y")
qf, rf = symbols("qf rf")
pf = 1 + qf*rf
Ftemplate = Matrix([
    pf**3*z + rf**2*pf*(1+3*pf),
    rf + 3*qf*pf**2*z + 3*qf*rf**2*(1+3*pf),
    qf*(5-3*pf) - qf**3*z,
])
Jqr = Symbol("Jqr")
det_template = factor(Ftemplate.jacobian([qf, rf, z]).det())
assert det_template == -2
print("template determinant in (q,r,z) =", det_template)
print("after (q,r)=(q(x,y),r(x,y)): det = -2*det d(q,r)/d(x,y)")

section("done")
print("all exact assertions passed")
