# Description

- **Domain:** async
- Write `batchPromises<T, R>(items: T[], batchSize: number, mapper: (item: T, index: number) => Promise<R>): Promise<R[]>`.
- Run up to `batchSize` asynchronous operations at once, processing batches sequentially.
