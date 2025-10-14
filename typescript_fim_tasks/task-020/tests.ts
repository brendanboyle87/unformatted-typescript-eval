import { mergeSortedArrays } from './full_solution';

test('merges two sorted arrays', () => {
  expect(mergeSortedArrays([1, 3, 5], [2, 4, 6])).toEqual([1, 2, 3, 4, 5, 6]);
});

test('includes duplicates', () => {
  expect(mergeSortedArrays([1, 2, 2], [2, 3])).toEqual([1, 2, 2, 2, 3]);
});

test('handles empty arrays', () => {
  expect(mergeSortedArrays([], [1, 2])).toEqual([1, 2]);
});
