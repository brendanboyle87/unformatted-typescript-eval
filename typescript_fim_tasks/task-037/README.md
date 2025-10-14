# Description

- **Domain:** object
- Write `setValueByPath<T extends Record<string, unknown>>(source: T, path: string, value: unknown): T & Record<string, unknown>` to assign a nested value.
- Generate intermediate containers without mutating `source`, interpreting numeric segments as array indices.
