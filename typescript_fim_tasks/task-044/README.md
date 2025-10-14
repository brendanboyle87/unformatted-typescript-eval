# Description

- **Domain:** async
- Write `limitConcurrency<T>(tasks: Array<() => Promise<T>>, limit: number): Promise<T[]>` to run tasks under a concurrency cap.
- Preserve result order and reject immediately if any task rejects.
