export function diffObjects<T extends Record<string, unknown>>(previous: T, next: T): Record<string, { before: unknown; after: unknown }> {
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
}
