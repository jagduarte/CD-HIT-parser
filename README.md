# CD-HIT Cluster file Parser
CD-HIT (http://weizhong-lab.ucsd.edu/cd-hit/) is very fast and can handle extremely large databases. CD-HIT helps to significantly reduce the computational and manual efforts in many sequence analysis tasks and aids in understanding the data structure and correct the bias within a dataset.  
- - - -
**cdhitparser.py** takes a cluster file (.clstr) as input and returns a .json file and csv file with the cluster number as key and all the clustered sequence ids as values.

`>python cdhitparser.py -c clusterfile.clstr -v`


