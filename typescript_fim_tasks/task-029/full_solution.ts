export function countingSort(values: number[]): number[] {
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
}
