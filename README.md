# CD-HIT Cluster file Parser
CD-HIT is very fast and can handle extremely large databases. CD-HIT helps to significantly reduce the computational and manual efforts in many sequence analysis tasks and aids in understanding the data structure and correct the bias within a dataset.  
http://weizhong-lab.ucsd.edu/cd-hit/
- - - -
cdhitparser.py takes a cluster file (.clstr) as input and returns a .json file and csv file with the cluster number as key and all the clustered sequence ids as values.

EX: 
`>python cdhitparser.py -c clusterfile.clstr -v`
