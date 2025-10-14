/* Docstring:
 * Write a function `countVowels` that counts the number of vowel characters in a string.
 * The function accepts a boolean flag `includeY` that, when true, counts the letter `y` as a vowel.
 * Return the total number of matching characters while treating the input case-insensitively.
 */
<｜fim▁begin｜>
const BASE_VOWELS = new Set(['a', 'e', 'i', 'o', 'u']);

export function countVowels(text: string, includeY = false): number {
<｜fim▁hole｜>
  let total = 0;
  for (const char of text.toLowerCase()) {
    if (BASE_VOWELS.has(char) || (includeY && char === 'y')) {
      total += 1;
    }
  }
  return total;
<｜fim▁end｜>
}
