import { uniqueNumbers } from './full_solution';

test('removes duplicates preserving order', () => {
  expect(uniqueNumbers([1, 2, 1, 3, 2])).toEqual([1, 2, 3]);
});

test('handles negative numbers', () => {
  expect(uniqueNumbers([-1, -1, -2])).toEqual([-1, -2]);
});

test('treats NaN as a single unique value', () => {
  const result = uniqueNumbers([NaN, NaN, 1]);
  expect(result.length).toBe(2);
  expect(Number.isNaN(result[0])).toBe(true);
  expect(result[1]).toBe(1);
});
