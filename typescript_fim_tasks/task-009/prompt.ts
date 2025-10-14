/* Docstring:
 * Implement `repeatPattern` to produce a string of a specified length by repeating a pattern.
 * The function takes a pattern string and the desired total length; it should truncate the last repetition to fit the limit.
 * Throw a `RangeError` when the requested length is negative and return an empty string if the pattern is empty.
 */
<｜fim▁begin｜>
export function repeatPattern(pattern: string, length: number): string {
<｜fim▁hole｜>
  if (length < 0) {
    throw new RangeError('length must be non-negative');
  }

  if (pattern.length === 0 || length === 0) {
    return '';
  }

  let result = '';
  while (result.length < length) {
    const remaining = length - result.length;
    result += remaining >= pattern.length ? pattern : pattern.slice(0, remaining);
  }

  return result;
<｜fim▁end｜>
}
