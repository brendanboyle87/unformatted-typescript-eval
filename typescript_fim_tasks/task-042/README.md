# Description

- **Domain:** async
- Write `withTimeout<T>(promise: Promise<T>, timeoutMs: number, message?: string): Promise<T>` to enforce a timeout on a promise.
- Reject with a timeout error message when the promise does not settle in time.
