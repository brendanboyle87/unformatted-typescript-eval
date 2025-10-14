export function quickSortStrings(values: string[]): string[] {
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
}
