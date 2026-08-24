
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode();
        // 声明的时候如果不初始化 就是野指针 指向随机内存
        // 创建这个新的对象要用 new 
        ListNode* cur = dummy;
        int val1,val2,x;
        // 同一个变量在同一作用域内,只能声明(带类型)一次,之后使用只写变量名
        int temp=0;
        while (l1 && l2) {
            // 不推荐写and 推荐写&&
            val1=l1? l1->val: 0;
            val2=l2? l2->val: 0;
            x=(val1+val2+temp)%10;
            temp=(val1+val2+temp)/10;
            // c++的整除是/ 和python(向下取整)不太一样 c++是向0截断
            cur->next=new ListNode(x);
            cur=cur->next;
            l1=l1->next;
            l2=l2->next;
        }
        while (l1) {
            val1=l1->val;
            x=(val1+temp)%10;
            temp=(val1+temp)/10;
            cur->next=new ListNode(x);
            cur=cur->next;
            l1=l1->next;
        }
        while (l2) {
            val2=l2->val;
            x=(val2+temp)%10;
            temp=(val2+temp)/10;
            cur->next=new ListNode(x);
            cur=cur->next;
            l2=l2->next;
        }
        if (temp!=0) {
            cur->next=new ListNode(temp);
        }
        return dummy->next;
    }
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode();
        ListNode* cur = dummy;
        int carry = 0;

        while (l1 || l2 || carry) {
            int val1 = l1 ? l1->val : 0;
            int val2 = l2 ? l2->val : 0;
            int sum = val1 + val2 + carry;

            carry = sum / 10;
            cur->next = new ListNode(sum % 10);
            cur = cur->next;

            if (l1) l1 = l1->next;
            if (l2) l2 = l2->next;
        }

        ListNode* result = dummy->next;  // 先存下真正要返回的链表头
        delete dummy;                    // 再释放 dummy 这个哨兵节点
        return result;
    }
};


// 节约额外空间 in-place修改
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode();  // 这个还是要 new,但只有这一个
        ListNode* cur = dummy;
        int carry = 0;

        while (l1 || l2 || carry) {
            int val1 = l1 ? l1->val : 0;
            int val2 = l2 ? l2->val : 0;
            int sum = val1 + val2 + carry;
            carry = sum / 10;

            if (l1) {
                l1->val = sum % 10;   // 复用 l1 的节点,直接改值
                cur->next = l1;
                l1 = l1->next;
            } else if (l2) {
                l2->val = sum % 10;   // l1 用完了,复用 l2 的节点
                cur->next = l2;
                l2 = l2->next;
            } else {
                cur->next = new ListNode(sum % 10);  // 两条链表都用完了,只剩进位,才需要新建
            }
            cur = cur->next;
        }

        ListNode* result = dummy->next;
        delete dummy;
        return result;
    }
};