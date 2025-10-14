# Description

- **Domain:** object
- Write `filterObject<T extends Record<string, unknown>>(source: T, predicate: (value: T[keyof T], key: keyof T) => boolean): Partial<T>` to filter entries.
- Preserve the original object and include entries in the same iteration order.
