import numpy as np
import matplotlib.pyplot as plt
# from scipy.stats import norm
import math

def normpdf(x, mu, sigma):
	#for some reason norm kept breaking on my computer
    u = (x-mu)/abs(sigma)
    y = (1/(math.sqrt(2*math.pi)*abs(sigma)))*math.exp(-u*u/2)
    return y

def opt_build_powerlaw_joint(tobs):
	"""
		returns an (anonymous) procedure of one argument - ttotal - that
		computes the joint density evaluated on that argument and tobs.

		TODO: construct and return anonymous procedure
	"""

	# [...]

	if tobs >= x:
		return lambda x: 0 

	else:
		return math.pow(x, -2.43)/x



def opt_build_lifespan_joint(tobs):
	"""
		TODO: model after build_powerlaw_joint
	"""

	# [...]

	if tobs >= x:
		return lambda x: 0 
	else:
		return norm.pdf(x, 75, 16)/x



def opt_compute_posterior(joint, theta_min, theta_max, num_steps):
	"""
		Computes a table representation of the posterior distribution
		with at most num_steps joint density evaluations, covering the
		range from theta_min to theta_max.

		People interested in fancier integrators should feel free to
		modify the signature for this procedure, as well as its callers,
		as appropriate.

		TODO: compute Z along with an unnormalized table

		TODO: normalize joint

	"""

    postvals = []
    thetavals = []
    Z = 0

    step = int((theta_max-theta_min)/num_steps)
    for i in range(theta_min+step, theta_max, step): #i is ttotal
        thetavals.append(i)
        out = joint(i)
        postvals.append(out)
        Z += step*out

    for i in range(len(postvals)):
        postvals[i] /= Z

    return (thetavals, postvals)
