class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> hsh1(26, 0);
        vector<int> hsh2(26, 0);

        if (s.size() != t.size()) {
            return false;
        }

        for (int i = 0; i < s.size(); i++) {
            hsh1[s[i] - 'a']++; 
        }
        for (int j = 0; j < t.size(); j++) {
            hsh2[t[j] - 'a']++; 
        }

        if (hsh1 == hsh2) {
            return true;
        }
        return false;
    }
};
