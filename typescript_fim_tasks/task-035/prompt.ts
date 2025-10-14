/* Docstring:
 * Implement `omitKeys` to produce a shallow copy of an object without specific keys.
 * Accept the source object and an array of keys to remove.
 * Return a new object excluding those keys without modifying the original.
 */
<｜fim▁begin｜>
export function omitKeys<T extends Record<string, unknown>, K extends keyof T>(source: T, keys: K[]): Omit<T, K> {
<｜fim▁hole｜>
  const exclusions = new Set(keys);
  const result: Record<string, unknown> = {};

  (Object.keys(source) as Array<keyof T>).forEach((key) => {
    if (!exclusions.has(key)) {
      result[key as string] = source[key];
    }
  });

  return result as Omit<T, K>;
<｜fim▁end｜>
}
