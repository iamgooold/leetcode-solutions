class Solution {
public:
    string freqAlphabets(string s) {
        string res;
        for (int i = s.size() - 1; i >= 0; i--) {
            if (s[i] == '#') {
                int num = (s[i - 2] - '0') * 10 + (s[i - 1] - '0');
                res += char('a' + num - 1);
                i -= 2;
            } else {
                int num = s[i] - '0';
                res += char('a' + num - 1);
            }
        }
        reverse(res.begin(), res.end());
        return res;
    }
};