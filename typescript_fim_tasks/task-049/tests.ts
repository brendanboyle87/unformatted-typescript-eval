import { mapAsyncSeries } from './full_solution';

test('maps sequentially', async () => {
  const order: number[] = [];
  const results = await mapAsyncSeries([1, 2, 3], async (value) => {
    order.push(value);
    return value * 2;
  });
  expect(results).toEqual([2, 4, 6]);
  expect(order).toEqual([1, 2, 3]);
});

test('handles empty array', async () => {
  expect(await mapAsyncSeries([], async (value) => value)).toEqual([]);
});

test('propagates errors', async () => {
  await expect(
    mapAsyncSeries([1, 2], async (value) => {
      if (value === 2) {
        throw new Error('fail');
      }
      return value;
    }),
  ).rejects.toThrow('fail');
});
