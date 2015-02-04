LIBS=-lm runtime.o hashtable*.o
CFLG=-m32

SRC_FOLDER=p0src
SRCFILES=$SRC_FOLDER/1.py $SRC_FOLDER/2.py $SRC_FOLDER/3.py $SRC_FOLDER/4.py
ASMFILES=$(foreach i,$(seq 1 $SRC_NUM), p0src/$i.s)
OBJFILES=$(foreach i,$(seq 1 $SRC_NUM), p0src/$i.o)

test_lexer:
	echo $(SRCFILES)
	python dj_lex_tester.py $(SRCFILES[1])
	
test_parser:

test_compiler:
	PRES=$(foreach i,"$(SRCFILES)", python $i <in.txt)

	xargs -I {} python compile.py {} < $SRCFILES
	
	SRES=()
	n=0
	for i in $(ASMFILES)
	do
		gcc -c $i -o p0src/$n.o $CFLG
		gcc p0src/$n.o -o prog $LIBS $CFLG
		n=n+1
		SRES+=$(./prog < in.txt)
	done
	
	echo RES[0]
	echo SRES[0]

clean:
	find . -iregex '.*.pyc' -delete
	find . -iregex '.*p0src/*.s' -delete
	find . -iregex '.*p0src/*.o' -delete
