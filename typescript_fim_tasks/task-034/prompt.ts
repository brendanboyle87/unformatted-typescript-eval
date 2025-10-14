/* Docstring:
 * Implement `mapKeys` to transform the keys of an object using a mapping function.
 * The mapper receives the original key and value and returns a new key; the values remain unchanged.
 * When multiple keys map to the same result, later keys should overwrite earlier ones.
 */
<｜fim▁begin｜>
export function mapKeys<T extends Record<string, unknown>>(source: T, mapper: (key: keyof T, value: T[keyof T]) => string): Record<string, T[keyof T]> {
<｜fim▁hole｜>
  const result: Record<string, T[keyof T]> = {};
  (Object.keys(source) as Array<keyof T>).forEach((key) => {
    const newKey = mapper(key, source[key]);
    result[newKey] = source[key];
  });
  return result;
<｜fim▁end｜>
}
