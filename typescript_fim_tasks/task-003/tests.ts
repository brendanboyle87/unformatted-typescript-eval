import { capitalizeWords } from './full_solution';

test('capitalizes words while preserving spaces', () => {
  expect(capitalizeWords('hello   world')).toBe('Hello   World');
});

test('handles mixed casing', () => {
  expect(capitalizeWords('gOOD MORNING')).toBe('Good Morning');
});

test('supports unicode letters', () => {
  expect(capitalizeWords('über cool')).toBe('Über Cool');
});
