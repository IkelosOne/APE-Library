def EuclideanAlgorithm(b, a):
	"""Returns the greatest common divisor of a and b using the Euclidean Algorithm.
	This function is also known as gcd() or hcf()."""

	if a == 0 or b == 0:
		if a == 0 and b == 0:
			return 0
		else:
			return 1
	if b % a != 0:
		return EuclideanAlgorithm(a, b % a)
	else:
		return a

def BezoutCoefficients(a, b):
	"""Generates two Bezout coefficients, s and t, satisfying Bezout's identity as + bt = gcd(a, b).
	Pseudocode from https://www.dcode.fr/bezout-identity

	N.B. doesn't work."""

	r1 = a
	r2 = b
	u1 = 1
	u2 = 0
	v1 = 0
	v2 = 1

	while r2 != 0:
		q = int(r1 / r2)
		rs = r1
		us = u1
		vs = v1
		r = r2
		u = u2
		v = v2
		r2 = rs - q * r2
		u2 = us - q * u2
		v2 = vs - q * v2
	return r, u, v

def Gamma(a):
	"""Generalised factorial. The function Γ such that Γ(α + 1) = αΓ(α). Takes any real number greater than 0."""

	if a > 1:
		return a * Gamma(a - 1)
	else:
		return a


if __name__ == "__main__":
	print(Gamma(10))
