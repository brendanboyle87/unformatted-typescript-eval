export function getTopNElements(values: number[], n: number): number[] {
  if (n <= 0) {
    return [];
  }

  const count = Math.min(n, values.length);
  const copy = [...values];
  copy.sort((a, b) => b - a);
  return copy.slice(0, count);
}
