In CiteSeer
-Each document has a document id also called DOI
-Each author is referred to using an author id.


[1] papers.lemur.txt contains documents and their abstracts in a format that is easy to index
in Lemur/Indri

[2] doi2auth.map.txt  

Contains authors information for each DOI.
Each lines looks like
DOI AuthID

[3] doi2ncites.map.txt  

Each line looks like
DOI <number of citations for this paper in CiteSeer>

[4] dois.citations.txt  

DOI* <list of DOIs that cite DOI*>

[5] queries.txt and sresults 

Contains the list of queries and for each query, a corresponding file in sresults
contains the top 100 results from Indri. That is using the query, the top-100 matching
papers from papers.lemur are listed with their scores.

[6] gold
For each query, the list of "gold experts" are listed.
