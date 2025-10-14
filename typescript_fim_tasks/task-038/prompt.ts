/* Docstring:
 * Implement `diffObjects` to compare two plain objects and describe their differences.
 * Return a mapping from keys to `{ before, after }` pairs for keys whose values are not strictly equal.
 * Include keys present in one object but not the other.
 */
<｜fim▁begin｜>
export function diffObjects<T extends Record<string, unknown>>(previous: T, next: T): Record<string, { before: unknown; after: unknown }> {
<｜fim▁hole｜>
  const diff: Record<string, { before: unknown; after: unknown }> = {};
  const keys = new Set([...Object.keys(previous), ...Object.keys(next)]);

  keys.forEach((key) => {
    const before = previous[key as keyof T];
    const after = next[key as keyof T];
    if (before !== after) {
      diff[key] = { before, after };
    }
  });

  return diff;
<｜fim▁end｜>
}
