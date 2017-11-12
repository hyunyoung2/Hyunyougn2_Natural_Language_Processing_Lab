# Google C source file, Word2vec

This file is made in jupyter notebook. 

This file explains to you how to use C Source file of google's Word2Vec from compile to usage of simple example.

To sum up the file : 

from now on, what I exmplain to you is After download is complet.

> unzip source-archive.zip

```bash
Archive:  source-archive.zip
   creating: word2vec/
  ......
  inflating: word2vec/trunk/word2vec.c  
  inflating: word2vec/trunk/questions-words.txt  
  inflating: word2vec/trunk/LICENSE  
```

enter word2vec/trunk directory. 

> cd word2vec/trunk

> ls 

```bash
# hyunyoung2 @ hyunyoung2-desktop in ~/my-jupyter/word2vec-of-google/test/word2vec/trunk [17:29:10] 
$ ls
compute-accuracy.c       demo-train-big-model-v1.sh  makefile               word2vec.c
demo-analogy.sh          demo-word-accuracy.sh       questions-phrases.txt  word-analogy.c
demo-classes.sh          demo-word.sh                questions-words.txt
demo-phrase-accuracy.sh  distance.c                  README.txt
demo-phrases.sh          LICENSE     
```

> make 

> ls 

```
# hyunyoung2 @ hyunyoung2-desktop in ~/my-jupyter/word2vec-of-google/test/word2vec/trunk [17:33:25] 
$ make
gcc word2vec.c -o word2vec -lm -pthread -O3 -march=native -Wall -funroll-loops -Wno-unused-result
gcc word2phrase.c -o word2phrase -lm -pthread -O3 -march=native -Wall -funroll-loops -Wno-unused-result
gcc distance.c -o distance -lm -pthread -O3 -march=native -Wall -funroll-loops -Wno-unused-result
distance.c: In function ‘main’:
distance.c:31:8: warning: unused variable ‘ch’ [-Wunused-variable]
   char ch;
        ^
......
                                                                                                   ^
chmod +x *.sh

# hyunyoung2 @ hyunyoung2-desktop in ~/my-jupyter/word2vec-of-google/test/word2vec/trunk [17:38:36] 
$ ls
compute-accuracy         demo-train-big-model-v1.sh  makefile               word2vec
compute-accuracy.c       demo-word-accuracy.sh       questions-phrases.txt  word2vec.c
demo-analogy.sh          demo-word.sh                questions-words.txt    word-analogy
demo-classes.sh          distance                    README.txt             word-analogy.c
demo-phrase-accuracy.sh  distance.c                  word2phrase
demo-phrases.sh          LICENSE                     word2phrase.c

```

let's execute word2vec as follows:

> ./word2vec -train data.txt -output vec.txt -size 200 -window 5 -sample 1e-4 -negative 5 -hs 0 -binary 0 -cbow 1 -iter 3


