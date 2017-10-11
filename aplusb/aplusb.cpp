#include <algorithm>
#include <chrono>
#include <iostream>
#include <unordered_map>

using namespace std;
using std::max;
using std::chrono::high_resolution_clock;
using std::chrono::duration_cast;

struct Node
{
    int key;
    int index;
    Node *left;
    Node *right;
    int height;
};

int height(Node *N)
{
    if (N == NULL)
        return 0;
    return N->height;
}

struct Node* newNode(int key, int index)
{
    struct Node* node = (Node*)
                        malloc(sizeof(Node));
    node->key    = key;
    node->index  = index;
    node->left   = NULL;
    node->right  = NULL;
    node->height = 1;
    return(node);
}

struct Node *rightRotate(Node *y)
{
    Node *x = y->left;
    Node *T2 = x->right;

    x->right = y;
    y->left = T2;

    y->height = max(height(y->left), height(y->right))+1;
    x->height = max(height(x->left), height(x->right))+1;

    return x;
}

struct Node *leftRotate(Node *x)
{
    Node *y = x->right;
    Node *T2 = y->left;

    y->left = x;
    x->right = T2;

    x->height = max(height(x->left), height(x->right))+1;
    y->height = max(height(y->left), height(y->right))+1;

    return y;
}

int getBalance(Node *N)
{
    if (N == NULL)
        return 0;
    return height(N->left) - height(N->right);
}

struct Node* insert(Node* node, int key, int index)
{
    if (node == NULL)
        return(newNode(key, index));

    if (key < node->key)
        node->left  = insert(node->left, key, index);
    else if (key > node->key)
        node->right = insert(node->right, key, index);
    else
        return node;

    node->height = 1 + max(height(node->left),
                           height(node->right));

    int balance = getBalance(node);

    if (balance > 1 && key < node->left->key)
        return rightRotate(node);

    if (balance < -1 && key > node->right->key)
        return leftRotate(node);

    if (balance > 1 && key > node->left->key)
    {
        node->left =  leftRotate(node->left);
        return rightRotate(node);
    }

    if (balance < -1 && key < node->right->key)
    {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }

    return node;
}

int minIndex(Node *node, int value)
{
    Node *prevNode;
    while (node != NULL) {
        if (node->key == value)
            return node->index;

        prevNode = node;
        node = value < node->key ? node->left : node->right;
    }
    return prevNode->index;
}

int main()
{
    auto t1 = high_resolution_clock::now();
    int N, i, j = 0;
    int maxNum;
    int size;
    cin >> N;
    struct Node *tree = NULL;

    int nums[N];
    unordered_map<int, int> numCount;
    for (i = 0; i < N; i++) {
        cin >> maxNum;
//        numCount[maxNum]++;
//        if (numCount[maxNum] == 1) {
//            tree = insert(tree, maxNum, j);
//            nums[j++] = maxNum;
//        }
    }

//    size = numCount.size();
//    for (i = 0; i < size; i++) {
//        for (j = max(i, 50000-i); j < size; j++) {

//        }
//    }

    cout << duration_cast<chrono::microseconds>(high_resolution_clock::now()-t1).count()*0.000001 << endl;
    return 0;
}
