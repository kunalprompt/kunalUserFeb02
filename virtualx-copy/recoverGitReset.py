f_file = open('allhashes', 'r').readlines()
commits = []
for i in f_file:
	commit_id = str(i.split()[2])
	commits.append(commit_id)
#print commits

from subprocess import call

filename = "file"

i = 1

for c in commits:
    f = open(filename + str(i),"wb")
    call(["git", "show", c],stdout=f)
    i+=1
print i