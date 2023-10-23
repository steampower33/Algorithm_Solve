#include "cpp.hpp"

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
		ListNode *result = new ListNode();
		ListNode *tmp = result;
		int	plus = 0;

		while (l1 || l2)
		{
			if (l1)
				tmp->val += l1->val;
			if (l2)
				tmp->val += l2->val;
			if (tmp->val >= 10)
			{
				plus = 1;
				tmp->val -= 10;
			}
			if (l1)
				l1 = l1->next;
			if (l2)
				l2 = l2->next;
			if (l1 || l2 || plus)
			{
				if (plus == 1)
					tmp->next = new ListNode(1);
				else
					tmp->next = new ListNode();
				plus = 0;
				tmp = tmp->next;
			}
		}
		return (result);
    }
};

int main(void)
{
	Solution s;

	vector<int> v1 = {9,9,9,9,9,9,9};
	vector<int> v2 = {9,9,9,9};
	ListNode *a = new ListNode();
	ListNode *b = new ListNode();
	ListNode *tmp_a;
	ListNode *tmp_b;

	tmp_a = a;
	for(int i = 0; i < v1.size(); i++)
	{
		a->val = v1[i];
		if (i != v1.size() - 1)
			a->next = new ListNode();
		cout << a->val << " ";
		a = a->next;
	}
	cout << endl;

	tmp_b = b;
	for(int i = 0; i < v2.size(); i++)
	{
		b->val = v2[i];
		if (i != v2.size() - 1)
			b->next = new ListNode();
		cout << b->val << " ";
		b = b->next;
	}
	cout << endl;

	ListNode *result = s.addTwoNumbers(tmp_a, tmp_b);
	for (ListNode *node = result; node != nullptr; node = node->next)
	{
		cout << result->val << " ";
		result = result->next;
	}
	cout << endl;

}