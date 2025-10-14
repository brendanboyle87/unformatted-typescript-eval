export async function mapAsyncSeries<T, R>(items: T[], mapper: (item: T, index: number) => Promise<R>): Promise<R[]> {
  const results: R[] = [];
  for (let index = 0; index < items.length; index += 1) {
    results.push(await mapper(items[index], index));
  }
  return results;
}
