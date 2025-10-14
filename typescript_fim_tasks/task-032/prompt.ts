/* Docstring:
 * Implement `deepMerge` to merge two plain objects recursively.
 * When both objects contain the same key with plain object values, merge them; when both are arrays, concatenate copies of the arrays.
 * Other values should be overwritten by the source.
 */
<｜fim▁begin｜>
const isPlainObject = (value: unknown): value is Record<string, unknown> =>
  value !== null && typeof value === 'object' && !Array.isArray(value) && !(value instanceof Date);

export function deepMerge<T extends Record<string, unknown>, U extends Record<string, unknown>>(target: T, source: U): T & U {
<｜fim▁hole｜>
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
<｜fim▁end｜>
}
