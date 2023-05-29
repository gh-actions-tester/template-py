// EXAMPLE TEST
// Expacted solution file is uploaded to the root of the project
var solution_file = "../index";

const {sum} = require(solution_file);

test("add 1 and 2 together", () => {
	expect(sum(1, 2)).toBe(3);
});

test("add 2 and 2 together", () => {
	expect(sum(2, 2)).toBe(4);
});

test("add 3 and 2 together", () => {
	expect(sum(3, 2)).toBe(5);
});

test("add 4 and 2 together", () => {
	expect(sum(4, 2)).toBe(6);
});

test("add 5 and 2 together", () => {
	expect(sum(5, 2)).toBe(7);
});

test("add 5 and 2 together is 1?", () => {
	expect(sum(5, 2)).toBe(1);
});

test("add 5 and 2 together is 2?", () => {
	expect(sum(5, 2)).toBe(2);
});
