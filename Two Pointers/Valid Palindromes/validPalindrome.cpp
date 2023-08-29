class Solution {
public:
    bool isPalindrome(string s) {
        string sLower;
        for(auto i: s){
            if (isalnum(i) != 0){
                sLower+=i;
            }
        }

        int fwd = 0;
        int back = sLower.length() - 1;

        for(int i = 0; i<= floor(sLower.length()/2); i++){
            if (sLower[fwd] != sLower[back]){
                return false;
            }
            else{
                fwd += 1;
                back -= 1;
            }
        }
        return true;
    }
};