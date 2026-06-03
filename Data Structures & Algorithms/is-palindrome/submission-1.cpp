class Solution {
public:
    bool isPalindrome(string s) {
        string str1;

        for (char c : s) {
            if (isalnum(c)){
                str1 += tolower(c);
            }
        }

        string rev = str1;
        reverse(rev.begin(), rev.end());
        if (str1 == rev) return true;
        return false;
    }
};
