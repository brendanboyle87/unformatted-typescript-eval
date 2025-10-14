export function padCenter(text: string, targetLength: number, padChar = ' '): string {
  if (padChar.length !== 1) {
    throw new Error('padChar must be exactly one character');
  }

  if (text.length >= targetLength) {
    return text;
  }

  const padding = targetLength - text.length;
  const left = Math.floor(padding / 2);
  const right = padding - left;
  return `${padChar.repeat(left)}${text}${padChar.repeat(right)}`;
}
