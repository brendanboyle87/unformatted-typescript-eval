export function snakeToCamel(value: string): string {
  const segments = value.split('_');
  return segments
    .filter((segment) => segment.length > 0)
    .map((segment, index) => {
      const lower = segment.toLowerCase();
      if (index === 0) {
        return lower;
      }
      const [first, ...rest] = lower;
      return `${first.toUpperCase()}${rest.join('')}`;
    })
    .join('');
}
