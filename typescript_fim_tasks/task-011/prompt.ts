/* Docstring:
 * Implement `uniqueNumbers` to return an array containing only the first occurrence of each number in the input sequence.
 * Preserve the original order of the numbers and do not mutate the provided array.
 * The function should handle negative numbers and `NaN` values correctly.
 */
<｜fim▁begin｜>
export function uniqueNumbers(values: number[]): number[] {
<｜fim▁hole｜>
  const seen = new Set<number>();
  let seenNaN = false;
  const result: number[] = [];

  for (const value of values) {
    if (Number.isNaN(value)) {
      if (!seenNaN) {
        seenNaN = true;
        result.push(value);
      }
      continue;
    }

    if (!seen.has(value)) {
      seen.add(value);
      result.push(value);
    }
  }

  return result;
<｜fim▁end｜>
}
