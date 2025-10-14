# Description

- **Domain:** object
- Write `diffObjects<T extends Record<string, unknown>>(previous: T, next: T): Record<string, { before: unknown; after: unknown }>` to capture differences between two objects.
- Use strict equality to compare values and include added or removed keys.
