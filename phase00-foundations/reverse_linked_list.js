// Problem: FizzBuzz
// Approach: Brute Force

class Node {
  constructor(value, next = null) {
    this.value = value;
    this.next = next;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }

  append(value) {
    const newNode = new Node(value);

    if (!this.head) {
      this.head = newNode;
      return;
    }

    let lastNode = this.head;
    while (lastNode.next) {
      lastNode = lastNode.next;
    }

    lastNode.next = newNode;
  }

  reverseLinkedList() {
    let node = this.head;
    let reversedLLHead = null;

    while (node) {
      const newNode = new Node(node.value);

      if (!reversedLLHead) {
        reversedLLHead = newNode;
        node = node.next;
        continue;
      }

      newNode.next = reversedLLHead;
      reversedLLHead = newNode;

      node = node.next;
    }

    this.head = reversedLLHead;
  }

  print() {
    let lastNode = this.head;
    while (lastNode) {
      process.stdout.write(`${lastNode.value} -> `);
      lastNode = lastNode.next;
    }

    process.stdout.write("null\n");
  }
}

const ll = new LinkedList();
ll.append(10);
ll.append(20);
ll.append(6);

ll.print();

ll.reverseLinkedList();

ll.print();
