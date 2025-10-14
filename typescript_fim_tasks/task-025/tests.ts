import { mergeSort } from './full_solution';

test('sorts numbers using merge sort', () => {
  expect(mergeSort([5, 2, 4, 6, 1, 3])).toEqual([1, 2, 3, 4, 5, 6]);
});

test('returns new array for single element', () => {
  const input = [1];
  const output = mergeSort(input);
  expect(output).toEqual([1]);
  expect(output).not.toBe(input);
});

test('handles empty array', () => {
  expect(mergeSort([])).toEqual([]);
});
