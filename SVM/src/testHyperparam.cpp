#include<iostream>
#include<cmath>
#include<sstream>
int main(){


	for(int i = -5; i < 16; i+=5){
		double C =pow(2, i);
		for (int j = -15; j < 4; j+=5){
			double gamma = pow(2, j);

			std::cout << "C: " << C << std::endl;
			std::cout << "gamma: " << gamma << std::endl;

			std::ostringstream strs;
			strs << C;

			std::ostringstream strs1;
			strs1 << gamma;

			system(("../../../libsvm/svm-train -q -s 0 -c "+strs.str()+" -t 2 -g "+strs1.str()+" -e 0.1 train.scale.txt").c_str());
			system("../../../libsvm/svm-predict test.scale.txt train.scale.txt.model result.txt");

			std::cout << std::endl;
		}
	}
	return 0;
}