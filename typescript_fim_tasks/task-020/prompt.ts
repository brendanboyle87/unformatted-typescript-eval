/* Docstring:
 * Implement `mergeSortedArrays` to merge two sorted arrays of numbers into a single sorted array.
 * Both inputs are sorted in ascending order; the result should also be ascending and include duplicates.
 * The original arrays must not be modified.
 */
<｜fim▁begin｜>
export function mergeSortedArrays(left: number[], right: number[]): number[] {
<｜fim▁hole｜>
  const result: number[] = [];
  let i = 0;
  let j = 0;

  while (i < left.length && j < right.length) {
    if (left[i] <= right[j]) {
      result.push(left[i]);
      i += 1;
    } else {
      result.push(right[j]);
      j += 1;
    }
  }

  while (i < left.length) {
    result.push(left[i]);
    i += 1;
  }

  while (j < right.length) {
    result.push(right[j]);
    j += 1;
  }

  return result;
<｜fim▁end｜>
}
