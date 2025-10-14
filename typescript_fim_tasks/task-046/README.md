# Description

- **Domain:** async
- Write `runSequentially<T>(tasks: Array<() => Promise<T>>): Promise<T[]>` to chain asynchronous tasks sequentially.
- Await each task before invoking the next and collect their results in order.
