import { omitKeys } from './full_solution';

test('omits specified keys', () => {
  expect(omitKeys({ a: 1, b: 2, c: 3 }, ['b'])).toEqual({ a: 1, c: 3 });
});

test('handles empty keys array', () => {
  expect(omitKeys({ a: 1 }, [])).toEqual({ a: 1 });
});

test('ignores keys not present', () => {
  expect(omitKeys<Record<string, number>, string>({ a: 1 }, ['missing'])).toEqual({ a: 1 });
});
