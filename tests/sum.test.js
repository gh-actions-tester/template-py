const { sum } = require("../index");

test("add 1 and 2 together", () => {
  expect(sum(1, 2)).toBe(3);
});
