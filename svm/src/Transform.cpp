#include<string>
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
			while (std::getline(infile, line))
			{
				std::stringstream  lineStream(line);
				std::string        cell;
				std::vector<double> data;
				while(std::getline(lineStream,cell,','))
				{
					data.push_back(std::stod (cell));
				}
				std::string newData = dtos(data[0]);
				for (int i = 1; i < data.size(); i++){
					newData+=" " + dtos(i)+":"+ dtos(data[i]);
				}

				ofile <<newData<<"\n";
			}
			ofile.close();
		}
	}

	std::string dtos(double db){
		std::ostringstream strs;
		strs << db;
		std::string str = strs.str();
		std::string s =strs.str();
		return s;
	}
};