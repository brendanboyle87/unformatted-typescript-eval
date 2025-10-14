export function sumByKey<T extends Record<string, unknown>>(items: T[], key: keyof T): number {
  let total = 0;
  for (const item of items) {
    const value = item[key];
    if (typeof value === 'number' && Number.isFinite(value)) {
      total += value;
    }
  }
  return total;
}
