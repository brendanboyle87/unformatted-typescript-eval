import { reverseString } from './full_solution';

test('reverses ascii word', () => {
  expect(reverseString('hello')).toBe('olleh');
});

test('handles empty string', () => {
  expect(reverseString('')).toBe('');
});

test('reverses unicode characters', () => {
  expect(reverseString('🙂🙃')).toBe('🙃🙂');
});
