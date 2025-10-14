import { chunkArray } from './full_solution';

test('chunks array into equal parts', () => {
  expect(chunkArray([1, 2, 3, 4], 2)).toEqual([[1, 2], [3, 4]]);
});

test('handles remainder chunk', () => {
  expect(chunkArray([1, 2, 3, 4, 5], 2)).toEqual([[1, 2], [3, 4], [5]]);
});

test('throws on invalid size', () => {
  expect(() => chunkArray([1, 2, 3], 0)).toThrow('size must be greater than zero');
});
