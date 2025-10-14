export function filterTruthy<T>(values: T[]): Array<NonNullable<T>> {
  return values.filter((value): value is NonNullable<T> => Boolean(value));
}
