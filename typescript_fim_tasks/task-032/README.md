# Description

- **Domain:** object
- Write `deepMerge<T extends Record<string, unknown>, U extends Record<string, unknown>>(target: T, source: U): T & U` to recursively merge plain objects.
- Concatenate arrays and clone nested objects to avoid mutating inputs.
