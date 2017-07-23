
# open the file - and read all of the lines.
changes_file = 'changes_python.log'
# use strip to strip out spaces and trim the line.

#my_file = open(changes_file, 'r')
#data = my_file.readlines()

data = [line.strip() for line in open(changes_file, 'r')]

# print the number of lines read
print(len(data))

sep = 72*'-'

# create the commit class to hold each of the elements 
class Commit:
    'class for commits'
   
    def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment
		

    def get_commit_comment(self):
        return 'svn merge -r' + str(self.revision-1) + ':' + str(self.revision) + ' by ' \
                + self.author + ' with the comment ' + ','.join(self.comment) \
                + ' and the changes ' + ','.join(self.changes)

				
def average_commits(commits,authors): 
		
	return len(commits) / len(authors) 
	

def maximum(commits_author): 
	
	return max(commits_author)


def dates_min(dates):
	
	return min(dates)


def dates_max(dates): 

	return max(dates)

	
commits = []
current_commit = None
index = 0

author = {}
while True:
    try:
		# parse each of the commits and put them into a list of commits
		current_commit = Commit()
		details = data[index + 1].split('|')
		current_commit.revision = int(details[0].strip().strip('r'))
		current_commit.author = details[1].strip()
		current_commit.date = details[2].strip()
		current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
		current_commit.changes = data[index+2:data.index('',index+1)]
		#print(current_commit.changes)
		index = data.index(sep, index + 1)
		current_commit.comment = data[index-current_commit.comment_line_count:index]
		commits.append(current_commit)
		
    except IndexError:
        break
	
#create functions useful for further analytics
authors= []
for c in commits: 
	found=False 
	for a in authors:
		if c.author==a:
			found=True
	if found==False:
		authors.append(c.author)

commits_author=[]
for i in range(len(authors)):
	commits_author.append(0)
	for c in commits:
		if c.author==authors[i]:
			commits_author[i]+=1

dates=[]
for d in commits:
	found=False
	for a in dates:
		if d.date==a:
			found=True
	if found==False:
		dates.append(d.date)

#print out the results

print "The number of contibuting authors was",(len(authors))
print "Names of the authors were:", authors
print "The number of commits on average was",average_commits(commits,authors)
print "The maximum numbers of commits per author was", maximum(commits_author)
print "These are the records from " + min(dates) + " until " + max(dates)
