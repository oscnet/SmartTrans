#!/bin/sh

# 参数1 为html文件或 url

if [ -a $1 ];then
  html=`cat $1`
  curl -L -X POST --data "html=$html&showframe=0" "http://heckyesmarkdown.com/go/"
else
  curl -L -X POST --data "u=$1&showframe=0" "http://heckyesmarkdown.com/go/"
fi
