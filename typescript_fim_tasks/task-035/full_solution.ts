export function omitKeys<T extends Record<string, unknown>, K extends keyof T>(source: T, keys: K[]): Omit<T, K> {
  const exclusions = new Set(keys);
  const result: Record<string, unknown> = {};

  (Object.keys(source) as Array<keyof T>).forEach((key) => {
    if (!exclusions.has(key)) {
      result[key as string] = source[key];
    }
  });

  return result as Omit<T, K>;
}
