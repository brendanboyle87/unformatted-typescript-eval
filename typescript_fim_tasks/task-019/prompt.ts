/* Docstring:
 * Create `filterTruthy` to remove falsy values from an array.
 * The function should return a new array containing only values that coerce to true, preserving the original order.
 * TypeScript should infer the narrowed type of the returned array.
 */
<｜fim▁begin｜>
export function filterTruthy<T>(values: T[]): Array<NonNullable<T>> {
<｜fim▁hole｜>
  return values.filter((value): value is NonNullable<T> => Boolean(value));
<｜fim▁end｜>
}
