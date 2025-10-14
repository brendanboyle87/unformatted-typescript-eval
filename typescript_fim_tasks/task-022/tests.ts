import { quickSortStrings } from './full_solution';

test('sorts strings ignoring case', () => {
  expect(quickSortStrings(['Banana', 'apple', 'cherry'])).toEqual(['apple', 'Banana', 'cherry']);
});

test('handles already sorted list', () => {
  expect(quickSortStrings(['a', 'b', 'c'])).toEqual(['a', 'b', 'c']);
});

test('handles duplicates', () => {
  expect(quickSortStrings(['a', 'A', 'b'])).toEqual(['a', 'A', 'b']);
});
