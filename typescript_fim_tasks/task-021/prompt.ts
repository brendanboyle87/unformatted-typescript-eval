/* Docstring:
 * Implement `bubbleSortNumbers` to sort an array of numbers in ascending order using the bubble sort algorithm.
 * Return a new array without mutating the original input.
 * Optimize by stopping early when no swaps occur during a pass.
 */
<｜fim▁begin｜>
export function bubbleSortNumbers(values: number[]): number[] {
<｜fim▁hole｜>
  const result = [...values];
  for (let end = result.length - 1; end > 0; end -= 1) {
    let swapped = false;
    for (let i = 0; i < end; i += 1) {
      if (result[i] > result[i + 1]) {
        [result[i], result[i + 1]] = [result[i + 1], result[i]];
        swapped = true;
      }
    }
    if (!swapped) {
      break;
    }
  }
  return result;
<｜fim▁end｜>
}
