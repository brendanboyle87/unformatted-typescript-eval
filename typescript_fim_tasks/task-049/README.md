# Description

- **Domain:** async
- Write `mapAsyncSeries<T, R>(items: T[], mapper: (item: T, index: number) => Promise<R>): Promise<R[]>` to map sequentially.
- Ensure each item is processed after the previous one finishes.
