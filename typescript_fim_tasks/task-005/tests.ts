import { countVowels } from './full_solution';

test('counts vowels in lowercase', () => {
  expect(countVowels('hello world')).toBe(3);
});

test('is case insensitive', () => {
  expect(countVowels('AEIOU')).toBe(5);
});

test('optionally counts y', () => {
  expect(countVowels('rhythms', true)).toBe(1);
});
