/* Docstring:
 * Implement `findMissingNumbers` to identify the integers missing from a sequence.
 * Given an array of integers (in any order), return the numbers that do not appear between the minimum and maximum values inclusive.
 * Return an empty array when the input is empty or contains a complete range.
 */
<｜fim▁begin｜>
export function findMissingNumbers(values: number[]): number[] {
<｜fim▁hole｜>
  if (values.length === 0) {
    return [];
  }

  const min = Math.min(...values);
  const max = Math.max(...values);
  const set = new Set(values);
  const missing: number[] = [];

  for (let number = min; number <= max; number += 1) {
    if (!set.has(number)) {
      missing.push(number);
    }
  }

  return missing;
<｜fim▁end｜>
}
