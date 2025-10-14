import { countingSort } from './full_solution';

test('sorts non-negative integers', () => {
  expect(countingSort([3, 1, 2, 1])).toEqual([1, 1, 2, 3]);
});

test('handles empty array', () => {
  expect(countingSort([])).toEqual([]);
});

test('throws on negative input', () => {
  expect(() => countingSort([1, -1])).toThrow('countingSort only accepts non-negative integers');
});
