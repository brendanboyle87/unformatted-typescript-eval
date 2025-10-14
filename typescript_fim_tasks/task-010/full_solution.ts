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
  if (keyword.length === 0) {
    return text;
  }

  const escaped = escapeRegex(keyword);
  const pattern = new RegExp(escaped, 'gi');
  return text.replace(pattern, (match) => `${wrapper.start}${match}${wrapper.end}`);
}
