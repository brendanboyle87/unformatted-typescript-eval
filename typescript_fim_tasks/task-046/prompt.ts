/* Docstring:
 * Implement `runSequentially` to execute an array of asynchronous functions one after another.
 * Each function returns a promise whose resolution should be awaited before starting the next.
 * Resolve with an array of the fulfilled values in order.
 */
<｜fim▁begin｜>
export async function runSequentially<T>(tasks: Array<() => Promise<T>>): Promise<T[]> {
<｜fim▁hole｜>
  const results: T[] = [];
  for (const task of tasks) {
    results.push(await task());
  }
  return results;
<｜fim▁end｜>
}
