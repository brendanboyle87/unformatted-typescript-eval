/* Docstring:
 * Implement `countingSort` to sort an array of non-negative integers using the counting sort algorithm.
 * Return a new sorted array without mutating the input.
 * Throw an error if a negative number is encountered.
 */
<｜fim▁begin｜>
export function countingSort(values: number[]): number[] {
<｜fim▁hole｜>
  if (values.length === 0) {
    return [];
  }

  let max = 0;
  for (const value of values) {
    if (value < 0) {
      throw new Error('countingSort only accepts non-negative integers');
    }
    if (value > max) {
      max = value;
    }
  }

  const counts = new Array<number>(max + 1).fill(0);
  for (const value of values) {
    counts[value] += 1;
  }

  const result: number[] = [];
  counts.forEach((count, number) => {
    for (let i = 0; i < count; i += 1) {
      result.push(number);
    }
  });

  return result;
<｜fim▁end｜>
}
