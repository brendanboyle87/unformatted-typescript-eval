import { groupByKey } from './full_solution';

interface User {
  role: string;
  name: string;
}

const users: User[] = [
  { role: 'admin', name: 'A' },
  { role: 'user', name: 'B' },
  { role: 'admin', name: 'C' },
];

test('groups by role', () => {
  expect(groupByKey(users, 'role')).toEqual({
    admin: [users[0], users[2]],
    user: [users[1]],
  });
});

test('handles empty array', () => {
  expect(groupByKey([], 'role')).toEqual({});
});

test('stringifies non-string keys', () => {
  expect(groupByKey([{ id: 1 }, { id: 1 }, { id: 2 }], 'id')).toEqual({ '1': [{ id: 1 }, { id: 1 }], '2': [{ id: 2 }] });
});
