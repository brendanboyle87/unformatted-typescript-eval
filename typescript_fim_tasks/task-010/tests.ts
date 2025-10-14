import { highlightKeyword } from './full_solution';

test('wraps occurrences with default markup', () => {
  expect(highlightKeyword('Learn TypeScript with TypeScript', 'typescript')).toBe('Learn <mark>TypeScript</mark> with <mark>TypeScript</mark>');
});

test('uses custom wrapper', () => {
  expect(highlightKeyword('1 + 1 = 2', '+', { start: '[', end: ']' })).toBe('1 [+] 1 = 2');
});

test('leaves text unchanged for empty keyword', () => {
  expect(highlightKeyword('sample', '')).toBe('sample');
});
