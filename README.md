# CD-HIT Cluster file Parser
CD-HIT (http://weizhong-lab.ucsd.edu/cd-hit/) is a powerful tool to significantly reduce the computational and manual efforts in many sequence analysis tasks, understanding the data structure and correct the bias within a dataset.  
- - - -
**cdhitparser.py** takes a cluster file (.clstr) as input and returns .json and csv files with the cluster number as key and all the clustered sequence ids as values.

### Example
Input file: clusterfile.clstr  
`>python cdhitparser.py -c clusterfile.clstr -v`

![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)
