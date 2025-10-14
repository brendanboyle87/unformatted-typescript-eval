export function filterObject<T extends Record<string, unknown>>(source: T, predicate: (value: T[keyof T], key: keyof T) => boolean): Partial<T> {
  const result: Partial<T> = {};
  (Object.keys(source) as Array<keyof T>).forEach((key) => {
    const value = source[key];
    if (predicate(value, key)) {
      result[key] = value;
    }
  });
  return result;
}
