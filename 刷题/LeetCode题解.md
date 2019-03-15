<!-- GFM-TOC -->
* [1. TwoSum](#1-TwoSum)
* [2. AddTwoNumbers](#2-AddTwoNumbers)
* [3. LongestSubstringWithoutRepeatingCharacters](#3-LongestSubstringWithoutRepeatingCharacters)
* [4. MedianofTwoSortedArrays](#4-MedianofTwoSortedArrays)
* [5. LongestPalindromicSubstring](#5-LongestPalindromicSubstring)
* [6. ZigZagConversion](#6-ZigZagConversion)
* [7. ReverseInteger](#7-ReverseInteger)
* [8. StringtoInteger](#8-StringtoInteger)
* [9. PalindromeNumber](#9-PalindromeNumber)
* [10. RegularExpressionMatching](#10-RegularExpressionMatching)
* [11. ContainerWithMostWater](#11-ContainerWithMostWater)
* [104. MaximumDepthofBinaryTree](#104-MaximumDepthofBinaryTree)
* [110. BalancedBinaryTree](#110-BalancedBinaryTree)
* [112. PathSum](#112-PathSum)
* [144. BinaryTreePreorderTraversal](#144-BinaryTreePreorderTraversal)
* [437. PathSumIII](#437-PathSumIII)
* [617. MergeTwoBinaryTrees](#617-MergeTwoBinaryTrees)
* [572. SubtreeofAnotherTree](#572-SubtreeofAnotherTree)
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

# 8. StringtoInteger

实现从字符串转化为整数的`atoi`功能。

函数丢弃空格直到找到第一个非空字符，如果字符串的第一个字符是非有效的整数，或者`str`是空字符串或仅仅包含空格，不执行转换。

`INT_MAX(2^31 - 1)` 和 `INT_MIN(-2^31)`。定义`res`为`long long`类型，要不然`res`是最大负数的时候，计算`res * 10`的时候会溢出。
```C++
class Solution {
public:
	int myAtoi(string str) {
		int len = str.length();
		if (str.length() == 0) return 0;
		int i = 0;
		while (str[i] == ' ') i++;
		int flag = 1;
		if (str[i] == '+') {
			i++;
		}
		else if (str[i] == '-') {
			flag = -1;
			i++;
		}
		long long res = 0;//***longlong
		
		while (str[i] - '0' >= 0 && str[i] - '0' <= 9) {
			res = res * 10 + str[i] - '0';
			if (res > INT_MAX) {
				if (flag == 1) return  INT_MAX;
				else return INT_MIN;
			}
			i++;
		}

		return flag * res;
	}
};
```

# 9. PalindromeNumber
回文数

确定一个整数是不是回文数，一个数是回文数当且仅当它从前往后读都是一样的。

第一个思路是将数转换为字符串，但是需要额外的非常数空间；第二种方式是将数翻转与原来的数进行比较，如果它们两者相同的话，则是回文数，但是这个翻转的数是大于`int.MAX`，整数溢出问题。

仅仅翻转数的一半，这个数应该和原来的数的前一半相同。
```C++
class Solution {
public:
	bool isPalindrome(int x) {
		if (x < 0)
			return false;
		if (x == 0)
			return true;
		int tmp = x;
		int reverse_half_num = 0;
		int bitnum = 0;

		while (tmp > 0) {
			tmp = tmp / 10;
			bitnum++;
		}

		for (int i = 0; i < bitnum / 2; i++) {
			reverse_half_num = reverse_half_num * 10 + x % 10;
			x = x / 10;
		}

		if (((reverse_half_num == x) && (bitnum % 2 == 0)) ||( (reverse_half_num == x / 10) && (bitnum % 2 != 0)))
			return true;
		return false;
	}
};
```
# 10. RegularExpressionMatching
给定一个输入字符串s和模式p，用`*`和`.`实现正则表达匹配。

`.`匹配零个或者多个单个字符；`*`匹配零个或者多个前面的元素。

匹配应该覆盖所有的输入字符串而不是部分。

注意： 字符串可以为空，并且只包含`a-z`的小写字母；可以为空，并且只包含`a-z`的小写字母，以及像`.`和`*`的字符。

首先，拿到这个题目后我第一个感觉是做过，可惜的是做题思路给忘记了。顿时有点小小的忧桑，刚刚看到大佬说，刷到一定的题量后，每天花一点时间保持题感还是很重要的，建议刷之前做过的题目，复习效果比做新题要好。大家都有一样的问题，一个月不刷题，再看到题目就跟智障一样。2019年3月4日

现在让我们重新梳理一遍吧。

在剑指Offer第52题中做过这个题目。

s是正常的字符串，p是包含特殊字符的。匹配的话，从左到右一直进行下去。`.`可以匹配任意字符，`*`的话根据它前面的字符来定。

分类如下：
1. 如果s为空的话，p为空，返回为true。
2. 如果s不为空，但是p为空，返回false。在s为空，p不为空时，还是有可能能够匹配成功的。
3. p的下一个字符为`*`。如果p的下一个字符不是`*`，那就直接匹配当前的字符，如果匹配成功，直接匹配下一个，如果匹配失败，那么返回false;如果p的下一个字符是`*`的话，那就比较复杂，因为其可以代表0个或者是多个。如果匹配零个字符时，s的当前字符不变，p的字符后移两位，跳过*这个字符。如果匹配的是1个或者多个，str的字符往下移动一个，但是p的字符不变。

判断条件需要仔细，递归方法。
```C++
class Solution {
public:
	bool isMatch(string s, string p) {
		if (s.empty() && p.empty()) return true;
		if (!s.empty() && p.empty()) return false;
		
		int i = 0, j = 0;
		if (p[j + 1] != '*') {
			if (s[i] == p[j] || (s[i] != '\0' && p[j] == '.') )
				return isMatch(s.substr(i + 1, s.length()), p.substr(j + 1, p.length()));
			else return false;
		}
		else {
			if (s[i] == p[j] || (s[i] != '\0' && p[j] == '.'))
				return isMatch(s, p.substr(j + 2, p.length())) || isMatch(s.substr(i + 1, s.length()), p);
			else//s[i] == '\0'
				return isMatch(s, p.substr(j + 2, p.length()));
		}

		return false;
	}
};
```

# 11. ContainerWithMostWater
给定n个非负整数，每一个代表了在坐标（i，ai）上的点。根据输入画一条垂直的线，线的两端分别是（i，ai）和（i，0）。找到两条垂直的线组成的容器，使其能够容纳最大的量。

拿到这个题的第一个想法就是使用动态规划。

方法1：穷举搜索，计算每两个垂直线对。时间复杂度O(n^2)。

方法2：面积是由最短的那个线的高度决定的。这条线越远，就会获取更多的面积。首先，选取两个指针，一个指向开始端，一个指向结束端，组成了线的长度。维持一个`maxarea`存储目前获取到的最大面积。在每一步找到它们之间的面积，更新`maxarea`并且移动指针指向较短的那条线知道移动到另一端。

```C++
class Solution {
public:
	int maxArea(vector<int>& height) {
		int maxarea = 0;
		if (!height.empty()) {
			int left = 0, right = height.size() - 1;
			while (right >= left) {
				maxarea = max(maxarea, (right - left) * min(height[left], height[right]));
				if (height[left] < height[right]) left++;
				else right--;
			}
		}
		return maxarea;
	}
};
```
# 104. MaximumDepthofBinaryTree
递归方法求树的高度
```C++
class Solution {
public:
	int maxDepth(TreeNode* root) {
		if (root == NULL) return 0;
		return 1 + max(maxDepth(root->left), maxDepth(root->right));
	}
};
```

# 110. BalancedBinaryTree
判断平衡树，递归的方法，用到求解树的高度，在判断的时候需要对每个结点是否平衡进行判断。
```C++
class Solution {
public:
	bool isBalanced(TreeNode* root) {
		if (root == NULL) return true;
		if (abs(height(root->right) - height(root->left)) <= 1) return isBalanced(root->right) && isBalanced(root->left);
		return false;
	}
	int height(TreeNode* root) {
		if (root == NULL) return 0;
		return 1 + max(height(root->right), height(root->left));
	}
};
```

# 112. PathSum

```C++
class Solution {
public:
	bool hasPathSum(TreeNode* root, int sum) {
		if (root == NULL) return false;
		if ( root->left == NULL && root->right == NULL && root->val == sum) return true;
		return hasPathSum(root->left, sum - root->val) || hasPathSum(root->right, sum - root->val);
	}
};
```

# 144. BinaryTreePreorderTraversal
非递归实现树的前序遍历

# 437. PathSumIII
统计路径和等于一个数的路径数量
```C++
struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };

//以根结点为起点或者，不以根节点为起点，两个函数
class Solution {
public:
	int pathSum(TreeNode* root, int sum) {
		if (root == NULL) return 0;	
		int ret = rootPathSum(root, sum) + pathSum(root->left, sum) + pathSum(root->right, sum);
		return ret;
	}
	int rootPathSum(TreeNode* root, int sum) {//以根节点为起点
		if (root == NULL) return 0;
		int ret = 0;
		if (root->val == sum) ret++;
		ret += rootPathSum(root->left, sum - root->val) + rootPathSum(root->right, sum - root->val);
		return ret;
	}
};
```
# 617. MergeTwoBinaryTrees
归并两棵树，对根节点初始化，对根节点的左右结点进行递归。
```C++
class Solution {
public:
	TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
		if (t1 == NULL && t2 == NULL) return NULL;
		if (t1 == NULL) return t2;
		if (t2 == NULL) return t1;
		TreeNode* root = new TreeNode(t1->val + t2->val);
		root->left = mergeTrees(t1->left, t2->left);
		root->right = mergeTrees(t1->right, t2->right);
		return root;
	}
};
```

# 572. SubtreeofAnotherTree
此题判断一个树是不是另外一个树的子树。本题的求解转换为：判断s为根节点的树是否和t相同，或者判断s的两个子树是否存在解。在子树上的求解方法：依旧是递归。
```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
	bool isSubtree(TreeNode* s, TreeNode* t) {
		if ((s == NULL && t == NULL) || (s != NULL && t == NULL)) return true;
		if (s == NULL && t != NULL) return false;
		return isRootSubTree(t, s) || isSubtree(s->left, t) || isSubtree(s->right, t);
	}
	bool isRootSubTree(TreeNode* s, TreeNode* t) {
		if (s == NULL && t == NULL) return true;
		if ((s == NULL && t != NULL) || (s != NULL && t == NULL)) return false;
		if (s->val == t->val) return isRootSubTree(s->left, t->left) && isRootSubTree(s->right, t->right);
		else return false;
	}
};
```