import { deepMerge } from './full_solution';

test('merges nested objects', () => {
  const merged = deepMerge({ a: { b: 1 } }, { a: { c: 2 } });
  expect(merged).toEqual({ a: { b: 1, c: 2 } });
});

test('concatenates arrays', () => {
  const merged = deepMerge({ tags: ['a'] }, { tags: ['b'] });
  expect(merged.tags).toEqual(['a', 'b']);
});

test('overwrites primitive values', () => {
  expect(deepMerge({ count: 1 }, { count: 2 })).toEqual({ count: 2 });
});
