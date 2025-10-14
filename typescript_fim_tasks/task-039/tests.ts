import { filterObject } from './full_solution';

test('filters values based on predicate', () => {
  expect(filterObject({ a: 1, b: 2, c: 3 }, (value) => value > 1)).toEqual({ b: 2, c: 3 });
});

test('returns empty object when nothing matches', () => {
  expect(filterObject({ a: 1 }, () => false)).toEqual({});
});

test('passes key to predicate', () => {
  const result = filterObject({ keep: true, drop: false }, (_value, key) => key === 'keep');
  expect(result).toEqual({ keep: true });
});
