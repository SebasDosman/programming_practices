//const array = ["Juan", "Sebastian", "Oscar"]

class MyArray {
  constructor() {
    this.lenght = 0;
    this.data = {};
  }

  get(index) {
    return this.data[index];
  }

  push(item) {
    this.data[this.lenght] = item;
    this.lenght++;
    return this.data;
  }

  pop() {
    const lastItem = this.data[this.lenght - 1];
    delete this.data[this.lenght - 1];
    this.lenght--;
    return lastItem;
  }

  delete(index) {
    const itemIndex = this.data[index];
    this.shiftIndex(index);
    return itemIndex;
  }

  shiftIndex(index) {
    for (let i = index; i < this.lenght - 1; i++) {
      this.data[i] = this.data[i + 1];
    }

    delete this.data[this.lenght - 1];
    this.lenght--;
  }

  unShift(index) {
    for (let i = this.length; i > 0; i--) {
      this.data[i] = this.data[i - 1];
    }

    this.data[0] = index;
    this.length++;
    return this.data;
  }
}

const myArray = new MyArray();