const sleep = (ms: number): Promise<void> => new Promise((resolve) => setTimeout(resolve, ms));

export async function pollUntil<T>(
  factory: () => Promise<T>,
  predicate: (value: T) => boolean,
  intervalMs: number,
  timeoutMs: number,
): Promise<T> {
  const deadline = Date.now() + timeoutMs;

  while (true) {
    const result = await factory();
    if (predicate(result)) {
      return result;
    }

    if (Date.now() >= deadline) {
      throw new Error('Polling timed out');
    }

    if (intervalMs > 0) {
      const waitTime = Math.min(intervalMs, Math.max(0, deadline - Date.now()));
      if (waitTime > 0) {
        await sleep(waitTime);
      }
    }
  }
}
