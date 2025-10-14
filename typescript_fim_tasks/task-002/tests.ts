import { areAnagrams } from './full_solution';

test('detects anagrams with punctuation ignored', () => {
  expect(areAnagrams('Conversation', 'Voices rant on!')).toBe(true);
});

test('detects non-anagrams when counts differ', () => {
  expect(areAnagrams('hello', 'heloo')).toBe(false);
});

test('handles numeric characters', () => {
  expect(areAnagrams('123', '321')).toBe(true);
});
