import { bubbleSortNumbers } from './full_solution';

test('sorts numbers ascending', () => {
  expect(bubbleSortNumbers([3, 2, 5, 1])).toEqual([1, 2, 3, 5]);
});

test('handles already sorted array efficiently', () => {
  expect(bubbleSortNumbers([1, 2, 3])).toEqual([1, 2, 3]);
});

test('works with duplicates', () => {
  expect(bubbleSortNumbers([3, 3, 2])).toEqual([2, 3, 3]);
});
