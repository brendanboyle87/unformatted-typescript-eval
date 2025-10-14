export function chunkArray<T>(items: T[], size: number): T[][] {
  if (size <= 0) {
    throw new Error('size must be greater than zero');
  }

  const result: T[][] = [];
  for (let index = 0; index < items.length; index += size) {
    result.push(items.slice(index, index + size));
  }

  return result;
}
