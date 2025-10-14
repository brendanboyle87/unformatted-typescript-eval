/* Docstring:
 * Implement `filterObject` to produce a new object containing only entries that satisfy a predicate.
 * The predicate receives the value and key and should return a boolean indicating whether to keep the pair.
 * The original object must remain unchanged.
 */
<｜fim▁begin｜>
export function filterObject<T extends Record<string, unknown>>(source: T, predicate: (value: T[keyof T], key: keyof T) => boolean): Partial<T> {
<｜fim▁hole｜>
  const result: Partial<T> = {};
  (Object.keys(source) as Array<keyof T>).forEach((key) => {
    const value = source[key];
    if (predicate(value, key)) {
      result[key] = value;
    }
  });
  return result;
<｜fim▁end｜>
}
