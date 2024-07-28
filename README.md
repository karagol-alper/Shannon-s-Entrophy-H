# Shannon-s-Entrophy-H

This tool computes Shannon's entropy, providing a measure of genetic diversity within a sequence [1]. It can be used to quantify the diversity of genetic sequences within a population or the diversity of species within an ecosystem [2]. 

For a discrete random variable X with possible values {x₁, ..., xₙ} and probability mass function P(X), the Shannon entropy H(X) is defined as:
H(X) = -∑ P(xᵢ) * log₂(P(xᵢ))
where the sum is over all possible values of X. 

The calculateSequenceEntropy(sequence) implements this formula. It calculates the probability of each character by dividing its count by the total sequence length. Finally, it computes the entropy using the formula:
entropy = -∑ pᵢ * log₂(pᵢ)
where pᵢ is the probability of each unique character in the sequence.

1)	Shannon, C.E. (1948) A Mathematical Theory of Communication. Bell System Technical Journal, 27, 379-423. http://dx.doi.org/10.1002/j.1538-7305.1948.tb01338.x
2)	Daly, A. J., Baetens, J. M., & De Baets, B. (2018). Ecological diversity: measuring the unmeasurable. Mathematics, 6(7), 119.


# Please cite:
1)	Shannon, C.E. (1948) A Mathematical Theory of Communication. Bell System Technical Journal, 27, 379-423. http://dx.doi.org/10.1002/j.1538-7305.1948.tb01338.x
