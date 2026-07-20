# Structural Investigation of the Three-Sheeted Jacobian Counterexample

**Exact symbolic follow-up report**  
**Date:** 20 July 2026  
**Arithmetic:** exact rational and polynomial arithmetic  
**Primary system:** SymPy 1.14.0  
**Independent system:** Nerdamer 1.1.13

## Executive conclusion

The displayed three-point collision is not isolated. The map has generic degree three. A projective coordinate

    [S:T]=[x:1+xy]

identifies the source exactly with the simple-root locus of the binary cubic

    Phi_{a,b,c}(S,T)=2aS^3-bS^2T+2ST^2-cT^3.

Consequently a target with nonzero cubic discriminant has three affine preimages, a generic point of the discriminant hypersurface has one, and a particular smooth curve in that hypersurface has none. The nonproperness set is the entire discriminant hypersurface, not merely the omitted curve.

The generic function-field extension has degree three and Galois closure group `S3`. Its quadratic subfield is obtained by adjoining `sqrt(-Q)`, where

    Q=27a^2c^2-18abc+16a+b^3c-b^2.

The most informative new structural calculation is a second, birational cubic model. Polynomial source functions `q=x`, `k`, and `d` factor the map rationally as `F=Psi o Phi`; the nonconstant Jacobians of these two rational transformations cancel exactly. After a birational target change, the map becomes the finite cubic

    (d,R,c) -> (R,(d^3-3Rd)/2,c).

Its ramification divisor `d^2=R` is precisely the divisor removed by the birational source chart. Its image is `Q=0`. Thus the original polynomial map has no critical points because the ramification of the finite cubic model has been moved to infinity, where two inverse sheets escape generically and all three escape on the cusp curve.

The third variable is structurally essential in the displayed polynomial realization: it supplies the direction `B` in `F=A+zB`, while the two nonconstant rational Jacobian factors cancel only in three dimensions. It is best described as both a determinant compensator and an auxiliary compatibility variable. It is not a branch label: the branch label is the projective root `[x:1+xy]` (or, birationally, `d`).

A same-day manuscript matching the formula proves exact parameter families and higher-degree deformations. Our code independently verifies its three-parameter determinant formula. Therefore a nontrivial exact family has been found in the literature; this report does not present that family as an independent discovery. The manuscript also proves examples of every generic degree at least three. This sharply supersedes a rigidity conjecture for unrestricted structured deformations.

## 1. Status and reliability

| Result | Status | Basis |
|---|---|---|
| General `A+zB` determinant equations | Verified | Universal symbolic determinant expansion |
| Rank geometry and cubic cone for the displayed `B` | Verified | Exact minors and identities |
| Normalization of the cone | Verified | Explicit finite birational Veronese ring; standard normality fact |
| Projective-root incidence description | Literature theorem; defining identities rechecked | Same-day manuscript plus exact substitution |
| Generic degree three and complete fiber counts | Literature theorem; consistent with earlier elimination | Finite incidence cover and exact reconstruction |
| Generic Galois group `S3` | Verified | Irreducible cubic plus nonsquare discriminant |
| Local monodromy descriptions | Rigorous algebraic interpretation | Cubic normal forms and valuations |
| Birational finite-cubic factorization | Verified, apparently new relative to located sources | Exact forward/inverse formulas and Jacobians |
| Cone-to-target invariant bridge | Verified, apparently new relative to located sources | Exact polynomial identities |
| Nonproperness geometry | Verified and literature-confirmed | Finite incidence compactification and explicit escape arcs |
| Structured parameter family | Literature theorem; determinant independently verified for `H=0` | Exact CAS computation |
| Arbitrary-degree deformations | Literature result, not independently recomputed here | Theorem 5.2 and Corollary 5.3 of the same-day manuscript |
| Full bounded-degree rigidity | Not established | Unnecessary after exact families; broad Gröbner search omitted |
| Ordinary projective resolution at infinity | Not completed | Naive homogenization has a large base locus |

No floating-point output is used as proof. Rational formulas are always accompanied by their excluded divisors. Claims imported from the same-day manuscript are labeled as literature results rather than independent computations.

## 2. The universal `A+zB` determinant equations

Let `A,B:C^2 -> C^3` and

    F(x,y,z)=A(x,y)+zB(x,y).

Writing column determinants, exact multilinearity gives

    det JF = C0 + z C1 + z^2 C2,

where

    C0 = det(Ax,Ay,B),
    C1 = det(Bx,Ay,B)+det(Ax,By,B),
    C2 = det(Bx,By,B).

Hence `det JF=lambda != 0` is equivalent to the three polynomial identities

    det(Bx,By,B)=0,
    det(Bx,Ay,B)+det(Ax,By,B)=0,
    det(Ax,Ay,B)=lambda.

The first condition depends only on `B`; the second is linear in the first derivatives of `A`; the last is quadratic in them. In differential-form language, the first condition says that the pullback of the ambient volume form contracted with the radial field vanishes on `B`. On the rank-two locus of `dB`, it has the concrete meaning

    B is in span(Bx,By).

At rank at most one the determinant vanishes automatically, so the condition is weaker there.

### 2.1 The displayed `B`

For `u=1+xy`,

    B=(u^3,3xu^2,-x^3).

The three `2 x 2` minors of `[Bx By]` are

    -9xu^4,  9x^3u^2,  18x^4u.

Thus `rank(dB)=2` exactly when `xu != 0`; it is one on `x=0` or `u=0`. These loci are disjoint, so the rank never vanishes. On `x != 0`,

    B=(x/3)Bx+(1/(3x))By.

This is the exact radial-tangency mechanism forcing the `z^2` coefficient to disappear.

### 2.2 Factorization through a homogeneous cubic map

Set `(p,q)=(u,x)` and

    M(p,q)=(p^3,3qp^2,-q^3).

Then `B=M(u,x)`. Euler's identity gives

    M=(p/3)Mp+(q/3)Mq,

so `det(Mp,Mq,M)=0` before any substitution. The map `(x,y)->(u,x)` is birational on `x != 0`, with inverse `y=(p-1)/q`. This shows that the radial cancellation is built into a degree-three homogeneous parameterization, not a coincidental expansion.

## 3. The cubic cone and its normalization

Writing the coordinates of `M` as `(w,v,t)`, its image lies on

    C(w,v,t)=v^3+27w^2t=0.

This polynomial is irreducible. Its singular locus is the line `w=v=0`. The parameterization by `A^2_{p,q}` is generically three-to-one: scalar multiplication `(p,q)->(omega p,omega q)` for `omega^3=1` leaves `M` fixed.

It is important not to call `A^2` the normalization. The normalization ring is the third Veronese invariant ring

    C[p^3,p^2q,pq^2,q^3]=C[p,q]^{mu_3}.

Adjoining `s=pq^2`, one obtains the finite birational normalization by the relations

    v^2=9ws,
    vs=-3wt,
    3s^2=-vt.

Geometrically, it is the affine cone over the twisted cubic and has only the quotient singularity at the vertex. The map `A^2 -> normalization` is the finite `mu_3` quotient; the normalization then maps finitely and birationally to the nonnormal cubic cone.

## 4. The invariant bridge

For target coordinates `(a,b,c)`, define

    Q=27a^2c^2-18abc+16a+b^3c-b^2,
    R=4-3bc,
    L=27ac^2-9bc+8.

Exact expansion gives

    R^3+27Qc^2=L^2.

Thus the same cubic form occurs twice:

    C(B1,B2,B3)=0,
    C(c,R,Q)=L^2.

The target invariants therefore form a double-cover deformation of the same cubic cone. This is a genuine symbolic bridge between the `B`-cone and the eliminant invariants, though it does not by itself prove that one construction uniquely determines the other.

### 4.1 Source coordinates behind the bridge

Define polynomial functions

    k=2-3xy-x^2z,
    d=3k(1+xy)-2.

Since `F3=xk`, direct pullback of the target invariants gives

    c=xk,
    R=d^2-6k,
    x^2Q=8k-d^2,
    L=d(9k-d^2).

The cone identity reduces to the elementary one-variable identity

    (d^2-6k)^3+27k^2(8k-d^2)=d^2(9k-d^2)^2.

More significantly, `d` satisfies the depressed cubic

    d^3-3Rd-2L=0.

Its discriminant is

    -108(L^2-R^3)=-2916Qc^2.

Unlike the earlier eliminant in `x`, this discriminant has no extra `L^2` factor. The earlier factor reflects failure of `x` to separate two distinct points when `L=0`; it is not ramification of the full cover.

## 5. Exact projective-root compactification

The cleanest global description was found in a same-day manuscript matching this map. The defining polynomial identity is independently checked in the supplied code:

    2F1 x^3-F2 x^2(1+xy)+2x(1+xy)^2-F3(1+xy)^3=0.

Consequently `[S:T]=[x:1+xy]` is a root of

    Phi_{a,b,c}(S,T)=2aS^3-bS^2T+2ST^2-cT^3.

The coefficient of `ST^2` is always two, so the binary cubic is never identically zero. The cited manuscript proves that the source is isomorphic to the simple-root locus of the incidence hypersurface `Phi=0` in `C^3 x P^1`. It supplies regular reconstruction formulas on both projective charts, including the root at infinity.

The affine cubic on `T=1` has discriminant

    disc_s(2as^3-bs^2+2s-c)=-4Q.

Therefore:

- `Q != 0`: three simple projective roots, hence exactly three affine preimages;
- `Q=0` away from the triple-root curve: one simple root and one double root, hence exactly one affine preimage;
- on the triple-root curve: no simple roots, hence no affine preimage.

The omitted curve is

    Gamma: 12a-b^2=0,  3bc-4=0,

and is parametrized by

    (a,b,c)=(1/(3t^2),2/t,2t/3),  t != 0.

At `(-1/4,0,0)`, the root cubic is

    -s(s-2)(s+2)/2,

so its three simple roots reconstruct exactly the reported three points. This proves that their multiplicity is generic, not exceptional.

## 6. Function fields, Galois closure, and monodromy

On the chart `1+xy != 0`, let `s=x/(1+xy)`. The reconstruction formulas imply

    C(x,y,z)=C(a,b,c)(s),
    2as^3-bs^2+2s-c=0.

The incidence theorem gives degree three, so this cubic is minimal and irreducible over `K=C(a,b,c)`.

The polynomial `Q`, regarded as a quadratic in `a`, has discriminant

    disc_a(Q)=-4(3bc-4)^3.

This is not a square in `C(b,c)`, so `Q` is irreducible and its valuation along `Q=0` is odd. Hence `-Q` is not a square in `K`. An irreducible cubic with nonsquare discriminant has generic Galois group

    Gal(K_split/K)=S3.

The splitting field has degree six. Its unique quadratic subfield is

    K(sqrt(-Q)).

After adjoining `sqrt(-Q)`, the remaining Galois group is `A3`, cyclic of order three. For the depressed `d`-cubic, one convenient quadratic resolvent is

    Z^2-54LZ+729R^3,

whose discriminant has the same square class.

### 6.1 Monodromy interpretation

Over `U={Q != 0}`, the incidence description makes the map a finite etale cover of degree three. Its geometric monodromy is `S3`.

- Around a generic smooth point of `Q=0`, the binary cubic has one simple and one double root. A small loop swaps the two roots that collide at the boundary: a transposition.
- Around the cusp curve `Gamma`, the three roots coalesce. A transverse cusp loop gives a three-cycle.
- Around a generic point of `L=0` with `Q != 0`, the full cover is unramified. The factor `L^2` in the `x`-eliminant records two different sheets having the same `x` coordinate, so its local full-cover monodromy is trivial.

No sheet is globally distinguished. The special branch `x=0` visible over `(a,0,0)` is moved among all three sheets by the transitive `S3` action.

## 7. Birational factorization and determinant compensation

Define

    Phi(x,y,z)=(q,k,d)=(x,2-3xy-x^2z,3k(1+xy)-2).

On `qk != 0`, its rational inverse is

    p=(d+2)/(3k),
    x=q,
    y=(p-1)/q,
    z=(5k-d-2-k^2)/(kq^2).

Define the rational map

    Psi1=-(d+2)(d^2+d-9k-2)/(27k^2q^2),
    Psi2=-(d^2-6k-4)/(3kq),
    Psi3=kq.

Exact simplification gives

    F=Psi o Phi,
    det JPhi=3q^3k,
    det JPsi=-2/(3kq^3).

Therefore

    det JF=-2

is a literal cancellation of two reciprocal rational Jacobians. The composition is polynomial because the special formulas cancel all apparent denominators after pulling back. This supplies a conceptual determinant explanation complementary to direct expansion.

### 7.1 Finite cubic normal form

On the target set `c != 0`, the change

    tau(a,b,c)=(R,L,c)

is birational, with inverse

    b=(4-R)/(3c),
    a=(L-3R+4)/(27c^2).

Its Jacobian is `81c^3`. In these coordinates the function-field map is the finite cubic

    pi(d,R,c)=(R,(d^3-3Rd)/2,c).

The ramification divisor of `pi` is

    d^2=R.

On it, `L=-d^3`, hence `L^2=R^3`, equivalently `Q=0`. But the inverse from `(d,R,c)` to `(x,y,z)` has

    x=6c/(d^2-R).

Thus the entire ramification divisor lies at the boundary of the original affine source chart. This explains how a ramified finite cubic becomes an everywhere-etale polynomial map: the critical points are removed to infinity while their target image remains the nonproperness hypersurface.

At a generic point of `Q=0`, the depressed cubic factors as one simple root and one double root. The simple root yields the single finite preimage; the double-root pair has `d^2-R=0` and escapes. At the cusp `R=L=0`, all three roots lie on the boundary and the affine fiber is empty.

## 8. Geometry at infinity

The incidence variety in `C^3 x P^1` is a finite compactification over the target. It is superior to naive degree-seven homogenization of `F`, whose leading forms have a large base locus.

For the one-parameter slice `(a,0,0)` with `a=-s^2/4`, the two nonzero points in the earlier collision family are

    (x,y,z)=(+1/s,-3s/2,13s^2/2),
    (x,y,z)=(-1/s,+3s/2,13s^2/2).

Both approach `[1:0:0:0]` in ordinary projective `P^3`. In the chart `X=1`, their local coordinates satisfy

    Y/X=-3W^2/2,
    Z/X=13W^3/2,
    a=-W^2/4,

with `W=+s` and `W=-s`. Hence the two affine sheets are the two sides of one analytic branch at infinity, exchanged by a quadratic ramification over the target parameter `a`. This is the local projective shadow of the generic transposition along `Q=0`.

The nonproperness set is exactly `Q=0`, as proved in the cited manuscript by finiteness of the incidence projection off the discriminant and explicit escape arcs on it. This agrees with Jelonek's theorem that a nonempty nonproperness set for a generically finite polynomial self-map is a hypersurface.

## 9. What the third variable does

The evidence supports three distinct statements.

1. **Determinant compensator.** In `A+zB`, the `z` derivative supplies the third column `B`. Radial tangency removes the `z^2` coefficient, and the mixed `z` coefficient is canceled by the tailored derivatives of `A`. In the birational factorization, the same phenomenon becomes the exact cancellation `3q^3k * [-2/(3kq^3)]`.
2. **Auxiliary compatibility variable.** Once `(x,y)` and the target are constrained, `z` enforces the remaining compatibility; in the incidence reconstruction it is recovered rationally from a simple projective root.
3. **Not the branch label.** The branch label is the projective root `[x:1+xy]`, or the primitive element `d`. Distinct sheets do not correspond to freely chosen `z` values at fixed `(x,y)`.

For a two-variable polynomial map there is no third Jacobian column and no literal `A+zB` coefficient hierarchy. That comparison explains why this mechanism is intrinsically three-coordinate in its present form. It is not a proof that no different two-variable mechanism exists, and no such impossibility is claimed.

## 10. Structured generalization and rigidity

### 10.1 Exact same-degree family in the current literature

The same-day manuscript gives, for nonzero `lambda,alpha,gamma` and arbitrary `H(x,y)`, a family obtained from

    U=lambda+xy,
    W=gamma*z+H(x,y),
    Btilde=U^2W+[3/(alpha lambda^2)]y^2(4lambda+3xy),

and

    F1=U Btilde,
    F2=y+alpha x Btilde,
    F3=2x/lambda-3x^2y/lambda^2-(alpha/3)x^3W.

It proves

    det JF=-2 gamma lambda^2

and retains the cubic fiber geometry. Our SymPy script independently verifies this determinant for `H=0`. General `H` and `gamma` are induced by the triangular source change `z -> gamma z+H(x,y)`, so they are source-equivalent. The remaining parameters include rescalings; a complete quotient by affine conjugacy is not attempted here.

The same manuscript further gives polynomial deformations with every generic degree at least three while retaining the displayed three-point collision. Those formulas and their proof are cited, not independently reproduced in this bundle. Therefore the correct conclusion is that exact nontrivial families exist; the original map is not rigid under the broader natural structural constraints.

### 10.2 Pullback by a plane Keller pair

There is also a simple compositional family. Replace `(x,y)` in the original formula by a polynomial pair `(q(x,y),r(x,y))`. Exact chain rule gives

    det JF(q,r,z)=-2 det d(q,r)/d(x,y).

If `(q,r)` is a polynomial automorphism, this is merely source equivalence. A genuinely new example through a nonautomorphic constant-Jacobian plane pair would presuppose a counterexample to the two-dimensional conjecture, so this route gives no unconditional new inequivalent maps.

### 10.3 Rigidity triage

An unrestricted bounded-degree Gröbner rigidity search is no longer the decisive question because exact deformation families are known. Gauge perturbations `A -> A+gB` are always induced by `z -> z+g(x,y)`, and constant additions to `A` are target translations. Any future rigidity statement must first quotient these equivalences and must explicitly exclude the published higher-degree deformations.

## 11. Literature note

The closest source is the unsigned manuscript **A Counterexample to the Jacobian Conjecture**, dated 20 July 2026 and linked from the announcement. It studies the identical formula, proves the projective binary-cubic incidence model, classifies every fiber, determines the image and nonproperness set, and constructs exact families. These results are directly relevant and are incorporated with attribution.

Jelonek's 1993 theorem supplies the general hypersurface result for the nonproperness set. Bass–Connell–Wright remains a standard reference for reductions of the classical conjecture but does not anticipate this explicit mechanism.

Kulikov's older degree-three unramified morphism, discussed for example by Adjamagbo, is geometrically reminiscent because it is a nontrivial etale degree-three map from a rational affine surface to `C^2`. It is not the same kind of object: the source is not affine space, and no explicit algebraic equivalence to the present threefold map was found. The resemblance should therefore remain a literature analogy, not an identification.

## 12. Limitations and open directions

- A full resolution of the naive projective homogenization was not attempted. Its large base locus makes the binary-cubic incidence compactification the more efficient exact model.
- A broad Gröbner search for all bounded-degree completions `A` with fixed `B` was discontinued. Exact published families make unqualified rigidity false, and a meaningful search must quotient source and target equivalences first.
- No claim about the two-dimensional Jacobian conjecture is made.
- The current literature is changing on the same day as this report. Bibliographic attribution and priority should be rechecked before publication.

## 13. Conclusion

The most structurally informative results are the invariant bridge between the source cone and target discriminant data, the primitive coordinate d, the rational factorization F=Ψ∘Φ, and the finite cubic normal form whose ramification divisor is displaced to infinity. These calculations are presented as an independent structural analysis of the announced counterexample; rapidly developing same-day literature should be consulted for overlapping fiber classifications and deformation families. 

## 14. Reproduction

From the repository root, after installing the corresponding pinned
dependencies:

    python src/structural_sympy.py
    node src/verify_structural_nerdamer.js

The first script checks all displayed new polynomial and rational identities with exact SymPy arithmetic. The second independently checks the determinant, target cone identity, source pullbacks, and rational factorization in Nerdamer. Captured outputs are included.

## References

1. **A Counterexample to the Jacobian Conjecture**, unsigned manuscript dated 20 July 2026, linked at https://t.co/ywUCjGXFwm.
2. Z. Jelonek, *The set of points at which a polynomial map is not proper*, Ann. Polon. Math. 58 (1993), 259–266, https://eudml.org/doc/262458.
3. H. Bass, E. H. Connell, and D. Wright, *The Jacobian conjecture: reduction of degree and formal expansion of the inverse*, Bull. Amer. Math. Soc. 7 (1982), 287–330, https://doi.org/10.1090/S0273-0979-1982-15032-7.
4. K. Adjamagbo, *The complete solution to Bass Generalized Jacobian Conjecture*, arXiv:1210.5281, https://arxiv.org/abs/1210.5281.
5. The Stacks Project, Lemma 37.44.1 (proper and locally quasi-finite implies finite), Tag 0F2P, https://stacks.math.columbia.edu/tag/0F2P.
