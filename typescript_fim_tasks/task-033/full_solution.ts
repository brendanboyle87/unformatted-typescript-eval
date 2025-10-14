export function groupByKey<T extends Record<string, unknown>, K extends keyof T>(items: T[], key: K): Record<string, T[]> {
  return items.reduce<Record<string, T[]>>((groups, item) => {
    const groupKey = String(item[key]);
    if (!groups[groupKey]) {
      groups[groupKey] = [];
    }
    groups[groupKey].push(item);
    return groups;
  }, {});
}
