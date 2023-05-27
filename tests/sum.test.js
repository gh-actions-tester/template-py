// EXAMPLE TEST
// Expacted solution file is uploaded to the root of the project
var solution_file = "../index";

const { sum } = require(solution_file);
test("add 1 and 2 together", () => {
	expect(sum(1, 2)).toBe(3);
});
