# Description

- **Domain:** async
- Write `memoizeAsync<T extends (...args: any[]) => Promise<any>>(fn: T): T` to memoize asynchronous functions.
- Use JSON stringification of arguments as the cache key and reuse pending promises.
