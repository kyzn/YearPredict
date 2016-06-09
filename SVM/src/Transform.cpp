#include <iomanip>
#include<string>
#include<limits>
#include<iostream>
#include <fstream>
#include<vector>
#include<sstream>

class Transform{
private:
	std::string infile;
public:
	Transform(std::string filename){
		this->infile = filename;
	}

	void save(std::string filename){
		std::ifstream infile(this->infile);
		std::string line;
		std::ofstream ofile(filename);
		if (ofile.is_open())
		{
			std::vector<std::vector<double >> dataLine;
			while (std::getline(infile, line))
			{

				std::stringstream  lineStream(line);
				std::string        cell;
				std::vector<double> data;
				while(std::getline(lineStream,cell,','))
				{

					data.push_back(std::stod (cell));
				}

//				data[0]-=1922;
				dataLine.push_back(data);
			}
			dataLine = scale(dataLine);
			for (int i = 0; i < dataLine.size(); i ++){
				std::vector<double> data = dataLine[i];
				std::string newData = dtos(data[0]);
				for (int j = 1; j < data.size(); j++){

					newData+=" " + dtos(j)+":"+ dtos(data[j]);
				}

				ofile <<newData<<"\n";
			}
			ofile.close();
		}
	}
private:
	std::string dtos(double db){
		std::ostringstream strs;
		strs << std::setprecision(8) << db;
		std::string str = strs.str();
		std::string s =strs.str();
		return s;
	}


	double findMax(std::vector<std::vector<double >> dataLine, int x){
		double max = std::numeric_limits<double >::min();
		for(int i = 0; i < dataLine.size(); i++){
			if (dataLine[i][x] > max)
				max = dataLine[i][x];
		}
		return max;
	}
	double findMin(std::vector<std::vector<double >> dataLine, int x){
		double min = std::numeric_limits<double >::max();
		for(int i = 0; i < dataLine.size(); i++){
			if (dataLine[i][x] < min)
				min = dataLine[i][x];
		}
		return min;
	}

	std::vector<std::vector<double>> scale(std::vector<std::vector<double>> dataLine){
		//90 features
		auto y(dataLine);
		bool x = false;
		for (int i = 1; i < 91; i++){
			double min = findMin(dataLine, i);
			double max = findMax(dataLine, i);
			std::cout << std::setprecision(8) <<min << std::endl;
			std::cout << std::setprecision(8) <<max << std::endl;
			for(int j = 0; j < dataLine.size(); j++){
				y[j][i] = -1+ (1 - (-1))*(dataLine[j][i]-min)/(max - min);
			}
		}
		return y;
	}
};