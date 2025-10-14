export function truncateString(text: string, maxLength: number, ellipsis = '…'): string {
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
}
