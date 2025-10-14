/* Docstring:
 * Implement `binarySearch` to locate a target number within a sorted ascending array of numbers.
 * Return the index of the target if found or `-1` otherwise.
 * Use an iterative binary search algorithm with `O(log n)` complexity.
 */
<｜fim▁begin｜>
export function binarySearch(values: number[], target: number): number {
<｜fim▁hole｜>
  let low = 0;
  let high = values.length - 1;

  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    const value = values[mid];

    if (value === target) {
      return mid;
    }

    if (value < target) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }

  return -1;
<｜fim▁end｜>
}
