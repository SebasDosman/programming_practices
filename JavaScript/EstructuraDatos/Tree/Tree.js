class Node {
  constructor(value) {
    this.value = value;
    this.right = null;
    this.left = null;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
  }

  insert(value) {
    const newNode = new Node(value);

    if (this.root === null) {
      this.root = newNode;
    } else {
      let current = this.root;

      while (true) {
        if (value < current.value) {
          if (!current.left) {
            current.left = newNode;
            return this;
          }

          current = current.left;
        } else if (!current.right) {
          current.right = newNode;
          return this;
        }

        current = current.right;
      }
    }
  }

  search(value, tree = this.root) {
    if (!this.root) {
      return console.error("The Binary Search Tree is empty");
    }

    if (!tree) {
      return console.error("The node is not in the tree");
    }

    if (value < tree.value) {
      return this.search(value, tree.left);
    } else if (value > tree.value) {
      return this.search(value, tree.rigth);
    } else {
      console.log("The value has been finded in the Tree");
      return tree;
    }
  }

  delete(value) {
    if (!this.root) {
      return console.error("The Binary Search Tree is empty");
    }
    if (value === this.root.value) {
      delete this.root;
      return this;
    }

    let pointer = this.root;

    while (pointer) {
      if (value < pointer.value) {
        if (pointer.left && value === pointer.left.value) {
          pointer.left = null;
          return this;
        }
        pointer = pointer.left;
      } else if (pointer.rigth && value === pointer.rigth.value) {
        pointer.rigth = null;
        return this;
      }
      pointer = pointer.rigth;
    }
  }
}
