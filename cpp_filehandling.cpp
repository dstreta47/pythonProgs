#include<iostream>
#include<fstream>

int main(){

    std::ofstream ofs("myt.txt",std::ios::trunc);
    ofs<< "hi my name is Amit, this is an example" << std::endl;
    ofs<<25<< std::endl;
    ofs.close();
}
