#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

int main()
{
	ifstream in_post;
	ofstream out_post;
	int p = 1901, endp = 1902;
	size_t found = 0;
	stringstream name_ss, file_ss;
	string file_name, file_contain;
	file_name.clear();
	file_contain.clear();
    
	cout << "begin tag-remover\nplease enter the number of last post:\n";
    cin >> endp;
	cout << "remove & replace all unwanted tag from " << p << " to " << endp << endl;
	
	while(p <= endp)
	{
		// clear all stringstream
		file_ss.str(std::string());
		name_ss.str(std::string());
		
		// get the filename
		name_ss << p;
		if (p % 1000 == 0) cout << "p=" << p << endl;
		p++;
		file_name = "./zhhomestuck.github.io/p/00" + name_ss.str() + ".html";
		
		// read files
		in_post.open(file_name.data());
        if (in_post.fail())
        {
            cout << "file open fail at p =" << p << endl;
            continue;
        }
        
		file_ss << in_post.rdbuf();
		in_post.close();
		file_contain = file_ss.str();
		
		// replace and remove tags 
		while((found = file_contain.find("&lt;")) != string::npos)
		{
			char next = file_contain[found + 1];
			if (next != '!' || next != ' ')
			{
				file_contain.replace(found, 4, "<");
			}
		}
		while((found = file_contain.find("&gt;")) != string::npos)
		{
			char next = file_contain[found + 1];
			if (next != '!' || next != ' ')
			{
				file_contain.replace(found, 4, ">");
			}
		}
		if ((found = file_contain.find("//end AC code")) != string::npos)
		{
			file_contain.erase(found, 13);
		}
		if ((found = file_contain.find("<table>")) != string::npos)
		{
			file_contain.erase(found, 7);
			found = file_contain.find("</table>");
			file_contain.erase(found, 8);
			while((found = file_contain.find("<tbody>")) != string::npos)
			{
				file_contain.erase(found, 7);
			}
				while((found = file_contain.find("</tbody>")) != string::npos)
			{
				file_contain.erase(found, 8);
			}
			while((found = file_contain.find("<tr>")) != string::npos)
			{
				file_contain.erase(found, 4);
			}
			while((found = file_contain.find("</tr>")) != string::npos)
			{
				file_contain.erase(found, 5);
			}
			while((found = file_contain.find("<td>")) != string::npos)
			{
				file_contain.erase(found, 4);
			}
			while((found = file_contain.find("</td>")) != string::npos)
			{
				file_contain.erase(found, 5);
			}
		}
		while((found = file_contain.find("/zhhomestuck.blogspot.tw/p/")) != string::npos)
		{
			file_contain.replace(found, 27, "/zhhomestuck.github.io/p/");
		}
		while((found = file_contain.find("/zhhomestuck.blogspot.com/p/")) != string::npos)
		{
			file_contain.replace(found, 28, "/zhhomestuck.github.io/p/");
		}
		while((found = file_contain.find("/zhhomestuck.blogspot.tw/")) != string::npos)
		{
			file_contain.replace(found, 33, "/zhhomestuck.github.io/p/");
		}
		while((found = file_contain.find("/zhhomestuck.blogspot.com/")) != string::npos)
		{
			file_contain.replace(found, 34, "/zhhomestuck.github.io/p/");
		}
		
		// write result into file
		out_post.open(file_name.data(), ios::out | ios::trunc);
		out_post << file_contain;
		out_post.close();
	}
	return 0;
}
