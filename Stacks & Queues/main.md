# Stacks & Queues
Java is used for reference

Stacks & Queues are data structure. So, it's important to understand difference between datat types and data structures

<hr>

## Data Structure VS Data Type

### Data Structure

1. Data structure represents data.
2. Data structures reflect relationship between data.
3. Some are built-in like arrays and dictionaries. (depends on the language)
4. Others are not like linked list and treemap.

### Data Type

1. Data types are set of value.
2. There are set of operations available on those values. (Eg:- concat on strings)
3. Examples of built in data types are int, boolean, and string.
4. Examples for user-defined data types can be anything like User, Person, Client, and Post.

<hr>

A collection is an abstract data type whose values are multiset of items(same data type).

Stack & Queue differ in way of their operation.

### Stack Operations

1. Add item to the collection.
2. Remove & return the "most" recent item.
3. Works on "LIFO" priciple i.e last in first out.
4. Returns the size of collection.
5. Verify is it's not empty.

#### Example:-

Operations available on stack are push(add) and pop(remove).

Suppose you add '5' to the existing stack [4,3,2,1]. Then it would be [5,4,3,2,1].

And if your pop an item, it would be '5' due to LIFO principle.

### Queue Operations

1. Add item to the collection.
2. Remove & return the "least" recent item.
3. Works on "FIFO" priciple i.e first in first out.
4. Returns the size of collection.
5. Verify is it's not empty.

#### Example:-

Operations available on stack are enqueue(add) and dequeue(remove).

Suppose you add '5' to the existing stack [1,2,3,4]. Then it would be [1,2,3,4,5].

And if your pop an item, it would be '1' due to FIFO principle.

<hr>

### Performance Specifications

Performance matters. So, it's very important to provide guaranteed performance for a data structure.

Following are the performance specifications for a stacks & queues.

1. All operations must take constant time.
2. Shouldn't waste memory. Usage must be linear in the size of collection (when non-empty).
3. No limit in the code for collection size.

Performance playes key role in the implementation of data structure. It's not an stack/queue if there's no constant time for each operation. It can be a different type of data structure but not stack or queue.
