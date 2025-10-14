/* Docstring:
 * Implement `groupByKey` to group an array of records by the value of a specified key.
 * Return a mapping from key values to arrays of records sharing that value.
 * The original array should not be mutated.
 */
<｜fim▁begin｜>
export function groupByKey<T extends Record<string, unknown>, K extends keyof T>(items: T[], key: K): Record<string, T[]> {
<｜fim▁hole｜>
  return items.reduce<Record<string, T[]>>((groups, item) => {
    const groupKey = String(item[key]);
    if (!groups[groupKey]) {
      groups[groupKey] = [];
    }
    groups[groupKey].push(item);
    return groups;
  }, {});
<｜fim▁end｜>
}
