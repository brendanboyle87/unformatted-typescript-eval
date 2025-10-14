const wait = (ms: number): Promise<void> => new Promise((resolve) => setTimeout(resolve, ms));

export async function retryAsync<T>(operation: () => Promise<T>, attempts: number, delayMs = 0): Promise<T> {
  if (attempts <= 0) {
    throw new Error('attempts must be greater than 0');
  }

  let lastError: unknown;
  for (let attempt = 1; attempt <= attempts; attempt += 1) {
    try {
      return await operation();
    } catch (error) {
      lastError = error;
      if (attempt < attempts && delayMs > 0) {
        await wait(delayMs);
      }
    }
  }

  throw lastError instanceof Error ? lastError : new Error('Operation failed');
}
