export function partitionByPivot(values: number[], pivot: number): number[] {
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
}
