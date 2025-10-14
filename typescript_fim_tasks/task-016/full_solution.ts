export function findMissingNumbers(values: number[]): number[] {
  if (values.length === 0) {
    return [];
  }

  const min = Math.min(...values);
  const max = Math.max(...values);
  const set = new Set(values);
  const missing: number[] = [];

  for (let number = min; number <= max; number += 1) {
    if (!set.has(number)) {
      missing.push(number);
    }
  }

  return missing;
}
