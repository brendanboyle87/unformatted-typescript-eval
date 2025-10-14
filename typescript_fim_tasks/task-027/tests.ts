import { searchMatrix } from './full_solution';

const matrix = [
  [1, 3, 5],
  [7, 9, 11],
  [13, 15, 17],
];

test('finds existing value', () => {
  expect(searchMatrix(matrix, 9)).toBe(true);
});

test('returns false for missing value', () => {
  expect(searchMatrix(matrix, 10)).toBe(false);
});

test('handles empty matrix', () => {
  expect(searchMatrix([], 1)).toBe(false);
});
