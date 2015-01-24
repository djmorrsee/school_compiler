for i in `seq 1 7`
do
	file=p0src/$i.py
	RES=`python $file < in.txt`
	python compile.py $file
	gcc p0src/$i.s runtime/*.o -lm -m32 -o prog
	SRES=`./prog < in.txt`
	if [ $RES == $SRES ]
	then
		echo SUCCESS $i
	else 
		echo FAILURE $i
	fi
done
