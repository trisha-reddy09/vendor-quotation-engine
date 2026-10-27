// Shows rupees the Indian way: 120000 -> "Rs. 1,20,000"

export function formatRupees(n) {
  return "Rs. " + new Intl.NumberFormat("en-IN").format(n);
}