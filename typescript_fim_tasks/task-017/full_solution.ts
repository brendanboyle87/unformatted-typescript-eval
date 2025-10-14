export function rotateArray<T>(items: T[], steps: number): T[] {
  if (items.length === 0) {
    return [];
  }

  const normalized = ((steps % items.length) + items.length) % items.length;
  if (normalized === 0) {
    return [...items];
  }

  const splitIndex = items.length - normalized;
  return [...items.slice(splitIndex), ...items.slice(0, splitIndex)];
}
