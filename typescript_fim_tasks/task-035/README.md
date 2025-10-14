# Description

- **Domain:** object
- Write `omitKeys<T extends Record<string, unknown>, K extends keyof T>(source: T, keys: K[]): Omit<T, K>` to remove selected keys from an object copy.
- Do not mutate the original object.
