# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

###
# In This Graph, we have created 1 big graph with Documents and Authors.
#
###

import csv
from igraph import *

# read in the files for pre-processing
file = open("dois.citations.txt", "rb") #document citations
d2a = open("doi2auth.map.txt", "rb") # document authors
csv_read = csv.reader(file,dialect=csv.excel_tab) 
d2a_read = csv.reader(d2a, dialect=csv.excel_tab)

dois_list = [] # this will form the base list for further processing into the list of Tuples to be made into a Graph
for row in csv_read:
    for w in row:
        dois_list.append(w.split())

for row in d2a_read:
    for w in row:
        dois_list.append(w.split()[::-1])
        
graph_list = [] # create a list of tuples for the graph. This contains a pair of vertices that are directed to the 0th item
for d in dois_list:
    for i in range(len(d)-1):
        graph_list.append((d[i+1], d[0],1.5))
        
# Create graph_list
g = Graph.TupleList(directed=True, edges = graph_list, weights=True)



# Proposed visualisation with Gephi, export to edges for display
#g.write('waproj.edges',format='edgelist')

# Rank all nodes, merge with nodes into a dictionary
pagerank = {}
pagerank = dict(zip(g.vs["name"], g.pagerank()))

# Sort the results out and store it in a list in Descending order
pagerank_results = sorted(g.vs["name"], key=pagerank.__getitem__, reverse=True)

# Display up to 1000 records
pagerank_results[:1000]

# Save those Authors who have been identified in the Graph and Gold list
# Can alter the total number of nodes.
identified_list = []
for node in pagerank_results[:9400]:
    identified_list.append(GoldAuthor.get_author(node))

# Count the number of Gold Authors identified from the Graph
gold_author = 0
for i,a in enumerate(identified_list):
    if a != None:
        gold_author += 1
            
# DISPLAY and save results
print gold_author
print len(identified_list)
print 100.00*gold_author/len(identified_list)



file = open("pagerankresults.csv","wb")
wr = csv.writer(file, quoting=csv.QUOTE_ALL)
wr.writerow(pagerank_results)
file.close


file = open("gold_auth.csv", "wb")
wr = csv.writer(file, quoting=csv.QUOTE_ALL)
wr.writerow(identified_list)
file.close
