/* Docstring:
 * Implement `deepClone` to create a deep copy of plain objects and arrays.
 * The function should recursively clone nested arrays and objects, and copy `Date` instances by value.
 * Primitive values should be returned as-is.
 */
<｜fim▁begin｜>
export function deepClone<T>(value: T): T {
<｜fim▁hole｜>
  if (value instanceof Date) {
    return new Date(value.getTime()) as T;
  }

  if (Array.isArray(value)) {
    return value.map((item) => deepClone(item)) as unknown as T;
  }

  if (value !== null && typeof value === 'object') {
    const result: Record<string, unknown> = {};
    for (const [key, val] of Object.entries(value as Record<string, unknown>)) {
      result[key] = deepClone(val);
    }
    return result as T;
  }

  return value;
<｜fim▁end｜>
}
