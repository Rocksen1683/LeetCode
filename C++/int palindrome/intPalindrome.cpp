class Solution
{
public:
    bool isPalindrome(int x)
    {
        string s = std::to_string(x);
        string rev = "";

        for (int i = s.length() - 1; i >= 0; i--)
        {
            rev += s[i];
        }

        if (rev == s)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};