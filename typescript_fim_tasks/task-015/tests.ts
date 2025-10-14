import { getTopNElements } from './full_solution';

test('returns top elements', () => {
  expect(getTopNElements([5, 1, 3, 4], 2)).toEqual([5, 4]);
});

test('handles n larger than array length', () => {
  expect(getTopNElements([1, 2], 5)).toEqual([2, 1]);
});

test('returns empty when n <= 0', () => {
  expect(getTopNElements([1, 2, 3], 0)).toEqual([]);
});
