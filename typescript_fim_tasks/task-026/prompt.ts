/* Docstring:
 * Implement `findKthSmallest` to return the k-th smallest number in an unsorted array.
 * The function should use a selection algorithm with average `O(n)` time complexity and not mutate the input array.
 * Throw a `RangeError` when `k` is out of bounds (less than 1 or greater than the array length).
 */
<｜fim▁begin｜>
const partition = (array: number[], left: number, right: number, pivotIndex: number): number => {
  const pivotValue = array[pivotIndex];
  [array[pivotIndex], array[right]] = [array[right], array[pivotIndex]];
  let storeIndex = left;

  for (let i = left; i < right; i += 1) {
    if (array[i] < pivotValue) {
      [array[i], array[storeIndex]] = [array[storeIndex], array[i]];
      storeIndex += 1;
    }
  }

  [array[right], array[storeIndex]] = [array[storeIndex], array[right]];
  return storeIndex;
};

export function findKthSmallest(values: number[], k: number): number {
<｜fim▁hole｜>
  if (k < 1 || k > values.length) {
    throw new RangeError('k is out of range');
  }

  const array = [...values];
  let left = 0;
  let right = array.length - 1;
  const target = k - 1;

  while (true) {
    const pivotIndex = partition(array, left, right, Math.floor((left + right) / 2));

    if (pivotIndex === target) {
      return array[pivotIndex];
    }

    if (target < pivotIndex) {
      right = pivotIndex - 1;
    } else {
      left = pivotIndex + 1;
    }
  }
<｜fim▁end｜>
}
