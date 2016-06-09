Run the following commands in bin directory

rm -rf *;cmake ..;make;./svmtrain;../../../libsvm/svm-scale -l -1 -u 1 -s range train.txt > train.scale.txt;../../../libsvm/svm-scale -r range test.txt > test.scale.txt;../../../libsvm/svm-train -s 0 -c 5 -t 2 -g 0.5 -e 0.1 train.scale.txt

../../../libsvm/svm-predict test.scale.txt train.scale.txt.model result.txt

We recieve the following results
Accuracy = 45.2809% (806/1780) (classification)

