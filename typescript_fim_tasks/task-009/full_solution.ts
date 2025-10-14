export function repeatPattern(pattern: string, length: number): string {
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
}
