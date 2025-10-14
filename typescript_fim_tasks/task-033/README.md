# Description

- **Domain:** object
- Write `groupByKey<T extends Record<string, unknown>, K extends keyof T>(items: T[], key: K): Record<string, T[]>` to group records by `key`.
- Convert grouping keys to strings to use as object keys and avoid mutating the input array.
