def hyperplaneFitViaTls(data):
	from numpy.linalg import eig
	import numpy as np

	ans = []
	x = np.array(data)

	m = np.mean(x, axis = 1).reshape(-1,1)
	# print(m)
	c = x - m
	# print(c)
	v = np.cov(c)

	values, vectors = eig(v)
	s = np.argmin(values)

	tmp = vectors[:, s]
	# print(tmp)

	p = tmp.dot(m)
	# p = np.dot(tmp, m)
	p *= -1
	# print(p)

	tmp = np.append(tmp, p)

	if tmp[0] < 0:
		tmp *= -1

	# print(tmp)

	

	return tmp

def main():
    def Load_Coordinates(n_dim):
        data = [[float(val) for val in input().split()] for i in range(n_dim)]
        return data

    for _ in range(10):
        n_dim = int(input())
        data = Load_Coordinates(n_dim)
        params = hyperplaneFitViaTls(data)
        print(*params)

if __name__ == '__main__':
    main()


	# print(data)
	# print(x)

	# for i in range(len(data)):
	# 	data[i] = data[i] - np.mean(data[i])
	# 	v[i] = np.cov(data[i].T)	x = np.array([data])

	# print(data)
	# m = np.mean(data, axis = 1)
	# print(m)
	# c = data - m
	# print(type(c))
	# v = cov(c)

	# values, vectors = eig(v.T)
	# ans.append(vectors.dot(c))