from stackapi import StackAPI
SITE = StackAPI('stackoverflow')
comments = SITE.fetch('answers')

print comments
