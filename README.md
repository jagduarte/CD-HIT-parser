 # CD-HIT Cluster file Parser
CD-HIT (http://weizhong-lab.ucsd.edu/cd-hit/) is a powerful tool to significantly reduce the computational and manual efforts in many sequence analysis tasks, understanding the data structure and correct the bias within a dataset.  

**cdhitparser.py** takes a cluster file (.clstr) as input and returns a .json and/or a csv filesw ith the cluster number as key and all the clustered sequence ids as values.

### Example
Input file obtained from CD-HIT:  *cluster_file.clstr*  

Run the following command within windows CMD:  `$ python cdhitparser.py -c cluster_file.clstr -v`
- - - -
