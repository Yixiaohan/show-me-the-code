/*************************************************************************
	> File Name: permu.cpp
	> Author: wangxiaoxian
	> Mail: 634897019@qq.com 
	> Created Time: Wed 03 Aug 2016 10:14:19 PM CST
 ************************************************************************/
//返回一个字符串所有的排列方式
//代码来自：http://www.cricode.com/624.html

#include<iostream>
#include <vector>
using namespace std;
 
typedef vector<string> vs;
 
vs permu(string s){
    vs result;
    if(s == ""){
        result.push_back("");
        return result;
    }
    string c = s.substr(0, 1);
    vs res = permu(s.substr(1));
    for(int i=0; i<res.size(); ++i){
        string t = res[i];
        for(int j=0; j<=t.length(); ++j){
            string u = t;
            u.insert(j, c);
            result.push_back(u);
        }
    }

    return result; //调用result的拷贝构造函数，返回它的一份copy，然后这个局部变量销毁(与基本类型一样)
}
 
vs permu1(string s){
    vs result;
    if(s == ""){
        result.push_back("");
        return result;
    }
    for(int i=0; i<s.length(); ++i){
        string c = s.substr(i, 1);
        string t = s;
        vs res = permu1(t.erase(i, 1));
        for(int j=0; j<res.size(); ++j){
            result.push_back(c + res[j]);
        }
    }
    return result;
}
int main(){
    string s = "abc";
    vs res = permu1(s);
    for(int i=0; i<res.size(); ++i)
        cout<<res[i]<<endl;
    return 0;
}
