for i in $(seq 1 1)
do
	file=p0src/$i.py
	RES=$(python $file < in.txt)
	python compile.py $file
	
	gcc -c p0src/$i.s -o p0src/$i.o
	gcc -m32 p0src/$i.o -o prog runtime.o hashtable*.o
	
	SRES=$(./prog < in.txt)
	echo $RES
	echo $SRES
done
