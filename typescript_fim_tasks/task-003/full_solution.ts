export function capitalizeWords(text: string): string {
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
}
