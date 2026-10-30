"use client";

import { quotes } from "../../data/mockData";
import { formatRupees } from "../../lib/formatters";

export default function QuoteComparisonPage() {
  return (
    <div className="p-6">
      <h1 className="mb-1 text-2xl font-bold">
        Quote Comparison
      </h1>

      <p className="mb-4 text-gray-600">
        Quotations received from different vendors, side by side.
      </p>

      <div className="overflow-x-auto rounded-lg bg-white text-gray-900 shadow">
        <table className="min-w-full text-left text-sm">
          <thead className="bg-gray-100 text-gray-700">
            <tr>
              <th className="px-4 py-3 font-semibold">Vendor</th>
              <th className="px-4 py-3 font-semibold">Quote No</th>
              <th className="px-4 py-3 font-semibold min-w-[120px]">Date</th>
              <th className="px-4 py-3 font-semibold">Total Amount</th>
              <th className="px-4 py-3 font-semibold">Payment Terms</th>
              <th className="px-4 py-3 font-semibold">Lead Time (days)</th>
              <th className="px-4 py-3 font-semibold">Validity (days)</th>
            </tr>
          </thead>

          <tbody className="text-gray-800">
            {quotes.map((q) => (
              <tr
                key={q.id}
                className="border-t hover:bg-gray-50"
              >
                <td className="px-4 py-3">{q.vendor_name}</td>
                <td className="px-4 py-3">{q.quote_number}</td>
                <td className="px-4 py-3 min-w-[120px] whitespace-nowrap">
                  {q.quote_date.split("-").reverse().join("-")}
                </td>
                <td className="px-4 py-3">
                  {formatRupees(q.total_amount)}
                </td>
                <td className="px-4 py-3">{q.payment_terms}</td>
                <td className="px-4 py-3">{q.lead_time_days}</td>
                <td className="px-4 py-3">{q.validity_days}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}