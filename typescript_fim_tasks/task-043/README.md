# Description

- **Domain:** async
- Write `pollUntil<T>(factory: () => Promise<T>, predicate: (value: T) => boolean, intervalMs: number, timeoutMs: number): Promise<T>`.
- Resolve with the first value that satisfies the predicate or reject when the timeout elapses.
