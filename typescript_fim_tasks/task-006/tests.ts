import { snakeToCamel } from './full_solution';

test('converts simple snake to camel', () => {
  expect(snakeToCamel('hello_world')).toBe('helloWorld');
});

test('handles consecutive underscores', () => {
  expect(snakeToCamel('__make__everything__work__')).toBe('makeEverythingWork');
});

test('preserves lowercase first segment', () => {
  expect(snakeToCamel('Already_Lower')).toBe('alreadyLower');
});
