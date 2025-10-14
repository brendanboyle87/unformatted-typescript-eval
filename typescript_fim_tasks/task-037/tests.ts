import { setValueByPath } from './full_solution';

test('sets nested value on new object', () => {
  const result = setValueByPath({}, 'user.name', 'Ada');
  expect(result).toEqual({ user: { name: 'Ada' } });
});

test('creates arrays for numeric segments', () => {
  const result = setValueByPath({}, 'items.0.name', 'Book');
  expect(Array.isArray((result as any).items)).toBe(true);
  expect((result as any).items[0]).toEqual({ name: 'Book' });
});

test('does not mutate source', () => {
  const source = { user: { name: 'Ada' } };
  const result = setValueByPath(source, 'user.name', 'Grace');
  expect(source.user?.name).toBe('Ada');
  expect(result.user?.name).toBe('Grace');
});
