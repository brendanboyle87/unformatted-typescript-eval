/* Docstring:
 * Build a function `capitalizeWords` that converts the first character of every word in a string to uppercase while lowercasing the remaining characters of the word.
 * Words are delimited by whitespace but the original spacing must be preserved in the returned string.
 * The function should handle Unicode characters when changing case.
 */
<｜fim▁begin｜>
export function capitalizeWords(text: string): string {
<｜fim▁hole｜>
  return text
    .split(/(\s+)/)
    .map((segment) => {
      if (/^\s+$/.test(segment) || segment.length === 0) {
        return segment;
      }

      const [first, ...rest] = Array.from(segment);
      const head = first.toLocaleUpperCase();
      const tail = rest.join('').toLocaleLowerCase();
      return `${head}${tail}`;
    })
    .join('');
<｜fim▁end｜>
}
