/* Docstring:
 * Create `truncateString` to shorten a string to a maximum length, appending an ellipsis by default when truncation occurs.
 * Accept the original text, the maximum allowed length, and an optional ellipsis string defaulting to `…`.
 * Throw a `RangeError` if the maximum length is negative, and ensure the returned string does not exceed the limit.
 */
<｜fim▁begin｜>
export function truncateString(text: string, maxLength: number, ellipsis = '…'): string {
<｜fim▁hole｜>
  if (maxLength < 0) {
    throw new RangeError('maxLength must be non-negative');
  }

  if (text.length <= maxLength) {
    return text;
  }

  if (maxLength <= ellipsis.length) {
    return ellipsis.slice(0, maxLength);
  }

  const sliceEnd = maxLength - ellipsis.length;
  return `${text.slice(0, sliceEnd)}${ellipsis}`;
<｜fim▁end｜>
}
