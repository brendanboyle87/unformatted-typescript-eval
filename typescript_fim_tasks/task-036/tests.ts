import { getValueByPath } from './full_solution';

const data = { user: { address: { city: 'Paris' } }, items: [{ name: 'Book' }] };

test('retrieves nested value', () => {
  expect(getValueByPath(data, 'user.address.city')).toBe('Paris');
});

test('handles array indices', () => {
  expect(getValueByPath(data, 'items.0.name')).toBe('Book');
});

test('returns undefined when path missing', () => {
  expect(getValueByPath(data, 'user.address.zip')).toBeUndefined();
});
