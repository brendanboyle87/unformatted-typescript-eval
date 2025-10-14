import { diffObjects } from './full_solution';

test('detects updated values', () => {
  expect(diffObjects({ a: 1 }, { a: 2 })).toEqual({ a: { before: 1, after: 2 } });
});

test('detects removed keys', () => {
  expect(diffObjects({ a: 1 }, {})).toEqual({ a: { before: 1, after: undefined } });
});

test('detects added keys', () => {
  expect(diffObjects({}, { b: 2 })).toEqual({ b: { before: undefined, after: 2 } });
});
