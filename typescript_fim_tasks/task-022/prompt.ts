/* Docstring:
 * Implement `quickSortStrings` to sort strings in ascending order using the quicksort algorithm.
 * Compare strings using `localeCompare` with base sensitivity to perform a case-insensitive sort.
 * Return a new sorted array without mutating the input.
 */
<｜fim▁begin｜>
export function quickSortStrings(values: string[]): string[] {
<｜fim▁hole｜>
  if (values.length <= 1) {
    return [...values];
  }

  const [pivot, ...rest] = values;
  const left: string[] = [];
  const right: string[] = [];

  for (const value of rest) {
    const comparison = value.localeCompare(pivot, undefined, { sensitivity: 'base' });
    if (comparison < 0) {
      left.push(value);
    } else if (comparison > 0) {
      right.push(value);
    } else {
      right.push(value);
    }
  }

  return [...quickSortStrings(left), pivot, ...quickSortStrings(right)];
<｜fim▁end｜>
}
