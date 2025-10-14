/* Docstring:
 * Implement `limitConcurrency` to execute asynchronous tasks with a maximum number of concurrent operations.
 * Accept an array of functions returning promises and a positive concurrency limit.
 * Resolve with an array of results preserving the order of the original tasks.
 */
<｜fim▁begin｜>
export async function limitConcurrency<T>(tasks: Array<() => Promise<T>>, limit: number): Promise<T[]> {
<｜fim▁hole｜>
  if (limit <= 0) {
    throw new Error('limit must be greater than 0');
  }

  const results: T[] = new Array(tasks.length);
  let index = 0;

  const workers: Promise<void>[] = [];

  const runNext = async (): Promise<void> => {
    const currentIndex = index;
    index += 1;
    if (currentIndex >= tasks.length) {
      return;
    }
    const task = tasks[currentIndex];
    results[currentIndex] = await task();
    await runNext();
  };

  for (let i = 0; i < Math.min(limit, tasks.length); i += 1) {
    workers.push(runNext());
  }

  await Promise.all(workers);
  return results;
<｜fim▁end｜>
}
