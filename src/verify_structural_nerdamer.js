#!/usr/bin/env node
// Independent exact checks in Nerdamer 1.1.13.
const nerdamer = require('nerdamer/all');

function simp(s) { return nerdamer(`simplify(${s})`).toString(); }
function assertZero(name, s) {
  const got = simp(s);
  if (got !== '0') throw new Error(`${name}: ${got}`);
  console.log(`${name}: 0`);
}

const u='(1+x*y)';
const F1=`${u}^3*z+y^2*${u}*(4+3*x*y)`;
const F2=`y+3*x*${u}^2*z+3*x*y^2*(4+3*x*y)`;
const F3='2*x-3*x^2*y-x^3*z';
const d=(f,v)=>`diff(${f},${v})`;
const det3=(a11,a12,a13,a21,a22,a23,a31,a32,a33)=>
 `(${a11})*((${a22})*(${a33})-(${a23})*(${a32}))-(${a12})*((${a21})*(${a33})-(${a23})*(${a31}))+(${a13})*((${a21})*(${a32})-(${a22})*(${a31}))`;
const jac = det3(d(F1,'x'),d(F1,'y'),d(F1,'z'),d(F2,'x'),d(F2,'y'),d(F2,'z'),d(F3,'x'),d(F3,'y'),d(F3,'z'));
assertZero('detJF+2',`(${jac})+2`);

const Q='27*a^2*c^2-18*a*b*c+16*a+b^3*c-b^2';
const R='4-3*b*c';
const L='27*a*c^2-9*b*c+8';
assertZero('target cone bridge',`(${R})^3+27*(${Q})*c^2-(${L})^2`);

const k='2-3*x*y-x^2*z';
const delta=`3*(${k})*${u}-2`;
const pull=(expr)=>nerdamer(expr,{a:F1,b:F2,c:F3}).toString();
assertZero('R pullback',`(${pull(R)})-((${delta})^2-6*(${k}))`);
assertZero('x^2 Q pullback',`x^2*(${pull(Q)})-(8*(${k})-(${delta})^2)`);
assertZero('L pullback',`(${pull(L)})-(${delta})*(9*(${k})-(${delta})^2)`);

const q='q', K='K', D='D';
const psi1=`-(${D}+2)*(${D}^2+${D}-9*${K}-2)/(27*${K}^2*${q}^2)`;
const psi2=`-(${D}^2-6*${K}-4)/(3*${K}*${q})`;
const psi3=`${K}*${q}`;
assertZero('factorization F1',`(${psi1.replaceAll('q','x').replaceAll('K',`(${k})`).replaceAll('D',`(${delta})`)})-(${F1})`);
assertZero('factorization F2',`(${psi2.replaceAll('q','x').replaceAll('K',`(${k})`).replaceAll('D',`(${delta})`)})-(${F2})`);
assertZero('factorization F3',`(${psi3.replaceAll('q','x').replaceAll('K',`(${k})`).replaceAll('D',`(${delta})`)})-(${F3})`);
console.log('all Nerdamer assertions passed');
