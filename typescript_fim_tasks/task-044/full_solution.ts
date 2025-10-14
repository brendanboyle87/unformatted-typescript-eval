export async function limitConcurrency<T>(tasks: Array<() => Promise<T>>, limit: number): Promise<T[]> {
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
}
