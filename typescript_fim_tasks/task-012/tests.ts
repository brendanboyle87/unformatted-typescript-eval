import { flattenOneLevel } from './full_solution';

test('flattens arrays one level deep', () => {
  expect(flattenOneLevel([1, [2, 3], 4])).toEqual([1, 2, 3, 4]);
});

test('preserves nested arrays beyond one level', () => {
  expect(flattenOneLevel([1, [2, [3]], 4])).toEqual([1, 2, [3], 4]);
});

test('handles empty array', () => {
  expect(flattenOneLevel<number>([])).toEqual([]);
});
