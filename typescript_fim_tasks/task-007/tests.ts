import { truncateString } from './full_solution';

test('returns original when below limit', () => {
  expect(truncateString('hello', 10)).toBe('hello');
});

test('applies ellipsis when truncated', () => {
  expect(truncateString('typescript', 6)).toBe('type…');
});

test('throws on negative length', () => {
  expect(() => truncateString('test', -1)).toThrow(RangeError);
});
