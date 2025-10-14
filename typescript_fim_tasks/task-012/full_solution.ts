export function flattenOneLevel<T>(input: (T | T[])[]): T[] {
  const result: T[] = [];
  for (const element of input) {
    if (Array.isArray(element)) {
      result.push(...element);
    } else {
      result.push(element);
    }
  }
  return result;
}
