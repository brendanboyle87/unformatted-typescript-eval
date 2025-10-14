/* Docstring:
 * Implement `mergeSort` to sort an array of numbers in ascending order using the merge sort algorithm.
 * The function should recursively divide the array and merge sorted halves, returning a new array.
 * Do not mutate the input array.
 */
<｜fim▁begin｜>
const merge = (left: number[], right: number[]): number[] => {
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

  return result.concat(left.slice(i)).concat(right.slice(j));
};

export function mergeSort(values: number[]): number[] {
<｜fim▁hole｜>
  if (values.length <= 1) {
    return [...values];
  }

  const middle = Math.floor(values.length / 2);
  const left = mergeSort(values.slice(0, middle));
  const right = mergeSort(values.slice(middle));
  return merge(left, right);
<｜fim▁end｜>
}
