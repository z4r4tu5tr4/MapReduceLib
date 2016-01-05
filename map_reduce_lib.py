#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    About mapreducelib

Version:    0.2.6 (Dec/2015)
Author:     Eduardo Mendes (z4r4tu5tr4)
Oficial:    Github.com/z4r4tu5tr4/mapreducelib
License:    GPLv3
Support:    Python (2.7+ ~ 3.5+)
"""

import os


class hdfs:
    """ Class for manipulate HDFS files and directores"""

    # -------------- Set your Hadoop binary
    def __init__(self,hdfs_local="/usr/local/hadoop/bin/hadoop fs"):
        self.hdfs = hdfs_local

    # -------------- Make a new directory in HDFS
    def mkdir(self, local):
        os.system(("%s -mkdir %s")%(self.hdfs, local))

    # -------------- List a directory in HDFS
    def ls(self, dir="/"):
        if dir != '/':
            os.system(("%s -ls %s")%(self.hdfs,dir))
        else:
            os.system(("%s -ls /")%(self.hdfs))

    # -------------- Remove files
    def rm(self, dir):
    	os.system(("%s -rm %s")%(self.hdfs,dir))

    # -------------- Remove directory
    def rm_dir(self, dir):
        os.system(("%s -rm -r %s")%(self.hdfs,dir))

    # -------------- Trasfer local files to HDFS
    def put(self, files, dir):
        os.system(("%s -put %s %s")%(self.hdfs,files,dir))

    # -------------- Trasfer HDFS files to local FS
    def get(self, dir):
        os.system(("%s -get %s/* .")%(self.hdfs,dir))

    # -------------- Print file on STDOUT
    def cat(self, file):
    	os.system(("%s -cat %s")%(self.hdfs,file))

    # -------------- Change group in a file
    def chgrp(self, mode, file):
    	os.system(("%s -chgrp %s %s")%(self.hdfs,mode,file))

    # -------------- Change persions in a file or directory
    def chmod(self, mode,file):
    	os.system(("%s -chmod %s %s")%(self.hdfs,mode,file))

    # -------------- Change group in a file
    def chown(self, mode,file):
    	os.system(("%s -chown %s %s")%(self.hdfs,mode,file))

class hadoop:
    def __init__(self, hadoop_sbin="/usr/local/hadoop/sbin"):
        self.sbin = hadoop_sbin

    def start_all(self,):
        os.system(("%s/start-all.sh")%(self.sbin))

    def stop_all(self,):
        os.system(("%s/stop-all.sh")%(self.sbin))

    def balancer_start(self,):
        os.system(("%s/start-balancer.sh")%(self.sbin))

    def balancer_stop(self,):
        os.system(("%s/stop-balancer.sh")%(self.sbin))

    def dfs_start(self,):
        os.system(("%s/start-dfs.sh")%(self.sbin))

    def dfs_stop(self,):
        os.system(("%s/stop-dfs.sh")%(self.sbin))

    def dns_start(self,):
        os.system(("%s/start-secure-dns.sh")%(self.sbin))

    def dns_stop(self,):
        os.system(("%s/stop-secure-dns.sh")%(self.sbin))

    def yarn_start(self,):
        os.system(("%s/start-yarn.sh")%(self.sbin))

    def yarn_stop(self,):
        os.system(("%s/stop-yarn.sh")%(self.sbin))

    def format_namenode(self,):
        s_n = input("Deseja realmente formatar o seu HDFS? (S/N)")
        if s_n == "S" or "s":
            os.system("/usr/local/hadoop/bin/hdfs namenode -format")

    def format_datanode(self,):
        s_n = input("Deseja realmente formatar o seu HDFS? (S/N)")
        if s_n == "S" or "s":
            os.system("/usr/local/hadoop/bin/hdfs datanode -format")

class map_reduce:
    def __init__(self,
                hadoop_streaming="/usr/local/hadoop/share/hadoop\
                /tools/lib/hadoop-streaming-2.*.jar",
                hadoop_dir="/usr/local/hadoop/bin/hadoop"):

        self.streaming = hadoop_streaming
        self.hadoop = hadoop_dir

    def run_map_reduce(self, mapper, reducer,
                        _input,output):

    	os.system(("%s jar %s \
    	-mapper %s \
    	-reducer %s \
    	-input /%s \
    	-output /%s")%(self.hadoop,self.streaming,
                        mapper,reducer,_input,output))

    def run_map(self, mapper,
                _input, output):

        os.system(("%s jar %s \
    	-mapper %s \
    	-input /%s \
    	-output /%s")%(self.hadoop,self.streaming,mapper,
                        reducer,_input,output))

    def run_map_combiner_reduce(self, mapper, combiner,
                                reducer, _input, output):

        os.system(("%s jar %s \
    	-mapper %s \
    	-reducer %s \
        -combiner %s \
    	-input /%s \
    	-output /%s")%(self.hadoop,self.streaming,mapper,
                        combiner,reducer,_input,output))

    def run_pass_flags(self, parameter):

        os.system(("%s jar %s %s")%(self.hadoop, self.streaming, parameter))
