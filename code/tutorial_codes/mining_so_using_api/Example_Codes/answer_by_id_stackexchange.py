import stackexchange as se

so = se.StackOverflow()

u = so.user(41981)
qs = u.questions
qs = u.questions.fetch()

print qs
