//reads file
#include<iostream>
#include<fstream>

int main(){

    std::ofstream ofs("myt1.txt",std::ios::trunc);
    ofs<< "John" << std::endl;
    ofs<<25<< std::endl;
    ofs.close();

    std::ifstream ifs;
    ifs.open("myt1.txt");
    std::string str;
    int x;
    ifs >> str;
    ifs >> x;
    std::cout << str << " " <<x;
    if(ifs.eof()) std::cout << "EOF";
    ifs.close();
}
