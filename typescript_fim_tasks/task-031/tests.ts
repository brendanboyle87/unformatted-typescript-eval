import { deepClone } from './full_solution';

test('clones nested objects', () => {
  const original = { a: { b: 1 } };
  const copy = deepClone(original);
  expect(copy).toEqual(original);
  expect(copy).not.toBe(original);
  expect(copy.a).not.toBe(original.a);
});

test('clones arrays', () => {
  const original = [1, [2, 3]];
  const copy = deepClone(original);
  expect(copy).toEqual(original);
  expect(copy[1]).not.toBe(original[1]);
});

test('clones dates', () => {
  const date = new Date();
  const copy = deepClone(date);
  expect(copy).not.toBe(date);
  expect(copy.getTime()).toBe(date.getTime());
});
