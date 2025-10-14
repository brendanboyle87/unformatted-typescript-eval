/* Docstring:
 * Implement `rotateArray` to rotate an array of elements by a given number of steps to the right.
 * The rotation count may be negative, indicating a rotation to the left.
 * Return a new array without modifying the original input.
 */
<｜fim▁begin｜>
export function rotateArray<T>(items: T[], steps: number): T[] {
<｜fim▁hole｜>
  if (items.length === 0) {
    return [];
  }

  const normalized = ((steps % items.length) + items.length) % items.length;
  if (normalized === 0) {
    return [...items];
  }

  const splitIndex = items.length - normalized;
  return [...items.slice(splitIndex), ...items.slice(0, splitIndex)];
<｜fim▁end｜>
}
