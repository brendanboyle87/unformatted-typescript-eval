export function uniqueNumbers(values: number[]): number[] {
  const seen = new Set<number>();
  let seenNaN = false;
  const result: number[] = [];

  for (const value of values) {
    if (Number.isNaN(value)) {
      if (!seenNaN) {
        seenNaN = true;
        result.push(value);
      }
      continue;
    }

    if (!seen.has(value)) {
      seen.add(value);
      result.push(value);
    }
  }

  return result;
}
