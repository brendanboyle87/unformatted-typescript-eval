/* Docstring:
 * Implement `partitionByPivot` to reorder an array of numbers around a pivot value.
 * Elements less than the pivot should come first, followed by elements equal to the pivot, then greater than the pivot.
 * Return a new array reflecting the partition while preserving the relative order within each group.
 */
<｜fim▁begin｜>
export function partitionByPivot(values: number[], pivot: number): number[] {
<｜fim▁hole｜>
  const less: number[] = [];
  const equal: number[] = [];
  const greater: number[] = [];

  for (const value of values) {
    if (value < pivot) {
      less.push(value);
    } else if (value > pivot) {
      greater.push(value);
    } else {
      equal.push(value);
    }
  }

  return [...less, ...equal, ...greater];
<｜fim▁end｜>
}
