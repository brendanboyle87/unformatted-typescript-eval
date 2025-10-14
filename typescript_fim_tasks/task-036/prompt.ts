/* Docstring:
 * Implement `getValueByPath` to retrieve a nested value from an object using a dot-separated path.
 * If any segment is missing, return `undefined`.
 * Treat array indices as numeric segments in the path.
 */
<｜fim▁begin｜>
export function getValueByPath(source: unknown, path: string): unknown {
<｜fim▁hole｜>
  if (!path) {
    return source;
  }

  const segments = path.split('.');
  let current: unknown = source;

  for (const segment of segments) {
    if (current === null || typeof current !== 'object') {
      return undefined;
    }

    if (Array.isArray(current) && /^\d+$/.test(segment)) {
      current = current[Number(segment)];
    } else {
      current = (current as Record<string, unknown>)[segment];
    }
  }

  return current;
<｜fim▁end｜>
}
