# LDSAproject

# Contents
1. hadoop_master_conf and hadoop_slave_conf are folders with hadoop configuration for master and slave respectively
2. concatEmails.py is script for concatenate files input to achieve 64MB size
3. data_stat.csv is a list of total amount of emails inside each folder for each account
4. email_counter.py is a script to count emails in each folder
5. email_parser.py is example of parsing an email
6. mapper.py is a mapper script used outside hadoop environment
7. mapper_hadoop.py is a mapper script used in hadoop environment
8. readfiles.py is a eksperimental script to read files from enron folder
9. reducer.py is a script used as reducer in hadoop

# How to configure the Hadoop cluster

1. Follow the instructions given in the following tutorials:
* http://khangaonkar.blogspot.se/2014/02/hadoop-2x-yarn-cluster-setup-tutorial.htm
* https://linoxide.com/cluster/setup-hadoop-multi-node-cluster-ubuntu/
2. As trubleshooting, use the configuration files given in the folders hadoop_master_conf and hadoop_slave_conf. The .xml files should compared to the ones in the path $HADOOP_HOME/etc/hadoop and the hosts file with the file /etc/hosts	.

# How to run the experiment
1. Put data into HDFS storage:
	- hdfs dfs -mkdir /input
	- hdfs dfs -put local_path /input
2. Run hadoop command:
	- hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -file /mnt/volume/project/mapper_hadoop.py -mapper mapper_hadoop.py -file /mnt/volume/project/reducer.py -reducer reducer.py -input /input/* -output /output -verbose

# Setup git locally
git clone https://github.com/ilona-asa/LDSAproject.git

# How this repository works
1. Each time you're beginning to work in this repository, don't forget to do this:
    - git pull
  
2. After you're done with your work, do this:
    - git add <filename>
    - git commit -m "what you've modified/add/delete in detail"
    - git pull
    - git push -u origin master
  
3. If there's a conflict, then do this:
    - comment out the part that start with <<<< and end with >>>>>>
    - git commit -m "what conflict did you see and solve"
    - git push -u origin master
