LIBS=-lm runtime.o hashtable*.o
CFLG=-m32

SRC_FOLDER=p0src
SRCFILES=$(SRC_FOLDER)/1.py
ASMFILES=$(foreach i,$(seq 1 $SRC_NUM), p0src/$i.s)
OBJFILES=$(foreach i,$(seq 1 $SRC_NUM), p0src/$i.o)

test_lexer:
	echo $(SRCFILES)
	python dj_lex_tester.py $(SRCFILES)
	
test_parser:

compile:
	python compile.py p0src/1.py
	gcc -c -m32 p0src/1.s -o p0src/1.o $(CFLG)
	gcc p0src/1.o -o prog -m32 runtime.o hashtable*.o -lm

test_compiler:
	PRES=$(foreach i,"$(SRCFILES)", python $i <in.txt)

	xargs -I {} python compile.py {} | 
	
	SRES=()
	n=0
	for i in $(ASMFILES)
	do
		gcc -c -m32 $i -o p0src/$n.o $(CFLG)
		gcc p0src/$n.o -o prog $(LIBS) $(CFLG)
		n=n+1
		SRES+=$(./prog < in.txt)
	done
	
	echo RES[0]
	echo SRES[0]

clean:
	find . -iregex '.*.pyc' -delete
	find . -iregex '.*p0src/.*.s' -delete
	find . -iregex '.*p0src/.*.o' -delete
	rm -rf prog
