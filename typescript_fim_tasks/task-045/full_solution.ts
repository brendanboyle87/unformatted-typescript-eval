export async function batchPromises<T, R>(
  items: T[],
  batchSize: number,
  mapper: (item: T, index: number) => Promise<R>,
): Promise<R[]> {
  if (batchSize <= 0) {
    throw new Error('batchSize must be greater than 0');
  }

  const results: R[] = [];

  for (let i = 0; i < items.length; i += batchSize) {
    const batch = items.slice(i, i + batchSize).map((item, offset) => mapper(item, i + offset));
    const batchResults = await Promise.all(batch);
    results.push(...batchResults);
  }

  return results;
}
