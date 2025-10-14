/* Docstring:
 * Create a function `areAnagrams` that determines whether two input strings are anagrams of each other.
 * The function must ignore letter casing and non-alphanumeric characters while performing the comparison.
 * Return `true` only if both strings contain the same characters with the same multiplicity once normalized.
 */
<｜fim▁begin｜>
const normalize = (value: string): string =>
  Array.from(value.toLowerCase())
    .filter((char) => /[\p{Letter}\p{Number}]/u.test(char))
    .sort()
    .join("");

export function areAnagrams(first: string, second: string): boolean {
<｜fim▁hole｜>
  const normalizedFirst = normalize(first);
  const normalizedSecond = normalize(second);

  if (normalizedFirst.length !== normalizedSecond.length) {
    return false;
  }

  for (let index = 0; index < normalizedFirst.length; index += 1) {
    if (normalizedFirst[index] !== normalizedSecond[index]) {
      return false;
    }
  }

  return true;
<｜fim▁end｜>
}
