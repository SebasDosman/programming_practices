//Edge List

const graph = [
  [0, 2],
  [2, 3],
  [2, 1],
  [1, 3],
];

//Adjacent List

const graph1 = [[2], [2, 3], [0, 1, 3], [1, 2]];

//Object

const graph2 = {
  0: [2],
  1: [2, 3],
  2: [0, 1, 3],
  3: [1, 2],
};

//Adjacent Matrix

const graph3 = [
  [0, 0, 1, 0],
  [0, 0, 1, 1],
  [1, 1, 0, 1],
  [0, 1, 1, 0],
];

//Object Matrix

const graph4 = {
  0: [0, 0, 1, 0],
  1: [0, 0, 1, 1],
  2: [1, 1, 0, 1],
  3: [0, 1, 1, 0],
};
