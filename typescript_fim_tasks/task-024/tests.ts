import { insertionSortByKey } from './full_solution';

test('sorts objects by numeric key', () => {
  const sorted = insertionSortByKey(
    [
      { id: 3, name: 'c' },
      { id: 1, name: 'a' },
      { id: 2, name: 'b' },
    ],
    'id',
  );
  expect(sorted.map((item) => item.id)).toEqual([1, 2, 3]);
});

test('does not mutate original array', () => {
  const input = [{ score: 2 }, { score: 1 }];
  insertionSortByKey(input, 'score');
  expect(input).toEqual([{ score: 2 }, { score: 1 }]);
});

test('handles empty array', () => {
  expect(insertionSortByKey([], 'value')).toEqual([]);
});
