import { mapKeys } from './full_solution';

test('renames keys with mapper', () => {
  const result = mapKeys({ firstName: 'Ada', lastName: 'Lovelace' }, (key) => key.toUpperCase());
  expect(result).toEqual({ FIRSTNAME: 'Ada', LASTNAME: 'Lovelace' });
});

test('handles key collisions by overwriting', () => {
  const result = mapKeys({ a: 1, b: 2 }, () => 'same');
  expect(result).toEqual({ same: 2 });
});

test('works with empty objects', () => {
  expect(mapKeys({}, (key) => String(key))).toEqual({});
});
