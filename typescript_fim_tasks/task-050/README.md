# Description

- **Domain:** async
- Write `makeCancelable<T>(executor: (signal: AbortSignal) => Promise<T>): { promise: Promise<T>; cancel: () => void }`.
- Abort the underlying `AbortSignal` on cancel and reject with `Operation cancelled` when cancellation happens before resolution.
