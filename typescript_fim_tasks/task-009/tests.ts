import { repeatPattern } from './full_solution';

test('repeats pattern to desired length', () => {
  expect(repeatPattern('ab', 5)).toBe('ababa');
});

test('handles empty pattern', () => {
  expect(repeatPattern('', 5)).toBe('');
});

test('throws for negative length', () => {
  expect(() => repeatPattern('ab', -1)).toThrow(RangeError);
});
