/* Docstring:
 * Implement `highlightKeyword` to wrap all case-insensitive occurrences of a keyword within a text string.
 * The function receives the text, the keyword, and an optional wrapper object containing `start` and `end` strings defaulting to `<mark>` and `</mark>`.
 * Escape special regex characters in the keyword and leave the text unchanged when the keyword is empty.
 */
<｜fim▁begin｜>
export interface HighlightWrapper {
  start: string;
  end: string;
}

const escapeRegex = (value: string): string => value.replace(/[.*+?^${}()|[\]\]/g, '\$&');

export function highlightKeyword(
  text: string,
  keyword: string,
  wrapper: HighlightWrapper = { start: '<mark>', end: '</mark>' },
): string {
<｜fim▁hole｜>
  if (keyword.length === 0) {
    return text;
  }

  const escaped = escapeRegex(keyword);
  const pattern = new RegExp(escaped, 'gi');
  return text.replace(pattern, (match) => `${wrapper.start}${match}${wrapper.end}`);
<｜fim▁end｜>
}
