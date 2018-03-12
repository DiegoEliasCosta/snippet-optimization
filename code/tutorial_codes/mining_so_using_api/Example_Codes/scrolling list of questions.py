import stackexchange as se

so = se.StackOverflow()

for q in so.questions(pagesize=50):
	print q.title
