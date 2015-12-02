#!/bin/bash
current=`pwd`
cd /u01/blog
make html
cd $current

cp -r /u01/blog/output/* /root/git/cooleasyhan.github.com/

