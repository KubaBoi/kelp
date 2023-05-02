#include <iostream>
#include <iterator>
#include <string>
#include <regex>
#include <fstream> 

using namespace std;
 
int main()
{
    // Create a text string, which is used to output the text file
    string myText;

    // Read from the text file
    ifstream MyReadFile("filename.txt");

    // Use a while loop together with the getline() function to read the file line by line
    while (getline (MyReadFile, myText)) {
    // Output the text from the file
    cout << myText;
    }
 
    regex self_regex("REGULAR EXPRESSIONS", regex_constants::ECMAScript | regex_constants::icase);
    if (regex_search(myText, self_regex)) {
        cout << "Text contains the phrase 'regular expressions'\n";
    }
 
    regex word_regex("(\\w+)");
    auto words_begin = 
        sregex_iterator(myText.begin(), myText.end(), word_regex);
    auto words_end = sregex_iterator();
 
    cout << "Found "
              << distance(words_begin, words_end)
              << " words\n";
 
    const int N = 6;
    cout << "Words longer than " << N << " characters:\n";
    for (sregex_iterator i = words_begin; i != words_end; ++i) {
        smatch match = *i;
        string match_str = match.str();
        if (match_str.size() > N) {
            cout << "  " << match_str << '\n';
        }
    }
 
    regex long_word_regex("(\\w{7,})");
    string new_s = regex_replace(myText, long_word_regex, "[$&]");
    cout << new_s << '\n';
}