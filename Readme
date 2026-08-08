# Theseus 24-Bit Cryptographic Core

An experimental reversible 24-bit permutation architecture designed for exhaustive analysis across the complete state space.

The project explores a compact cryptographic transformation built around:

- Reversible integer transformations
- Modular arithmetic
- Nonlinear substitution
- Bit-level diffusion
- Differential propagation
- Walsh-spectrum behavior
- Structural properties
- Exact forward/inverse round-trip verification

The primary engineering requirement is simple:

> Every valid 24-bit input must map to exactly one unique 24-bit output, and the inverse transformation must recover the original input exactly.

## State Space

The core operates on:

```text
2^24 = 16,777,216 states
```

Because the state space is finite and computationally manageable, the complete permutation can be exhaustively evaluated rather than relying exclusively on statistical sampling.

## Design Goals

The Theseus core is being developed around four primary goals:

1. **Exact reversibility**  
   Every transformation must have a mathematically defined inverse.

2. **Strong diffusion**  
   Small input changes should propagate rapidly throughout the 24-bit state.

3. **Nonlinear behavior**  
   The transformation should resist simple linear and differential descriptions.

4. **Exhaustive verification**  
   Security-relevant properties should be tested across all 16,777,216 possible inputs whenever computationally practical.

## Repository Structure

```text
theseus-24bit-cryptographic-core/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── src/
│   └── theseus_core.py
│
├── tests/
│   ├── test_permutation.py
│   ├── test_inverse.py
│   └── test_roundtrip.py
│
├── analysis/
│   ├── differential.py
│   ├── walsh_spectrum.py
│   └── structural.py
│
├── docs/
│   └── RC1_EVALUATION.md
│
└── requirements.txt
```

## Verification Strategy

The evaluation framework is intended to test:

- Full-codebook permutation uniqueness
- Forward/inverse round-trip correctness
- Differential propagation
- Bit-level avalanche behavior
- Walsh-spectrum correlation
- Structural invariants
- Cycle behavior
- Fixed points
- Round-dependent diffusion

The strongest correctness test is exhaustive:

```python
for x in range(1 << 24):
    assert inverse(forward(x)) == x
```

Passing this test verifies exact round-trip recovery for every state in the complete 24-bit domain.

## Cryptanalytic Evaluation

The repository includes dedicated analysis modules for examining the transformation independently of the core implementation.

### Differential Analysis

`analysis/differential.py`

Evaluates how controlled input differences propagate through the permutation across increasing round counts.

### Walsh-Spectrum Analysis

`analysis/walsh_spectrum.py`

Measures linear correlation behavior and searches for statistically significant linear structure.

### Structural Analysis

`analysis/structural.py`

Examines properties including fixed points, invariant structures, cycle behavior, and other algebraic characteristics.

## RC1 Evaluation

Formal evaluation targets and experimental results are maintained in:

```text
docs/RC1_EVALUATION.md
```

Results should be treated as experimental until independently reproduced and reviewed.

## Important Security Notice

This repository contains **experimental cryptographic research**.

It has not been established as a production-grade encryption primitive and should not be used to protect sensitive information without extensive independent cryptanalysis, peer review, and security validation.

The purpose of this repository is to make the design reproducible, testable, falsifiable, and open to independent evaluation.

## Reproducibility

A central principle of the Theseus project is:

> Do not trust the claim. Run the test.

Implementations, evaluation scripts, and test vectors should provide enough information for independent researchers to reproduce or challenge every significant result.

## Status

**Research / Experimental**

Current work focuses on:

- Reference implementation
- Exhaustive permutation verification
- Differential analysis
- Walsh-spectrum analysis
- Structural evaluation
- Independent reproducibility

## License

Released under the MIT License.

See `LICENSE` for details.
