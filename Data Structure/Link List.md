Array always is stored as one continuous block of memory. In some case, memory manager will create new block and copy the data from old array to add new data if there is no space for new data in old array. So no-continuous block, link list, is important to manager memory. Then i can create new node when i want and i can delete a node when i want.

### Link List Structure
```
struct Node
{
    data-type data;
    Node* next;
}
```
Data is stored the **Node** and each node stores the data as well as link to the next node So each node kind of points to the next node. First node is called **Head Node**, stores the link list address. So the address of head node kind of gives us access of the complete list. And the last node stores **NULL** to sign the end of the link list.
If i want access the element of the link list, i must ask the head node for the next node and then ask next node who is your next until find the target.
Head node can choose whether store data, but when we create a new link the head node points **NULL**.

<br />

### Implementation in C/C++

#### Easy sample in C/C++
Create a new link list and add a new node to store a data. (data-type is defined int)
In C:
```
Node* A;
A = NULL;
Node* temp = (Node*)malloc(sizeof(struct Node));
(*temp).data = 2;
(*temp).next = NULL;
A = temp;

```

In C++:
```
Node* A;
A = NULL;
Node* temp = new Node();
temp->data = 2;
temp->next = NULL;
A = temp;
```

#### Link List Funchtion
- Empty, list has size 0
- Insert
- Remove
- Count
- Read/Modify element at a position
- Specify adta-type

##### Function of Empty

##### Function of Insert

##### Function of Remove

##### Function of Count

##### Function of 

##### Function of Remove