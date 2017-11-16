import stackexchange

# Get the Stack Overflow context
so = stackexchange.Site(stackexchange.StackOverflow)
so.be_inclusive()

question = so.question(14984119)

print('--- %s ---' % question.title)
print(question.body)
print()
print('%d answers.' % len(question.answers))

for answer in question.answers:

    print(answer.body)

