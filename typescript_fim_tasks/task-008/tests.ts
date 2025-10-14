import { padCenter } from './full_solution';

test('centers string with spaces', () => {
  expect(padCenter('cat', 7)).toBe('  cat  ');
});

test('prefers extra padding on the right', () => {
  expect(padCenter('go', 5, '.')).toBe('.go..');
});

test('throws when padChar is invalid', () => {
  expect(() => padCenter('test', 6, 'xx')).toThrow('padChar must be exactly one character');
});
