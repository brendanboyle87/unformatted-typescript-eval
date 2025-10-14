/* Docstring:
 * Design `padCenter` to center a string within a target length by padding with a specified character.
 * The function receives the text, the desired total length, and an optional single-character pad value defaulting to a space.
 * Throw an error when the pad value is not exactly one character long and return the original text if no padding is needed.
 */
<｜fim▁begin｜>
export function padCenter(text: string, targetLength: number, padChar = ' '): string {
<｜fim▁hole｜>
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
<｜fim▁end｜>
}
