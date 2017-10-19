import syft


def Paillier(n_length=1024):
    return syft.he.paillier.keys.KeyPair().generate(n_length)

def BV(n_length=2048, q=61, t=2030, sigma=8):
	return syft.he.bv.keys.KeyPair().generate(n_length, q, t, sigma)
