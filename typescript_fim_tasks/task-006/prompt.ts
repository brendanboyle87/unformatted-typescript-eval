/* Docstring:
 * Implement `snakeToCamel` to convert a snake_case string to camelCase.
 * The function should lowercase the first segment and capitalize the first letter of subsequent segments while removing underscores.
 * Empty segments caused by consecutive underscores should be skipped in the output.
 */
<｜fim▁begin｜>
export function snakeToCamel(value: string): string {
<｜fim▁hole｜>
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
<｜fim▁end｜>
}
