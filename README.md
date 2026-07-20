# Structural investigation of the three-sheeted Jacobian counterexample

This repository contains an exact symbolic follow-up analysis of the recently
announced three-dimensional Jacobian counterexample.

The report studies the map's determinant mechanism, cubic-cone structure,
generic Galois and monodromy behavior, birational factorization, and the way
ramification is displaced to infinity.

This is an independent reproducible follow-up analysis, not an author-supplied
derivation or a claim of priority for the original counterexample.

- [Read the PDF report](report/structural_jacobian_followup_report.pdf)
- [Read the Markdown report](report/technical_report.md)

## Main findings

- A universal determinant criterion is derived for maps of the form
  `F(x,y,z) = A(x,y) + zB(x,y)`.
- The displayed `B` factors through a homogeneous cubic cone.
- The generic function-field extension has Galois closure group `S3`.
- The map admits an exact rational factorization with reciprocal Jacobian
  factors.
- After a birational target change, the map becomes a finite cubic whose
  ramification divisor lies outside the original affine source chart.
- The nonproperness hypersurface is interpreted as the target image of that
  displaced ramification.
- Same-day literature results concerning complete fiber classification and
  deformation families are separated and attributed.

## Provenance and scope

The cone, invariant, discriminant, Galois, and birational-factorization
identities are exact calculations checked by the scripts in this repository.
The complete incidence-fiber theorem and arbitrary-degree deformation family
overlap with or are imported from same-day literature and are labeled as such
in the report. Captured exact outputs from both verification paths are included.

Priority and overlap should be interpreted relative to the public sources
located on 20 July 2026. The literature was developing rapidly, and no claim
of exhaustive literature coverage is made.

## Python verification

The Python and Node checks are independent verification paths; either can be
run without running the other.

### macOS/Linux

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python src/structural_sympy.py
```

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python src/structural_sympy.py
```

The run should end with `all exact assertions passed`. Its substantive output
can be compared with [`output/exact_output_sympy.txt`](output/exact_output_sympy.txt).

## Independent Node verification

Direct command:

```bash
npm ci
node src/verify_structural_nerdamer.js
```

Or use the package script:

```bash
npm ci
npm run verify
```

Both routes should end with `all Nerdamer assertions passed`. Their output can
be compared with
[`output/exact_output_nerdamer.txt`](output/exact_output_nerdamer.txt).

## Repository contents

- `report/technical_report.md` — full technical report in Markdown.
- `report/structural_jacobian_followup_report.pdf` — formatted public report.
- `report/structural_jacobian_followup_report.docx` — editable report.
- `src/structural_sympy.py` — primary exact symbolic verification.
- `src/verify_structural_nerdamer.js` — independent symbolic verification.
- `output/exact_output_sympy.txt` — captured primary output.
- `output/exact_output_nerdamer.txt` — captured independent output.
- `requirements.txt` — pinned Python dependencies.
- `package.json` and `package-lock.json` — pinned Node dependency metadata.
- `environment.txt` — recorded provenance and concise reproduction commands.
- `LICENSE` — MIT license for this repository.

No floating-point result is used as proof.

## Acknowledgments

Special thanks to Levent Alpöge, Akhil Mathew, and the team at Anthropic. The three-dimensional polynomial map studied in this repository was originally discovered by Anthropic’s Claude Fable 5 and publicly announced by Levent Alpöge on July 20, 2026.

This repository also draws on A COUNTEREXAMPLE TO THE JACOBIAN CONJECTURE ([Link](https://www.ulam.ai/research/jacobian.pdf)) analyzing the identical map, particularly for the projective-root incidence model, complete fiber classification, and higher-degree deformation families. Those imported results are explicitly identified and attributed in the report.

The structural calculations, exact symbolic verification, literature comparison, and drafting of the technical report were carried out by OpenAI’s GPT-5.6 Sol operating through the ChatGPT Work agent.

My role was to formulate the research questions, design and refine the investigation, supervise the agent’s progress, distinguish original calculations from same-day literature results, review the mathematical claims and presentation, and prepare the final repository for public release.

## License

Released under the [MIT License](LICENSE).
