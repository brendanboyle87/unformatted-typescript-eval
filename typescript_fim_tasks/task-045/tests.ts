import { batchPromises } from './full_solution';

test('processes items in batches', async () => {
  const order: number[] = [];
  const results = await batchPromises([1, 2, 3, 4], 2, async (value) => {
    order.push(value);
    return value * 2;
  });
  expect(results).toEqual([2, 4, 6, 8]);
  expect(order).toEqual([1, 2, 3, 4]);
});

test('handles empty list', async () => {
  const results = await batchPromises([], 3, async (value) => value);
  expect(results).toEqual([]);
});

test('throws on invalid batch size', async () => {
  await expect(batchPromises([1], 0, async (value) => value)).rejects.toThrow('batchSize must be greater than 0');
});
