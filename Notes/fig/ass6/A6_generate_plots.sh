#!/bin/bash
for i in `ls *.py`; do python $i; echo $i; done
