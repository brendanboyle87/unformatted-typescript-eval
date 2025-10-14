import { findMissingNumbers } from './full_solution';

test('finds missing numbers within range', () => {
  expect(findMissingNumbers([1, 4, 2])).toEqual([3]);
});

test('returns empty for continuous sequence', () => {
  expect(findMissingNumbers([3, 2, 1])).toEqual([]);
});

test('handles empty input', () => {
  expect(findMissingNumbers([])).toEqual([]);
});
