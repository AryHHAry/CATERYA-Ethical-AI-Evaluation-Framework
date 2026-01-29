# Mathematical Foundations of CATERYA

**Created and maintained by Ary HH (aryhharyanto@proton.me)**

---

## Introduction

CATERYA treats AI trustworthiness as a measurable physical quantity, subject to mathematical laws analogous to those governing energy, entropy, and information in physics. This document provides rigorous mathematical formulations for our core metrics.

**Design Philosophy**: Every metric must be:
1. **Quantifiable**: Produces numerical scores with defined ranges
2. **Reproducible**: Same inputs yield same outputs (deterministic)
3. **Bounded**: Scores have interpretable limits
4. **Theoretically Grounded**: Connected to established mathematical principles

---

## Core Framework: Trust as a Hamiltonian

### Definition

We model AI trust as a Hamiltonian system where ethical properties are conserved quantities under ideal conditions.

**Trust Hamiltonian**:
```
H_trust = T_ethical + V_bias + U_opacity
```

Where:
- **T_ethical**: "Kinetic" energy representing the system's capacity for ethical adaptation
- **V_bias**: "Potential" energy representing bias wells that trap the system
- **U_opacity**: "Interaction" energy representing opacity costs

**Interpretation**: An AI system in a high-trust state minimizes H_trust, analogous to physical systems minimizing total energy.

---

## Pillar 1: Bias & Fairness (Energy Landscape)

### 1.1 Fairness Energy Map

**Concept**: Bias creates "energy wells" in the decision landscape. Fair systems occupy low-energy, stable states.

**Mathematical Formulation**:

For a model producing predictions **ŷ** for groups **g ∈ G**:

```
E_fairness(g) = -log P(fair | g) + λ · KL(P(ŷ|g) || P(ŷ))
```

Where:
- **P(fair | g)**: Probability of fair treatment for group g
- **KL(·||·)**: Kullback-Leibler divergence measuring distribution mismatch
- **λ**: Regularization parameter balancing local vs. global fairness
- **P(ŷ)**: Marginal distribution (averaged across groups)

**Total Fairness Energy**:
```
E_total = Σ_g n_g · E_fairness(g)
```

where **n_g** is the population proportion of group g.

**Bounds**: E_fairness ∈ [0, ∞), with 0 = perfect fairness

---

### 1.2 Symmetry Index

**Concept**: Fairness as symmetry. Breaking symmetry across groups indicates bias.

**Mathematical Formulation**:

For metric **M** (accuracy, precision, etc.) computed per group:

```
S_index = 1 - σ(M_g) / μ(M_g)
```

Where:
- **σ(M_g)**: Standard deviation of metric across groups
- **μ(M_g)**: Mean of metric across groups

**Alternative (Entropy-Based)**:
```
S_entropy = H(M_g) / H_max
```

Where **H(M_g) = -Σ_g P(g) log P(M_g)** and **H_max = log|G|**

**Bounds**: S_index ∈ [0, 1], where 1 = perfect symmetry

**Physical Analogy**: Like rotational symmetry in physics, ethical systems should be invariant under group relabeling.

---

### 1.3 Ethical Energy Score

**Concept**: Combines computational cost, bias magnitude, and societal impact into unified energy metric.

**Mathematical Formulation**:

```
E_ethical = α·E_compute + β·E_bias + γ·E_impact
```

**Components**:

1. **Computational Energy**:
```
E_compute = (FLOPs · kWh_per_FLOP) / efficiency_baseline
```

2. **Bias Energy** (from Fairness Energy Map):
```
E_bias = E_total (from 1.1)
```

3. **Impact Energy** (societal harm potential):
```
E_impact = Σ_i w_i · harm_score_i
```

Where **w_i** are stakeholder-defined weights for harm categories (privacy, discrimination, misinformation, etc.)

**Normalization**:
```
E_ethical_normalized = E_ethical / (α + β + γ)
```

**Bounds**: E_ethical ∈ [0, 1] after normalization, lower is better

---

## Pillar 2: Interpretability (Information Principle)

### 2.1 Information Authenticity

**Concept**: Distinguish genuine understanding (high mutual information with semantics) from surface pattern matching (low mutual information).

**Mathematical Formulation**:

```
I_authentic = I(X; Y | C) / H(Y | C)
```

Where:
- **X**: Model internal representations
- **Y**: True semantic concepts
- **C**: Context information
- **I(·;·|·)**: Conditional mutual information
- **H(·|·)**: Conditional entropy

**Practical Estimation**:

Using SHAP values or attention weights as proxy for model representations:

```
I_authentic ≈ (Σ_i SHAP_i · relevance_i) / Σ_i |SHAP_i|
```

Where **relevance_i** measures how much feature i relates to true semantic meaning (human-annotated or via proxy tasks).

**Bounds**: I_authentic ∈ [0, 1], where 1 = perfect semantic alignment

---

### 2.2 Ethical Coherence Score

**Concept**: Stability of ethical reasoning under pressure (adversarial, business, technical constraints).

**Mathematical Formulation**:

For a model producing ethical judgments **e** under conditions **c**:

```
C_ethical = 1 - (1/|Δc|) Σ_Δc ||e(c + Δc) - e(c)|| / ||e(c)||
```

Where:
- **Δc**: Perturbations representing pressures (e.g., profit optimization, adversarial attacks)
- **||·||**: Norm measuring distance between ethical states

**Robustness Version**:

```
C_robust = min_Δc∈B_ε { similarity(e(c), e(c + Δc)) }
```

Where **B_ε** is a ball of perturbations with magnitude ε.

**Bounds**: C_ethical ∈ [0, 1], where 1 = perfect coherence

---

### 2.3 Feynman Test Score

**Concept**: Can the AI explain its reasoning simply? Inspired by Feynman's "If you can't explain it simply, you don't understand it."

**Mathematical Formulation**:

```
F_score = comprehensibility · correctness · completeness
```

**Components**:

1. **Comprehensibility** (readability):
```
comprehensibility = 1 / (1 + complexity(explanation))
```

Using Flesch-Kincaid or other readability metrics.

2. **Correctness**:
```
correctness = agreement(explanation, ground_truth_reasoning)
```

3. **Completeness**:
```
completeness = coverage(explanation, necessary_concepts)
```

**Practical Implementation**:

Generate natural language explanation, evaluate with:
- Human raters (gold standard)
- LLM-as-judge (scalable proxy)
- Automatic metrics (ROUGE, BLEU, BERTScore)

**Bounds**: F_score ∈ [0, 1], where 1 = perfect explanation

---

## Pillar 3: Robustness (Stability Principle)

### 3.1 Ethical Horizon Map

**Concept**: Analogous to black hole event horizons—beyond which ethical properties cannot escape.

**Mathematical Formulation**:

Define ethical state space **E** with metric **d_E**. The ethical horizon is:

```
H_ethical = {x ∈ E : ∃ perturbation δ, ||δ|| < ε ⇒ ethical_violation(x + δ)}
```

**Distance to Horizon**:
```
d_horizon(x) = min_h∈H d_E(x, h)
```

**Horizon Curvature** (how quickly ethics degrade):
```
κ_horizon = ∇²_x d_horizon(x)
```

**Visualization**: Plot **d_horizon** as height map, revealing "cliffs" where small changes cause ethical collapse.

**Bounds**: d_horizon ∈ [0, ∞), larger is safer

---

### 3.2 Ethical Gradient Analysis

**Concept**: Rate of ethical decay under adversarial conditions.

**Mathematical Formulation**:

For ethical metric **M** and perturbation **ε**:

```
G_ethical = ||∇_ε M(x + ε)||
```

**Adversarial Robustness**:

```
R_adversarial = min_||ε||<δ M(x + ε) / M(x)
```

Where **δ** is attack budget (e.g., L∞ norm bound).

**Lipschitz Constant** (global stability):

```
L_ethical = sup_{x≠y} ||M(x) - M(y)|| / ||x - y||
```

Lower Lipschitz constant = more stable ethics.

**Bounds**: G_ethical ∈ [0, ∞), lower is better; R_adversarial ∈ [0, 1], higher is better

---

### 3.3 Human Constant Stability

**Concept**: Like physical constants (c, ℏ, G), human values should remain stable across AI interactions.

**Mathematical Formulation**:

Define "human constant" **h** (e.g., respect for autonomy, privacy, fairness). Measure drift:

```
S_human = 1 - Var_t(h_t) / h_0²
```

Where:
- **h_t**: Human value at time t (measured via user surveys, behavior analysis)
- **h_0**: Baseline value
- **Var_t**: Variance over time

**Long-Term Stability**:

```
S_long-term = exp(-λ · t) · S_human(0)
```

Where **λ** is decay rate. Ethical AI maintains **λ → 0**.

**Bounds**: S_human ∈ [0, 1], where 1 = perfect stability

---

## Pillar 4: Transparency & Accountability (Entanglement)

### 4.1 Provenance Metrics

**Concept**: Every AI output is "entangled" with its origins. Measure traceability.

**Mathematical Formulation**:

**Data Lineage Score**:
```
L_data = |traced_samples| / |total_training_samples|
```

**Model Card Completeness**:
```
C_model = Σ_i w_i · present(field_i)
```

Where **w_i** are importance weights for model card fields (architecture, training data, limitations, etc.)

**Accountability Audit Trail**:
```
A_audit = log₂(|decision_points_logged|) / log₂(|decision_points_total|)
```

**Output Provenance** (C2PA-style):

For generated content **o**, compute cryptographic hash linking to:
- Model ID and version
- Input data hash
- Generation timestamp
- Parameters used

```
P_output = 1 if provenance_verified(o) else 0
```

**Aggregate Provenance Score**:
```
P_total = (L_data + C_model + A_audit + P_output) / 4
```

**Bounds**: All components ∈ [0, 1]

---

### 4.2 Moral Curvature

**Concept**: Ethical frameworks "curve" differently across cultures, like spacetime curves in general relativity.

**Mathematical Formulation**:

Define ethical value vector **v** in moral space **M**. Curvature measures how **v** changes across contexts:

```
K_moral = ∇²_c v(c)
```

Where **c** represents cultural/contextual coordinates.

**Ricci Curvature** (aggregate moral geometry):

```
R_moral = Σ_i K_ii
```

Positive curvature: Values converge (universal ethics).  
Negative curvature: Values diverge (relativistic ethics).

**Practical Estimation**:

Survey ethical judgments across **n** cultures for scenario **s**:

```
K_moral ≈ σ(judgments) / μ(judgments)
```

High curvature = high contextual sensitivity needed.

**Bounds**: K_moral ∈ [0, ∞), interpretation depends on use case

---

### 4.3 Contextual Ethics Simulator

**Concept**: Test AI decisions across diverse contexts to reveal hidden assumptions.

**Mathematical Formulation**:

For decision function **f** and context set **C = {c₁, c₂, ..., c_n}**:

**Consistency Score**:
```
CS = (1/|C|²) Σ_{i,j} similarity(f(x, c_i), f(x, c_j))
```

**Adaptation Score**:
```
AS = (1/|C|) Σ_i correctness(f(x, c_i), ground_truth_i)
```

**Trade-off**:

Ideal system balances consistency (not erratic) with adaptation (not rigid):

```
Balance = 2·CS·AS / (CS + AS)   [Harmonic mean]
```

**Bounds**: CS, AS, Balance ∈ [0, 1]

---

## Advanced Concepts

### Entropy-Symmetry-Information Triangle

**Concept**: Three fundamental quantities in tension.

**Mathematical Formulation**:

```
H (Entropy) = -Σ_i p_i log p_i         [Diversity]
S (Symmetry) = 1 - σ(M_g) / μ(M_g)     [Fairness]
I (Information) = I(X; Y)               [Understanding]
```

**Golden Triangle Zone**:

Optimal region defined by:
```
(H, S, I) ∈ [H_min, H_max] × [S_min, 1] × [I_min, 1]
```

Where thresholds are application-specific.

**Distance from Ideal**:
```
D_ideal = ||[H, S, I] - [H*, S*, I*]||₂
```

---

### Meaningful Scaling Index (MSI)

**Concept**: Does increasing model size improve ethics proportionally?

**Mathematical Formulation**:

For model size **N** (parameters) and ethical metric **M**:

```
MSI = d log M / d log N
```

**Interpretation**:
- **MSI > 1**: Super-linear improvement (scaling helps ethics)
- **MSI = 1**: Linear scaling (proportional improvement)
- **MSI < 1**: Sub-linear (diminishing returns)
- **MSI < 0**: Inverse scaling (larger models are less ethical—problematic!)

**Practical Estimation**:

Fit power law **M(N) = aN^b**, then **MSI = b**.

---

### Quantum-Inspired Learning Metrics

**Concept**: Coherence of semantic understanding, inspired by quantum coherence.

**Mathematical Formulation**:

Model knowledge as density matrix **ρ** in concept space:

```
ρ = Σ_i λ_i |ψ_i⟩⟨ψ_i|
```

**Coherence** (off-diagonal elements):
```
Γ = Σ_{i≠j} |ρ_ij|
```

High coherence = concepts are entangled (relational understanding).  
Low coherence = concepts are isolated (memorization).

**Purity**:
```
P = Tr(ρ²)
```

**Bounds**: Γ ∈ [0, ∞), P ∈ [1/n, 1] where n = dimension of concept space

---

## CATERYA Open Score: Unified Metric

**Concept**: Aggregate trustworthiness score combining all pillars.

**Mathematical Formulation**:

```
CATERYA_Score = f(P₁, P₂, P₃, P₄)
```

Where **P_i** are pillar scores (Bias, Interpretability, Robustness, Transparency).

**Option 1: Weighted Arithmetic Mean**
```
Score = Σ_i w_i · P_i, where Σ_i w_i = 1
```

**Option 2: Geometric Mean** (penalizes weak pillars)
```
Score = (Π_i P_i)^(1/4)
```

**Option 3: Harmonic Mean** (most conservative)
```
Score = 4 / (Σ_i 1/P_i)
```

**Recommendation**: Use geometric mean for balanced evaluation.

**Normalization**: Scale to [0, 100] for interpretability.

```
CATERYA_Score_100 = 100 · (Π_i P_i)^(1/4)
```

**Interpretation**:
- 90-100: Excellent trustworthiness
- 70-89: Good, minor improvements needed
- 50-69: Moderate concerns, significant improvements needed
- 30-49: Poor, major ethical issues
- 0-29: Critical failures, do not deploy

---

## Lagrangian-Inspired Optimization

**Concept**: Optimize model performance subject to ethical constraints.

**Mathematical Formulation**:

```
L(θ) = Loss(θ) + Σ_i λ_i · Constraint_i(θ)
```

Where:
- **Loss(θ)**: Standard ML loss (cross-entropy, MSE, etc.)
- **Constraint_i**: Ethical constraints (fairness, robustness, etc.)
- **λ_i**: Lagrange multipliers (penalty weights)

**Ethical Constraints**:

1. **Fairness**: `C_fairness = |E_g1 - E_g2|` (energy gap between groups)
2. **Robustness**: `C_robust = max_ε L(θ, x+ε) - L(θ, x)`
3. **Interpretability**: `C_interp = -I(X; Y)` (negative mutual information)

**Optimization**:
```
θ* = argmin_θ L(θ)
```

**Adaptive Multipliers**:

Update **λ_i** based on constraint violations:
```
λ_i ← λ_i + η · max(0, Constraint_i - threshold_i)
```

---

## Theoretical Bounds & Proofs

### Theorem 1: Fairness Energy Lower Bound

**Statement**: For any classifier, **E_fairness ≥ 0**, with equality iff predictions are group-independent.

**Proof**:

By definition, **KL(P||Q) ≥ 0** with equality iff **P = Q**.  
Thus, **KL(P(ŷ|g) || P(ŷ)) = 0** iff **P(ŷ|g) = P(ŷ)** (demographic parity).  
Since **-log P(fair|g) ≥ 0** (probability ≤ 1), we have **E_fairness ≥ 0**. ∎

---

### Theorem 2: Symmetry Index Bounds

**Statement**: **0 ≤ S_index ≤ 1**.

**Proof**:

By definition, **S_index = 1 - σ/μ**.  
Since **σ ≥ 0** and **μ > 0** (assuming non-degenerate metrics), we have **σ/μ ≥ 0**.  
When **σ = 0** (all groups identical), **S_index = 1**.  
As **σ/μ → ∞**, **S_index → -∞** (but we clip to 0 in practice).  
Therefore, **S_index ∈ [0, 1]** after clipping. ∎

---

### Theorem 3: Information Authenticity Monotonicity

**Statement**: **I_authentic** increases monotonically with mutual information **I(X; Y)**.

**Proof**:

**I_authentic = I(X; Y | C) / H(Y | C)**.  
Since **I(X; Y | C) ≤ H(Y | C)** (mutual information bounded by entropy), increasing **I(X; Y | C)** directly increases **I_authentic**.  
By chain rule of mutual information, this holds. ∎

---

## Implementation Notes

### Computational Complexity

| Metric | Time Complexity | Space Complexity |
|--------|-----------------|------------------|
| Fairness Energy | O(n · |G|) | O(n) |
| Symmetry Index | O(n · |G|) | O(|G|) |
| Information Authenticity | O(n · d · k) | O(n · d) |
| Ethical Horizon | O(n² · d) | O(n) |
| Provenance | O(n · log n) | O(n) |

Where:
- **n**: Number of samples
- **|G|**: Number of groups
- **d**: Feature dimensionality
- **k**: Number of semantic concepts

### Numerical Stability

**Issue**: Log of small probabilities causes underflow.

**Solution**: Use log-space arithmetic:
```python
import numpy as np
log_p = np.log(p + 1e-10)  # Add epsilon for stability
```

**Issue**: Division by zero when **μ → 0**.

**Solution**: Add regularization:
```python
symmetry_index = 1 - sigma / (mu + 1e-6)
```

---

## References

This framework draws from:

1. **Information Theory**: Shannon entropy, mutual information, KL divergence
2. **Statistical Mechanics**: Energy landscapes, partition functions, phase transitions
3. **Differential Geometry**: Curvature, geodesics, metric spaces
4. **Quantum Mechanics**: Density matrices, coherence, entanglement (as analogy)
5. **Optimization Theory**: Lagrangian multipliers, convex optimization, constraint satisfaction

---

## Future Directions

1. **Renormalization Group**: Coarse-graining ethics across scales (individual predictions → model behavior → societal impact)
2. **Conservation Laws**: Identify ethical quantities conserved during training
3. **Phase Transitions**: Detect sudden changes in ethical properties (scaling laws)
4. **Universality Classes**: Categorize AI systems by ethical behavior patterns
5. **Topological Ethics**: Use algebraic topology to characterize ethical structures

---

*"Mathematics is the language in which the universe is written. Ethics, too, can be written in this language."*

**— Ary HH**

---

**Document Version**: 1.0  
**Last Updated**: January 2026  
**Next Review**: July 2026
