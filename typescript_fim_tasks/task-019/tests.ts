import { filterTruthy } from './full_solution';

test('filters out falsy values', () => {
  expect(filterTruthy([0, 1, '', 'hello', null, undefined])).toEqual([1, 'hello']);
});

test('preserves true booleans', () => {
  expect(filterTruthy([false, true, true])).toEqual([true, true]);
});

test('handles empty array', () => {
  expect(filterTruthy([])).toEqual([]);
});
