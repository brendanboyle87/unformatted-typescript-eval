export function memoizeAsync<T extends (...args: any[]) => Promise<any>>(fn: T): T {
  const cache = new Map<string, Promise<any>>();

  const memoized = (...args: Parameters<T>): ReturnType<T> => {
    const key = JSON.stringify(args);
    if (!cache.has(key)) {
      const promise = fn(...args)
        .then((result) => {
          cache.set(key, Promise.resolve(result));
          return result;
        })
        .catch((error) => {
          cache.delete(key);
          throw error;
        });
      cache.set(key, promise);
    }
    return cache.get(key)! as ReturnType<T>;
  };

  return memoized as T;
}
