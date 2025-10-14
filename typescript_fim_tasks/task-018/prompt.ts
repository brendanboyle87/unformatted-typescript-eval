/* Docstring:
 * Implement `sumByKey` to sum numeric property values across an array of objects.
 * Accept an array of generic records and a key; treat missing or non-number values as zero.
 * Return the total sum as a number.
 */
<｜fim▁begin｜>
export function sumByKey<T extends Record<string, unknown>>(items: T[], key: keyof T): number {
<｜fim▁hole｜>
  let total = 0;
  for (const item of items) {
    const value = item[key];
    if (typeof value === 'number' && Number.isFinite(value)) {
      total += value;
    }
  }
  return total;
<｜fim▁end｜>
}
