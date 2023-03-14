#!/usr/bin/env bash

#Copy over this script to the evolution directory with batchrun.py
#use 'cp runBatchRun.sh /home/wesleyluk/oscillator/evolution/evolution'
#don't need to move the removeFail file!



#echo Run batchrun.py how many times?

read -p "Run batchrun.py how many times? > " numRuns

#echo $numRuns

for ((i=0; i<=$numRuns; i++))
do
	python3 /home/wesleyluk/oscillator/evolution/evolution/batchrun.py


	#while  [[ ! $(pgrep -f batchrun.py) ]]; do
				
	#fi

	for pid in $(pidof -x batchrun.py); do
		if [ $pid != $$ ]; then
			exit 1
		fi
	done


done


python3 /home/wesleyluk/oscillator/osc-scripts/removeFail.py
