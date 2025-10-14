# Description

- **Domain:** async
- Write `retryAsync<T>(operation: () => Promise<T>, attempts: number, delayMs?: number): Promise<T>` to retry failed operations.
- Wait `delayMs` milliseconds between attempts (default 0) and reject with the last error if all retries fail.
