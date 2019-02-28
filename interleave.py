def interleave(s1,s2):
	pairs = list(zip(s1,s2))
	jpairs =[''.join(p) for p in pairs]
	print(''.join(jpairs))

interleave("hello", "there")