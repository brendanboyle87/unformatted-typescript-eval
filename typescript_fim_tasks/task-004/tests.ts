import { formatCurrency } from './full_solution';

test('formats usd by default locale', () => {
  expect(formatCurrency(1234.56, 'USD')).toBe('$1,234.56');
});

test('shows four decimals for small values', () => {
  expect(formatCurrency(0.1234, 'EUR', 'de-DE')).toBe('0,1234 €');
});

test('handles negative amounts', () => {
  expect(formatCurrency(-42, 'GBP')).toBe('-£42.00');
});
