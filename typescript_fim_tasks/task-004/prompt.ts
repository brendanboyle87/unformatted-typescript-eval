/* Docstring:
 * Implement `formatCurrency` to format a numeric amount as a localized currency string.
 * The function accepts the amount, an ISO 4217 currency code, and an optional BCP 47 locale tag defaulting to `en-US`.
 * Use `Intl.NumberFormat` and ensure values less than one display at least four decimal places.
 */
<｜fim▁begin｜>
export function formatCurrency(amount: number, currency: string, locale = 'en-US'): string {
<｜fim▁hole｜>
  const fractionDigits = Math.abs(amount) < 1 ? 4 : 2;
  const formatter = new Intl.NumberFormat(locale, {
    style: 'currency',
    currency,
    minimumFractionDigits: fractionDigits,
    maximumFractionDigits: 4,
  });
  return formatter.format(amount);
<｜fim▁end｜>
}
