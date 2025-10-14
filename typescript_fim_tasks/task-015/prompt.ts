/* Docstring:
 * Implement `getTopNElements` to return the largest `n` numbers from an array sorted in descending order.
 * The original array must remain unchanged and `n` should be clamped between zero and the array length.
 * Handle duplicate numbers by including them according to their frequency.
 */
<｜fim▁begin｜>
export function getTopNElements(values: number[], n: number): number[] {
<｜fim▁hole｜>
  if (n <= 0) {
    return [];
  }

  const count = Math.min(n, values.length);
  const copy = [...values];
  copy.sort((a, b) => b - a);
  return copy.slice(0, count);
<｜fim▁end｜>
}
