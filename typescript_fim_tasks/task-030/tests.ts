import { interpolationSearch } from './full_solution';

const values = [10, 20, 30, 40, 50, 60, 70];

test('finds existing value', () => {
  expect(interpolationSearch(values, 50)).toBe(4);
});

test('returns -1 for missing value', () => {
  expect(interpolationSearch(values, 55)).toBe(-1);
});

test('handles uniform values', () => {
  expect(interpolationSearch([5, 5, 5, 5], 5)).toBe(0);
});
