const isPlainObject = (value: unknown): value is Record<string, unknown> =>
  value !== null && typeof value === 'object' && !Array.isArray(value) && !(value instanceof Date);

export function deepMerge<T extends Record<string, unknown>, U extends Record<string, unknown>>(target: T, source: U): T & U {
  const result: Record<string, unknown> = { ...target };

  for (const [key, sourceValue] of Object.entries(source)) {
    const targetValue = result[key];

    if (Array.isArray(targetValue) && Array.isArray(sourceValue)) {
      result[key] = [...targetValue, ...sourceValue.map((item) => (isPlainObject(item) ? deepMerge({}, item) : item))];
      continue;
    }

    if (isPlainObject(targetValue) && isPlainObject(sourceValue)) {
      result[key] = deepMerge(targetValue, sourceValue);
      continue;
    }

    result[key] = isPlainObject(sourceValue) ? deepMerge({}, sourceValue) : Array.isArray(sourceValue)
      ? sourceValue.slice()
      : sourceValue;
  }

  return result as T & U;
}
