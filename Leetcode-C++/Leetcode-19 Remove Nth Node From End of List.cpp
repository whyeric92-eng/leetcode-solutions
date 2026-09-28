struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// 速记: *p 指针→对象(解引用)  &x 对象→指针(取地址)  p->m 等价于 (*p).m

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // dummy 节点: 统一处理"删除头节点"的情况
        // 变量第一次出现必须写类型, 不能写 dummy = ListNode();
        ListNode dummy(0, head);

        int len = 0;
        // head 本身就是指针, 指针赋给指针不加任何符号; *head 是节点对象, 类型对不上
        ListNode* num = head;
        while (num) {
            len += 1;
            num = num->next;
        }

        int index = len;
        // &dummy 是地址, 只能赋给指针, 不能写 ListNode cur = &dummy;
        // 引用 ListNode& cur = dummy; 绑定后不能改指向, 遍历链表要"换目标", 必须用指针
        ListNode* cur = &dummy;
        while (cur->next) {
            if (index == n) {
                cur->next = cur->next->next;
                break;  // 删完直接退出, 避免无意义的循环
            }
            index -= 1;
            cur = cur->next;
        }
        // 对象用 . 指针用 -> : dummy 是对象, 写 dummy->next 会报错
        return dummy.next;
    }
};
