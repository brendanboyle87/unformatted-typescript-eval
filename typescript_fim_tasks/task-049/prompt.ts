/* Docstring:
 * Implement `mapAsyncSeries` to apply an asynchronous mapper to an array sequentially.
 * Await each mapper invocation before proceeding to the next item.
 * Return a promise that resolves with the array of mapped results in order.
 */
<｜fim▁begin｜>
export async function mapAsyncSeries<T, R>(items: T[], mapper: (item: T, index: number) => Promise<R>): Promise<R[]> {
<｜fim▁hole｜>
  const results: R[] = [];
  for (let index = 0; index < items.length; index += 1) {
    results.push(await mapper(items[index], index));
  }
  return results;
<｜fim▁end｜>
}
