import { groupByParity } from './full_solution';

test('splits numbers by parity', () => {
  expect(groupByParity([1, 2, 3, 4])).toEqual({ even: [2, 4], odd: [1, 3] });
});

test('handles empty input', () => {
  expect(groupByParity([])).toEqual({ even: [], odd: [] });
});

test('preserves order', () => {
  expect(groupByParity([3, 2, 2, 5]).even).toEqual([2, 2]);
});
