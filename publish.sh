#!/bin/bash
echo "converting deus to html....";
echo "press ctrl+c to abort";
while :
do
	python ~/writing/htmlify/menu.py publish /Users/jmason/writing/deus styles/css/styles.css; 
	sleep 1
done
