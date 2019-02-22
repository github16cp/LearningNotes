<!-- GFM-TOC -->
* [1. TwoSum](#1-TwoSum)
* [2. AddTwoNumbers](#2-AddTwoNumbers)
* [3. LongestSubstringWithoutRepeatingCharacters](#3-LongestSubstringWithoutRepeatingCharacters)
* [4. MedianofTwoSortedArrays](#4-MedianofTwoSortedArrays)
* [5. LongestPalindromicSubstring](#5-LongestPalindromicSubstring)
* [6. ZigZagConversion](#6-ZigZagConversion)
* [7. ReverseInteger](#7-ReverseInteger)
<!-- GFM-TOC -->

# 1. TwoSum

给定一个整数数组，返回两个数之和等于target的数组索引。

我的思路：夹逼准则，先排序，然后首位寻找是否等于target的数。但是这样排序改变了原来数组的下标，先找到这两个数，然后返回下标。

最简单的方法是穷举搜索，一个是x，另外一个是target-x；复杂度O(n^2)

优化方法：两次hash表操作，对在一维数组中查找target-x优化。

进一步优化：一次hash表操作，边建立hash表边返回。

```C++
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
	vector<int> twoSum(vector<int>& nums, int target) {
		vector<int> res;
		int size = nums.size();
		if (size <= 1) return res;
		vector<int> nums_sort(nums);
		sort(nums_sort.begin(), nums_sort.end());
		int i = 0, j = size - 1;
		while (i <= size - 1 && j >= i) {
			if (nums_sort[i] + nums_sort[j] == target) {
				break;
			}
			else if (nums_sort[i] + nums_sort[j] > target) {
				j--;
			}
			else {
				i++;
			}
		}

		for (int k = 0; k < size; k++) {
			if (nums[k] == nums_sort[i] || nums[k] == nums_sort[j])
				res.push_back(k);
		}		
		return res;
	}
};
```

# 2. AddTwoNumbers
两个非负整数的非空链表，整数数字是逆序存储的，每个节点存有单一的数字，将两个数相加然后将结果返回为一个链表。

```C++
struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
	ListNode * addTwoNumbers(ListNode* l1, ListNode* l2) {
		ListNode *res = new ListNode(0);
		ListNode *p = l1, *q = l2, *reshead = res;
		int carry = 0;
		while (p != nullptr || q != nullptr) {
			int x = (p != nullptr) ? p->val : 0;
			int y = (q != nullptr) ? q->val : 0;
			int sum = x + y + carry;
			carry = sum / 10;
			res->next = new ListNode(sum % 10);
			res = res->next;
			if (p != nullptr) p = p->next;
			if (q != nullptr) q = q->next;
		}
		if (carry > 0) {
			res->next = new ListNode(carry);
		}
		return reshead->next;
	}
};
```

# 3. LongestSubstringWithoutRepeatingCharacters
给定一个字符串，找到无重复字符的最长字串。

穷举搜索的方法：定义一个函数，判断字串是否含有重复字符，如果有重复字符`false`，问题更新为返回无重复的字串的最大长度。

```C++
class Solution {
public:
	int lengthOfLongestSubstring(string s) {
		int res = 0;
		int length = s.length();
		for (int i = 0; i < length; i++)
			for (int j = i + 1; j <= length; j++)
				if (allUnique(s, i, j)) res = max(res, j - i);
		return res;
	}

	bool allUnique(string s, int start, int end) {
		set<char> substr;
		for (int i = start; i < end; i++) {
			char ch = s[i];
			if (substr.find(ch) != substr.end()) return false;
			substr.insert(ch);
		}
        return true;
	}
};
```
std::set [用法](https://www.cnblogs.com/zyxStar/p/4542835.html)

用穷举搜索的方法，时间复杂度较高，不通过。

优化方法：滑动窗口，滑动窗口是在数组和字符串中常用的一个抽象概念。

```C++
class Solution {
public:
	int lengthOfLongestSubstring(string s) {
		vector<char> substr;
		int res = 0;
		for (int i = 0; i < s.length(); i++) {
			auto it = find(substr.begin(), substr.end(), s[i]);
			if (it != substr.end()) {//找到了
				if (res < substr.size())
					res = substr.size();
				it++;
				substr.erase(substr.begin(), it);
			}
			substr.push_back(s[i]);
		}

		if (res < substr.size())
			res = substr.size();

		return res;
	}
};
```

# 4. MedianofTwoSortedArrays
求两个排序数组的中位数，两个递增数组元素个数分别是m，n，求两个数组合并后的中位数。

思路：递归方法，在统计学中，中位数将一个集合分成相同长度的两个部分，其中一部分的数总是大于另外一部分的数。将两个集合进行划分，如果能够保证以下两点：
1. 左右两边的长度相等；
2. 左边的最大的数小于或者等于右边最小的数；
需满足：
1. `i + j = m - i + n - j` or `m - i + n - j + 1`，如果 `n` 大于等于 `m`，则设置 `i = 0 ~ m`， `j = (m + n + 1)/2 - i`；
2. `B[j-1]` 小于等于 `A[i]` && `A[i-1]` 小于等于 `B[j]`。

Searching i in [0, m], to find an object i such that:
```
(j = 0 or i = m or B[j−1] <= A[i] and
(i = 0 or j = n or A[i-1] <= B[j], where j = (m + n + 1)/2 - i
```
```
1. (j=0 or i = m or B[j−1] <= A[i]) and
(i = 0 or j = n or A[i-1] <= B[j])
Means i is perfect, we can stop searching.
2. i< m and B[j−1]>A[i]
Means i is too small, we must increase it.
3. i > 0 and A[i−1]>B[j]
Means i is too big, we must decrease it.
```
when i is found:
```
max(A[i−1],B[j−1]), when m + n is odd
(max(A[i−1],B[j−1])+min(A[i],B[j]))/2, when m + n is even
```

```C++
//二分搜索
class Solution {
public:
	double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
		int m = nums1.size(), n = nums2.size();
		if (m > n) {
			nums1.swap(nums2);
			int tmp; tmp = m; m = n; n = tmp;
		}
		int imin = 0, imax = m, halflen = (m + n + 1) / 2;
		while (imin <= imax) {
			int i = (imin + imax) / 2;
			int j = halflen - i;
			if (i < imax && nums2[j - 1] > nums1[i]) {//i is too small
				imin = i + 1;
			}
			else if (i > imin && nums1[i - 1] > nums2[j]) {//i is too big
				imax = i - 1;
			}
			else {
				int maxleft = 0;
				if (i == 0) { maxleft = nums2[j - 1]; }
				else if (j == 0) { maxleft = nums1[i - 1]; }
				else { maxleft = max(nums1[i - 1], nums2[j - 1]); }
				if ((m + n) % 2 == 1) { return maxleft; }

				int minright = 0;
				if (i == m) { minright = nums2[j]; }
				else if (j == n) { minright = nums1[i]; }
				else { minright = min(nums1[i], nums2[j]); }

				return (maxleft + minright) / 2.0;
			}
		}
		return 0.0;
	}
};
```

# 5. LongestPalindromicSubstring
给定一个字符串s，找到s中的最长回文子串，假定s的最长长度是1000。回文是一个在两个方向上读相同的字符串。

如何使用一个已知的回文字符串来计算一个更长的回文字符串；如果已知`aba`是一个回文字符串，那么判断`xabax`和`xabay`是否是回文字符串；如果采用穷举搜索的方法，开始-结束对O(n^2)的时间复杂度。

减少时间复杂度主要避免验证回文时的重新计算。

动态规划算法：
```C++
class Solution {
public:
	string longestPalindrome(string s) {
		if (s.length() < 1) return "";
		int start = 0, end = 0;
		for (int i = 0; i < s.length(); i++) {
			int len1 = centerDistance(s, i, i);
			int len2 = centerDistance(s, i, i + 1);
			int len = max(len1, len2);
			if (len > end - start + 1) {
				start = i - (len - 1) / 2;
				end = i + len/ 2;
			}
		}
		return s.substr(start, end - start + 1);//c++substr第二个参数代表的是个数
	}

	int centerDistance(string s, int start, int end) {
		while (start >= 0 && end < s.length() && s[start] == s[end]) {
			start--;
			end++;
		}
		return end - start - 1;
	}
};
```

# 6. ZigZagConversion

* 假设第0行有k个字符，位于第一行字符的索引`k*(2*rowNumbers - 2)`
* 第rowNumbers - 1行字符的索引`k*(2*rowNumbers - 2) + (rowNumbers - 1)`
* 第i行字符的索引`k*(2*rowNumbers - 2) + i`和`(k + 1)*(2*rowNumbers - 2) - i`

```C++
class Solution {
public:
	string convert(string s, int numRows) {
		int len = s.length();
		if (len == 0) return "";
		if (numRows == 1) return s;
		string res;
		int cycLen = 2 * numRows - 2;

		for (int i = 0; i < numRows; i++) {
			for (int j = 0; i + j < len; j += cycLen) {
				res += s[j + i];
				if (i != 0 && i != numRows - 1 && j + cycLen - i < len) {
					res += s[j + cycLen - i];
				}
			}
		}
		return res;

	}
};
```

# 7. ReverseInteger
给定32bit的有符号整数，翻转整数的数字。
```C++
class Solution {
public:
	int reverse(int x) {//考虑溢出问题,
		int res = 0;
		while (x != 0) {
			int pop = x % 10;
			x /= 10;
			if (res > INT_MAX/10 || (res == INT_MAX / 10 && pop > 7)) return 0;
			if (res < INT_MIN/10 || (res == INT_MIN / 10 && pop < -8)) return 0;
			res = res * 10 + pop;
		}
		return res;
	}
};
```
