export function formatCurrency(amount: number, currency: string, locale = 'en-US'): string {
  const fractionDigits = Math.abs(amount) < 1 ? 4 : 2;
  const formatter = new Intl.NumberFormat(locale, {
    style: 'currency',
    currency,
    minimumFractionDigits: fractionDigits,
    maximumFractionDigits: 4,
  });
  return formatter.format(amount);
}
