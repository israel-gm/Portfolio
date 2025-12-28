# Generative Bayesian KDE

A custom **Bayesian classifier** powered by **Kernel Density Estimation (KDE)**.

Instead of assuming Gaussian distributions, this model estimates class-conditional densities non‑parametrically, generalizing Bayes’ rule for **multi‑class classification**.

$P(y|x)=\frac{P(x|y)P(y)}{\sum_{c'} P(x|c')P(c')}$

## 🔑 Highlights
- **Derivation notebook**: step‑by‑step math + custom KDE function.  
- **MNIST demo**: toy example showing digits classification in action.  
- **Generative twist**: posterior probabilities not only classify, but model the data distribution.
