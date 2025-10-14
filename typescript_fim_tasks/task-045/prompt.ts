/* Docstring:
 * Implement `batchPromises` to process an array of items in batches using an asynchronous mapper.
 * Execute each batch sequentially while awaiting all promises within the batch in parallel.
 * Preserve the order of results matching the input items.
 */
<｜fim▁begin｜>
export async function batchPromises<T, R>(
  items: T[],
  batchSize: number,
  mapper: (item: T, index: number) => Promise<R>,
): Promise<R[]> {
<｜fim▁hole｜>
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
<｜fim▁end｜>
}
