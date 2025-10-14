import { partitionByPivot } from './full_solution';

test('orders values around pivot', () => {
  expect(partitionByPivot([3, 5, 2, 5, 1], 5)).toEqual([3, 2, 1, 5, 5]);
});

test('preserves relative order within groups', () => {
  expect(partitionByPivot([1, 2, 3, 4], 3)).toEqual([1, 2, 3, 4]);
});

test('handles no pivot matches', () => {
  expect(partitionByPivot([1, 2, 3], 0)).toEqual([1, 2, 3]);
});
