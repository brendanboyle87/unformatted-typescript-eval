const BASE_VOWELS = new Set(['a', 'e', 'i', 'o', 'u']);

export function countVowels(text: string, includeY = false): number {
  let total = 0;
  for (const char of text.toLowerCase()) {
    if (BASE_VOWELS.has(char) || (includeY && char === 'y')) {
      total += 1;
    }
  }
  return total;
}
