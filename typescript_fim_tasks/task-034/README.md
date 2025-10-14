# Description

- **Domain:** object
- Write `mapKeys<T extends Record<string, unknown>>(source: T, mapper: (key: keyof T, value: T[keyof T]) => string): Record<string, T[keyof T]>` to remap object keys.
- Preserve values as-is and allow later keys to overwrite earlier collisions.
