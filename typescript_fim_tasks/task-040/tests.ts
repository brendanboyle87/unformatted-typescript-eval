import { invertObject } from './full_solution';

test('inverts keys and values', () => {
  expect(invertObject({ a: 'x', b: 'y' })).toEqual({ x: 'a', y: 'b' });
});

test('stringifies non-string values', () => {
  expect(invertObject({ a: 1, b: true })).toEqual({ '1': 'a', true: 'b' });
});

test('later values overwrite earlier ones', () => {
  expect(invertObject({ a: 'x', b: 'x' })).toEqual({ x: 'b' });
});
