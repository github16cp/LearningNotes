<!-- GFM-TOC -->
* [1. 数组](#1-数组)
* [2. 字符串](#2-字符串)
* [3. 位运算](#3-位运算)
* [4. 哈希表](#4-哈希表)
* [5. 链表](#5-链表)
<!-- GFM-TOC -->

# 1. 数组
[array类题目](https://leetcode.com/problemset/all/?topicSlugs=array)
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
## 26. Remove Duplicates from Sorted Array
```C++
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
	int removeDuplicates(vector<int>& nums) {
		int len = nums.size();
		if (len == 0) return 0;
		if (len == 1) return 1;

		for (vector<int>::iterator it = nums.begin(); (it + 1)!= nums.end(); ) {
			if (*it == *(it+1))
				nums.erase(it+1);
			else it++;
		}
		return nums.size();
	}
};

int main()
{	
	Solution ss;
	vector<int> nums = { 0,0,1,1,1,2,2,3,3,4 };
	cout << ss.removeDuplicates(nums) << endl;
	system("pause");
	return 0;
}
```
## 27. Remove Element
```C++
class Solution {
public:
	int removeElement(vector<int>& nums, int val) {
		int len = nums.size();
		if (len == 0) return 0;
		for (vector<int>::iterator it = nums.begin(); it != nums.end();) {
			if (*it == val)
				it = nums.erase(it);
			else it++;
		}
		return nums.size();
	}
};
```

## 35. Search Insert Position
```C++
class Solution {
public:
	int searchInsert(vector<int>& nums, int target) {
		int len = nums.size();
		if (len == 0) return 0;		
		if (nums[0] >= target)
			return 0;
		int i = 0;
		for (; i + 1 < len; i++) {
			if (nums[i] == target)
				return i;
			if (nums[i] < target && nums[i + 1] >= target)
				return i + 1;
		}
		return len;
	}
};
```
## 53. Maximum Subarray
```C++
class Solution {
public:
	int maxSubArray(vector<int>& nums) {
		int len = nums.size();
		if (len == 0) return 0;
		int cursum = 0;//累加的子数组的和
		int greatsum = 0x80000000;//最大的子数组的和
		for (int i = 0; i < len; i++) {
			if (cursum <= 0)
				cursum = nums[i];
			else
				cursum += nums[i];

			if (cursum > greatsum)
				greatsum = cursum;
		}
		return greatsum;
	}
};
```
## 66. Plus One
```C++
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
	vector<int> plusOne(vector<int>& digits) {
		if (!digits.size()) return digits;
		int carry = 1;
		for (int i = digits.size() - 1; i >= 0; --i) {
			int tmp = digits[i] + carry;
			digits[i] = tmp % 10;
			carry = tmp / 10;
		}
		if (carry) digits.insert(digits.begin(), carry);
		return digits;
	}
};

int main() {
	Solution s;
	vector<int> vec = { 1,2,3 };
	vector<int> res;
	res = s.plusOne(vec);
	for (auto i : res)
		cout << i << " ";
	cout << endl;
	system("pause");
	return 0;
}
```
## 88. Merge Sorted Array
```C++
class Solution {
public:
	void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
		if (!nums2.size()) return;
		if (!nums1.size()) return;
		if (nums1.size() < (m + n)) return;
		int j = 0;
		for (int i = m; i < nums1.size() && j < nums1.size(); ++i)
			nums1[i] = nums2[j++];
		sort(nums1.begin(), nums1.end());
	}
};
```
## 118. Pascal's Triangle
杨辉三角
```C++
class Solution {
public:
	vector<vector<int>> generate(int numRows) {
		vector<vector<int> > res;
		if (numRows == 0) return res;

		vector<int> tmp(1, 1);//第一个
		res.push_back(tmp);

		for (int i = 2; i <= numRows; i++) {
			tmp.push_back(0);
			vector<int> cur = tmp;
			for (int j = 1; j < i; j++)
				cur[j] = tmp[j] + tmp[j - 1];
			res.push_back(cur);
			tmp = cur;
		}
		return res;
	}
};
```
## 119. Pascal's Triangle II
```C++
class Solution {
public:
	vector<int> getRow(int rowIndex) {
		vector<int> res;
		if (rowIndex < 0) return res;

		vector<int> last(1,1);///rowIndex = 0
		res = last;
		for (int i = 2; i < rowIndex + 2; i++) {//rowIndex = 1;
			last.push_back(0);
			res = last;
			for (int j = 1; j < i; j++)
				res[j] = last[j] + last[j - 1];
			last = res;
		}
		return res;
	}
};
```
## 121. Best Time to Buy and Sell Stock
```C++
class Solution {
public:
	int maxProfit(vector<int>& prices) {
		int len = prices.size();
		if (len <= 1) return 0;
		int res = prices[1] - prices[0], minprice = prices[0];
		for (int i = 2; i < len; i++) {
			minprice = min(minprice, prices[i - 1]);
			if (res < prices[i] - minprice)
				res = prices[i] - minprice;
		}
		if (res < 0) return 0;
		return res;
	}
};
```

```C++
```

```C++
```
# 2. 字符串
[字符串](https://leetcode.com/problemset/all/?topicSlugs=string)
## 344. Reverse String
```C++
class Solution {
public:
	void reverseString(vector<char>& s) {
		if (s.size() == 0) return;
		int begin = 0, end = s.size() - 1;
		while (begin < end) {
			char tmp = s[begin];
			s[begin] = s[end];
			s[end] = tmp;
			begin++, end--;
		}
	}
};
```
## 151. Reverse Words in a String
用`vector<string> tmp`存，时间复杂度太高
```C++
#include<iostream>
#include<string>
#include<vector>
using namespace std;
//"  hello  world!  ";
class Solution {
public:
	string reverseWords(string s) {
		int nLength = s.length();
		if (nLength == 0) return s;
		string res = "";
		int begin, end;
		for (int i = nLength - 1; i >= 0;) {
			while (i >= 0 && s[i] == ' ') i--;
			end = i;
			if (i < 0) break;
			if (!res.empty()) res.push_back(' ');
			while (i >= 0 && s[i] != ' ') i--;
			begin = i + 1;
			res.append(s.substr(begin, end - begin + 1));
		}
		return res;
	}
};

int main()
{
	string str = "  hello  world!  ";
	Solution  s;
	cout << s.reverseWords(str) << endl;
	system("pause");
	return 0;
}

```

## 709. To Lower Case
```C++
class Solution {
public:
	string toLowerCase(string str) {
		int len = str.length();
		if (len == 0) return str;
		transform(str.begin(), str.end(), str.begin(), ::tolower);		
		return str;
	}
};
```

## 917. Reverse Only Letters
对撞指针
```C++
class Solution {
public:
	string reverseOnlyLetters(string S) {
		int left = 0;
		int right = S.size() - 1;
		while (left < right) {
			if (((S[left] >= 'A' && S[left] <= 'Z') || (S[left] >= 'a' && S[left] <= 'z')) && ((S[right] >= 'A' && S[right] <= 'Z') || (S[right] >= 'a' && S[right] <= 'z'))) {
				char tmp = S[left];
				S[left] = S[right];
				S[right] = tmp;
				left++;
				right--;
			}
			else if(!((S[left] >= 'A' && S[left] <= 'Z') || (S[left] >= 'a' && S[left] <= 'z'))){
				left++;
			}
			else {
				right--;
			}
		}
		return S;
	}
};
```


## 824. Goat Latin
```C++
class Solution {
public:
	string toGoatLatin(string S) {
		vector<string> res;
		if (!S.length()) return S;
		string tmp = "";
		for (int i = 0; i < S.length(); i++) {
			if (S[i] != ' ') tmp += S[i];
			else {
				res.push_back(tmp);
				tmp = "";
			}
		}
		res.push_back(tmp);

		int j = 0;
		for (auto i : res)
		{
			if (i[0] == 'a' || i[0] == 'e' || i[0] == 'i' || i[0] == 'o' || i[0] == 'u' || i[0] == 'A' || i[0] == 'E' || i[0] == 'I' || i[0] == 'O' || i[0] == 'U')
				i += "ma";
			else {
				string temp = "";
				if (i.length() > 1) {
					temp = i.substr(1, i.length() - 1);
					temp += i[0];
					i = temp;
				}
				i += "ma";
			}
			res[j++] = i;
		}
		j = 0;
		for (auto i : res)
		{
			int k = 0;
			while (k++ < (j + 1)) {
				i += "a";
			}
			res[j++] = i;
		}
		string result = "";
		for (auto i : res) {
			result += i;
			result += " ";
		}
		S = result.substr(0, result.length() - 1);
		return S;
	}
};
```
## 13. Roman to Integer
```C++
class Solution {
public:
	int romanToInt(string s) {		
		int res = 0;
		unordered_map<char, int> m{ {'I',1} ,{'V',5} , {'X',10} , {'L',50} , {'C',100} , {'D',500} , {'M',1000} };
		for (int i = 0; i < s.size(); i++) {
			int val = m[s[i]];
			if (i == s.size() - 1 || m[s[i + 1]] <= m[s[i]]) res += val;
			else res -= val;
		}
		return res;
	}
};
```
## 14. Longest Common Prefix
```C++
bool cmp(const string& s1, const string& s2) {
	return s1.size() < s2.size();
}

class Solution {
public:
	string longestCommonPrefix(vector<string>& strs) {
		if (strs.size() == 0) return "";
		string res = "";
		sort(strs.begin(), strs.end(), cmp);
		for (int j = 0; j < strs[strs.size() - 1].length(); j++) {
			int i = 0;
			while (i < (strs.size() - 1) && strs[i][j] == strs[i + 1][j]) i++;
			if (i == strs.size() - 1) res += strs[i][j];
			else break;
		}
		return res;
	}
};
```
## 20. Valid Parentheses
```C++
class Solution {
public:
	bool isValid(string s) {
		if (s.length() == 0) return true;
		stack<char> res;
		for (int i = 0; i < s.length(); i++) {
			if (s[i] == '(')
				res.push(')');
			else if (s[i] == '[')
				res.push(']');
			else if (s[i] == '{')
				res.push('}');
			else if (res.empty() || s[i] != res.top())
				return false;
			else res.pop();
		}
		return res.empty();
	}
};
```

```C++
```

# 3. 位运算
## 338. Counting Bits
```C++
class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> res;
        for(int i = 0;i <= num; i++){
            res.push_back(NumberOf1(i));
        }
        return res;
    }
    
    int NumberOf1(int num){
        int count = 0;
        while(num){
            count++;
            num = num & (num - 1);
        }
        return count;
    }
};
```
# 4. 哈希表
[哈希表](https://leetcode.com/problemset/all/?topicSlugs=hash-table)
## 136. Single Number
```C++
class Solution {
public:
	int singleNumber(vector<int>& nums) {
		if (nums.size() <= 0) return 0;
		int tmp = 0;
		for (int i = 0; i < nums.size(); i++) {
			tmp = tmp ^ nums[i];
		}
		return tmp;
	}
};
```

```C++

```

```C++

```

```C++

```
# 5. 链表
[链表](https://leetcode.com/problemset/all/?topicSlugs=linked-list)
## 21. Merge Two Sorted Lists
```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
	ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
		if (l1 == nullptr) return l2;
		if (l2 == nullptr) return l1;
		ListNode* lres = nullptr;
		if (l1->val <= l2->val) {
			lres = l1;
			lres->next = mergeTwoLists(l1->next, l2);
		}
		else {
			lres = l2;
			lres->next = mergeTwoLists(l1, l2->next);
		}
		return lres;
	}
};

```
非递归方法
```C++
class Solution {
public:
	ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
		if (l1 == nullptr) return l2;
		if (l2 == nullptr) return l1;
		ListNode head(0);
		ListNode *lres = &head;
		while (l1 != nullptr && l2 != nullptr) {
			if (l1->val <= l2->val) {
				lres->next = l1;
				l1 = l1->next;
			}
			else {
				lres->next = l2;
				l2 = l2->next;
			}
			lres = lres->next;
		}
		if (l1 != nullptr) {
			while (l1 != nullptr) {
				lres->next = l1;
				lres = lres->next;
				l1 = l1->next;
			}
		}
		else {
			while (l2 != nullptr) {
				lres->next = l2;
				lres = lres->next;
				l2 = l2->next;
			}
		}
		return head.next;
	}
};
```
## 83. Remove Duplicates from Sorted List
```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
	ListNode* deleteDuplicates(ListNode* head) {
		if (head == nullptr || head->next == nullptr) return head;
		ListNode* lres = head;
		ListNode* tmp = head->next;
		while (tmp != nullptr) {
			if (lres->val == tmp->val) {
				tmp = tmp->next;
			}
			else {
				lres->next = tmp;
				lres = tmp;
				tmp = tmp->next;
			}
		}
		lres->next = nullptr;
		return head;
	}
};
```
## 141. Linked List Cycle
```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
	bool hasCycle(ListNode *head) {
		if (head == nullptr || head->next == nullptr) return false;
		ListNode* slow = head;
		ListNode* fast = head;
		while (fast && fast->next) {
			slow = slow->next;
			fast = fast->next->next;
			if (slow == fast) return true;
		}
		return false;
	}
};
```
## 160. Intersection of Two Linked Lists
```C++
class Solution {
public:
	ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
		if (headA == nullptr || headB == nullptr) return nullptr;
		ListNode *nodeA = headA, *nodeB = headB;
		int lenA = 0, lenB = 0;
		while (nodeA != nullptr) {
			lenA++;
			nodeA = nodeA->next;
		}
		while (nodeB != nullptr) {
			lenB++;
			nodeB = nodeB->next;
		}
		if (lenA <= lenB) {
			for (int i = 0; i < lenB - lenA; i++) {
				headB = headB->next;
			}
		}
		else {
			for (int i = 0; i < lenA - lenB; i++) {
				headA = headA->next;
			}
		}
		while (headA != headB && headA != nullptr && headB != nullptr) {
			headA = headA->next;
			headB = headB->next;
		}
		if (headA != nullptr && headB != nullptr) return headA;
		else return nullptr ;
	}
};
```
## 203. Remove Linked List Elements
```C++
class Solution {
public:
	ListNode* removeElements(ListNode* head, int val) {
		if (head == nullptr) return head;
		while (head->val == val) {
			head = head->next;
			if (head == nullptr) return head;
		}
		ListNode *ptr = head;
		while (ptr->next!= nullptr)
		{
			if (ptr->next->val == val) {
				ptr->next = ptr->next->next;
			}
			else {
				ptr = ptr->next;
			}
		}
		return head;
	}
};
```
## 206. Reverse Linked List
```C++
class Solution {
public:
	ListNode* reverseList(ListNode* head) {
		ListNode *res = nullptr;
		ListNode *curNode = head;
		ListNode *preNode = nullptr;
		while (curNode != nullptr) {
			ListNode *nextNode = curNode->next;
			if (nextNode == nullptr) res = curNode;
			curNode->next = preNode;
			preNode = curNode;
			curNode = nextNode;
		}
		return res;
	}
};
```
## 234. Palindrome Linked List
```C++
#include <iostream>
#include <string>
#include <stack>
using namespace std;

struct ListNode
{	
	int val;
	ListNode *next;
	ListNode(int x) :val(x), next(NULL) {}
};

class Solution {
public:
	ListNode* reverse(ListNode *head) {
		ListNode *res = nullptr;
		ListNode *curNode = head;
		ListNode *preNode = nullptr;
		while (curNode != nullptr) {
			ListNode *nextNode = curNode->next;
			curNode->next = preNode;
			if (nextNode == nullptr) res = curNode;
			preNode = curNode;
			curNode = nextNode;
		}
		return res;
	}
	bool isPalindrome(ListNode* head) {
		if (head == nullptr) return true;
		ListNode *ptr = head;
		int len = 0;
		while (ptr != nullptr) {
			ptr = ptr->next;
			len++;
		}		
		if (len % 2 == 0) {
			len /= 2;			
		}
		else {
			len = len / 2 + 1;
		}
		ptr = head;
		while (len > 1) {
			ptr = ptr->next;
			len--;
		}
		ListNode *head2 = ptr->next;
		ptr->next = nullptr;
		head2 = reverse(head2);
		while (head2 != nullptr) {
			if (head2->val != head->val) return false;
			head = head->next;
			head2 = head2->next;
		}
		return true;
	}
};

//尾插法建立单链表
ListNode * Creat_LinkList_R()
{
	int x;
	ListNode *head, *p, *tail;                    //tail是尾指针
	head = (ListNode*)malloc(sizeof(ListNode));
	if (head == NULL)
		return head;
	head->next = NULL;
	tail = head;                                  //一开始尾指针指向头指针的位置
	cout << "请输入要录入的数以0结束" << endl;
	cin >> x;
	head->val = x;
	while ((cin >> x) && (x != 0))
	{
		p = (ListNode*)malloc(sizeof(ListNode));
		if (p == NULL)
			return head;
		p->val = x;
		tail->next = p;                          //将p插入到尾节点的后面
		tail = p;                                //修改尾节点的指向
		tail->next = NULL;                       //将尾节点的指针域修改为空
	}
	return head;
}

int main() {
	Solution s;
	ListNode *list1;
	list1 = Creat_LinkList_R();
	cout << s.isPalindrome(list1) << endl;
	system("pause");
	return 0;
}
```
## 237. Delete Node in a Linked List
```C++
class Solution {
public:
	void deleteNode(ListNode* node) {
		*node = *(node->next);
	}
};
```

```C++
class Solution {
public:
	void deleteNode(ListNode* node) {
		ListNode *tmp = node->next;
        *node = *tmp;
        delete tmp;
	}
};
```

## 707. Design Linked List
```C++
class MyLinkedList {
public:
	class MyLinkedListNode {
	public:
		int val;
		MyLinkedListNode* next = nullptr;
		MyLinkedListNode* prev = nullptr;
		MyLinkedListNode() :val{ 0 }, next{ nullptr }, prev{ nullptr } {};
	};

	MyLinkedListNode* root = nullptr;
	/** Initialize your data structure here. */
	MyLinkedList() {
		MyLinkedListNode* root{};
	}

	/** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
	int get(int index) {
		if (index < 0)
			return -1;
		MyLinkedListNode* tmp = root;
		if (tmp == nullptr) return -1;
		for (int i = 0; i < index; i++) {
			if (tmp->next != nullptr)
				tmp = tmp->next;
			else
				return -1;
		}
		return tmp->val;
	}

	/** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
	void addAtHead(int val) {
		MyLinkedListNode* newhead = new MyLinkedListNode();
		newhead->val = val;
		newhead->next = root;
		if (root != nullptr)
			root->prev = newhead;
		root = newhead;
	}

	/** Append a node of value val to the last element of the linked list. */
	void addAtTail(int val) {
		MyLinkedListNode* tail = root;
		while (tail != nullptr && tail->next != nullptr)
			tail = tail->next;
		MyLinkedListNode* newtail = new MyLinkedListNode();
		newtail->val = val;
		if (tail != nullptr)
			tail->next = newtail;
		else
			tail = newtail;
		newtail->prev = tail;
	}

	/** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
	void addAtIndex(int index, int val) {
		if (index <= 0) {
			addAtHead(val);
			return;
		}
		if (get(index - 1) != -1) {
			MyLinkedListNode* previous = root;
			MyLinkedListNode* newone = new MyLinkedListNode();
			newone->val = val;
			for (int i = 0; i < index - 1; i++)
			{
				previous = previous->next;
			}
			newone->prev = previous;
			newone->next = previous->next;
			if (previous->next != nullptr)
				previous->next->prev = newone;
			previous->next = newone;
			return;
		}
		else return;
	}

	/** Delete the index-th node in the linked list, if the index is valid. */
	void deleteAtIndex(int index) {
		if (index < 0) return;
		if (get(index) != -1) {
			MyLinkedListNode* tmp = root;
			for (int i = 0; i < index; i++) {
				tmp = tmp->next;
			}
			if (tmp->prev != nullptr)
				tmp->prev->next = tmp->next;
			if (tmp->next != nullptr)
				tmp->next->prev = tmp->prev;

			if (index == 0)
				root = tmp->next;
			return;
		}
		else return;
	}
};

int main() {
	MyLinkedList linkedList;
	linkedList.addAtHead(7);
	linkedList.addAtHead(2);
	linkedList.addAtHead(1);
	linkedList.addAtIndex(3, 0);  // linked list becomes 1->2->3
	linkedList.deleteAtIndex(2);  // now the linked list is 1->3
	linkedList.addAtHead(6);
	linkedList.addAtTail(4);
	linkedList.get(4);            // returns 2
	linkedList.addAtHead(4);
	linkedList.addAtIndex(5, 0);  // linked list becomes 1->2->3
	linkedList.addAtHead(6);
	system("pause");
	return 0;
}
```


```C++
```


```C++
```