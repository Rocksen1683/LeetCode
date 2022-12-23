using namespace std;

class Solution
{
public:
    void phoneBFS(int index, vector<string> path)
    {
        if (path.size() == digits.length())
        {
            // path length is same as input
            string pathStr = "";
            for (int i = 0; i < path.size(); i++)
            {
                pathStr += path[i]
            }
            combinations.push_back(pathStr);
            return
        }

        // retrieving the possible combinations from the map
        string letters = phoneNums[digits[index]];

        for (int j = 0; j < letters.length(); j++)
        {
            path.push_back(letters[j])

                // getting next path
                phoneBFS(index + 1, path);

            // popping off last element in path for next iteration
            path.pop_back()
        }
    }
    vector<string> letterCombinations(string digits)
    {

        vector<string> combinations;

        if (digits.length() == 0)
        {
            return combinations;
        }

        unordered_map<string, string> phoneNums;

        phoneNums["2"] = "abc";
        phoneNums["3"] = "def";
        phoneNums["4"] = "ghi";
        phoneNums["5"] = "jkl";
        phoneNums["6"] = "mno";
        phoneNums["7"] = "pqrs";
        phoneNums["8"] = "tuv";
        phoneNums["9"] = "wxyz";

        // calling phoneBFS
        phoneBFS(0, []);

        return combinations;
    }
};