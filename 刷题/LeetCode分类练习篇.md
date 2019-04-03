<!-- GFM-TOC -->
* [1. 数组](#1-数组)
<!-- GFM-TOC -->

# 1. 数组
## 15. 3Sum
二分查找，寻找3个数相加为0。
```C++
#include<iostream>
#include <algorithm>
#include<vector>
using namespace std;

//固定i和j,查找t,二分查找lower_bound,O(n^2*log(n))
class Solution {
public:
	vector<vector<int>> threeSum(vector<int>& nums) {
		vector<vector<int>> res;
		int len = nums.size();
		if (len == 0) return res;
		sort(nums.begin(), nums.end());
		for (int i = 0; i < len; i++) {
			for (int j = i + 1; j < len; j++) {
				vector<int> tmp;
				int t = -(nums[i] + nums[j]);
				auto it = lower_bound(nums.begin() + j + 1, nums.end(), t);//返回下标
				if (it != nums.end() && *it == t) {//二分查找找到
					tmp.push_back(nums[i]);
					tmp.push_back(nums[j]);
					tmp.push_back(*it);
					res.push_back(tmp);
				}
				while (j + 1 < len && nums[j + 1] == nums[j]) {
					j++;

				}
			}
			while (i + 1 < len && nums[i + 1] == nums[i]) {
				i++;
			}
		}
		return res;
	}
};

int main()
{
	return 0;
}
```