import { findKthSmallest } from './full_solution';

test('finds first smallest', () => {
  expect(findKthSmallest([3, 1, 2], 1)).toBe(1);
});

test('finds middle element', () => {
  expect(findKthSmallest([7, 4, 6, 3, 9, 1], 3)).toBe(4);
});

test('throws on invalid k', () => {
  expect(() => findKthSmallest([1, 2, 3], 0)).toThrow(RangeError);
});
