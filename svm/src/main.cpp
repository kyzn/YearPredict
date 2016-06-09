#include<iostream>
#include "Transform.cpp"

int main(){
	Transform t("CroppedData.txt");

	t.save("svmdata.txt");
	return 0;
}