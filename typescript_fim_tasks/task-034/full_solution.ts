export function mapKeys<T extends Record<string, unknown>>(source: T, mapper: (key: keyof T, value: T[keyof T]) => string): Record<string, T[keyof T]> {
  const result: Record<string, T[keyof T]> = {};
  (Object.keys(source) as Array<keyof T>).forEach((key) => {
    const newKey = mapper(key, source[key]);
    result[newKey] = source[key];
  });
  return result;
}
