import { sumByKey } from './full_solution';

test('sums numeric values', () => {
  expect(sumByKey([{ value: 2 }, { value: 3 }], 'value')).toBe(5);
});

test('ignores missing keys', () => {
  expect(sumByKey([{ value: 2 }, {} as { value: number }], 'value')).toBe(2);
});

test('skips non-numeric values', () => {
  expect(sumByKey<{ value: unknown }>([{ value: '3' }, { value: 4 }, { value: Number.POSITIVE_INFINITY }], 'value')).toBe(4);
});
