import { rotateArray } from './full_solution';

test('rotates to the right', () => {
  expect(rotateArray([1, 2, 3, 4], 1)).toEqual([4, 1, 2, 3]);
});

test('rotates to the left when negative', () => {
  expect(rotateArray([1, 2, 3, 4], -1)).toEqual([2, 3, 4, 1]);
});

test('handles rotation greater than length', () => {
  expect(rotateArray([1, 2, 3], 5)).toEqual([2, 3, 1]);
});
