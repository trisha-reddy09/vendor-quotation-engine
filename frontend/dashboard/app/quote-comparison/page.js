
"use client";

import { useState } from "react";
import { quotes, vendors } from "../../src/data/mockData";
import { formatRupees } from "../../src/lib/formatters";

const PAYMENT_TERMS = ["Net-30", "Net-45", "Advance"];

export default function QuoteComparisonPage() {
  const [sortKey, setSortKey] = useState("total_amount");
  const [sortDir, setSortDir] = useState("asc");
  const [paymentFilter, setPaymentFilter] = useState("All");
  const [vendorFilter, setVendorFilter] = useState("All");

  function handleSort(key) {
    if (key === sortKey) {
      setSortDir(sortDir === "asc" ? "desc" : "asc");
    } else {
      setSortKey(key);
      setSortDir("asc");
    }
  }

  function resetFilters() {
    setPaymentFilter("All");
    setVendorFilter("All");
  }

  // Filter quotes
  const filteredQuotes = quotes.filter(
    (q) =>
      (paymentFilter === "All" || q.payment_terms === paymentFilter) &&
      (vendorFilter === "All" || q.vendor_name === vendorFilter)
  );

  // Sort filtered quotes
  const sortedQuotes = [...filteredQuotes].sort((a, b) =>
    sortDir === "asc"
      ? a[sortKey] - b[sortKey]
      : b[sortKey] - a[sortKey]
  );

  // Summary values
  const hasResults = sortedQuotes.length > 0;

  const lowestAmount = hasResults
    ? Math.min(...sortedQuotes.map((q) => q.total_amount))
    : null;

  const shortestLead = hasResults
    ? Math.min(...sortedQuotes.map((q) => q.lead_time_days))
    : null;

  function arrow(key) {
    if (key !== sortKey) return "";
    return sortDir === "asc" ? " ▲" : " ▼";
  }

  return (
    <div className="min-h-screen bg-slate-50 p-6 text-slate-800">

      <h1 className="mb-1 text-2xl font-bold text-slate-900">
        Quote Comparison
      </h1>

      <p className="mb-6 text-sm text-slate-500">
        Compare quotations from different vendors and find the best deal.
      </p>

      {/* Filters */}
      <div className="mb-6 flex flex-wrap items-end gap-4 rounded-xl border border-slate-200 bg-white p-5 shadow-sm">

        <div>
          <label className="mb-2 block text-sm font-semibold text-slate-700">
            Payment Terms
          </label>

          <select
            className="min-w-[160px] rounded-lg border border-slate-300 bg-white px-3 py-2.5 text-sm text-slate-700 outline-none focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100"
            value={paymentFilter}
            onChange={(e) => setPaymentFilter(e.target.value)}
          >
            <option value="All">All</option>

            {PAYMENT_TERMS.map((t) => (
              <option key={t} value={t}>
                {t}
              </option>
            ))}
          </select>
        </div>

        <div>
          <label className="mb-2 block text-sm font-semibold text-slate-700">
            Vendor
          </label>

          <select
            className="min-w-[200px] rounded-lg border border-slate-300 bg-white px-3 py-2.5 text-sm text-slate-700 outline-none focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100"
            value={vendorFilter}
            onChange={(e) => setVendorFilter(e.target.value)}
          >
            <option value="All">All</option>

            {vendors.map((v) => (
              <option key={v.id} value={v.vendor_name}>
                {v.vendor_name}
              </option>
            ))}
          </select>
        </div>

        <button
          className="rounded-lg bg-slate-100 px-4 py-2.5 text-sm font-semibold text-slate-700 transition hover:bg-slate-200"
          onClick={resetFilters}
        >
          Reset Filters
        </button>
      </div>

      {/* Summary Cards */}
      <div className="mb-6 grid grid-cols-1 gap-4 sm:grid-cols-3">

        <div className="rounded-xl border border-indigo-100 bg-white p-5 shadow-sm">
          <p className="text-xs font-semibold uppercase tracking-wider text-slate-500">
            Quotes Shown
          </p>

          <p className="mt-2 text-2xl font-bold text-indigo-700">
            {sortedQuotes.length} of {quotes.length}
          </p>

          <p className="mt-1 text-xs text-slate-400">
            Total quotations available
          </p>
        </div>

        <div className="rounded-xl border border-emerald-100 bg-white p-5 shadow-sm">
          <p className="text-xs font-semibold uppercase tracking-wider text-slate-500">
            Lowest Amount
          </p>

          <p className="mt-2 text-2xl font-bold text-emerald-700">
            {hasResults ? formatRupees(lowestAmount) : "-"}
          </p>

          <p className="mt-1 text-xs text-slate-400">
            Most affordable quotation
          </p>
        </div>

        <div className="rounded-xl border border-teal-100 bg-white p-5 shadow-sm">
          <p className="text-xs font-semibold uppercase tracking-wider text-slate-500">
            Shortest Lead Time
          </p>

          <p className="mt-2 text-2xl font-bold text-teal-700">
            {hasResults ? shortestLead + " days" : "-"}
          </p>

          <p className="mt-1 text-xs text-slate-400">
            Fastest vendor delivery
          </p>
        </div>
      </div>

      {/* Table or Empty Message */}
      {!hasResults ? (
        <div className="rounded-xl border border-slate-200 bg-white p-8 text-center text-slate-500 shadow-sm">
          No quotes match these filters.
        </div>
      ) : (
        <div className="overflow-x-auto rounded-xl border border-slate-200 bg-white shadow-sm">

          <table className="min-w-full text-left text-sm">

            <thead className="bg-slate-100 text-slate-700">
              <tr>
                <th className="px-4 py-4 font-semibold">Vendor</th>

                <th className="px-4 py-4 font-semibold">Quote No</th>

                <th className="min-w-[120px] whitespace-nowrap px-4 py-4 font-semibold">
                  Date
                </th>

                <th
                  className="cursor-pointer select-none px-4 py-4 font-semibold transition hover:bg-indigo-100 hover:text-indigo-800"
                  onClick={() => handleSort("total_amount")}
                >
                  Total Amount{arrow("total_amount")}
                </th>

                <th className="px-4 py-4 font-semibold">
                  Payment Terms
                </th>

                <th
                  className="cursor-pointer select-none px-4 py-4 font-semibold transition hover:bg-indigo-100 hover:text-indigo-800"
                  onClick={() => handleSort("lead_time_days")}
                >
                  Lead Time (days){arrow("lead_time_days")}
                </th>

                <th className="px-4 py-4 font-semibold">
                  Validity (days)
                </th>
              </tr>
            </thead>

            <tbody className="text-slate-700">

              {sortedQuotes.map((q) => {
                const isCheapest = q.total_amount === lowestAmount;
                const isFastest = q.lead_time_days === shortestLead;

                return (
                  <tr
                    key={q.id}
                    className={
                      "border-t border-slate-200 transition hover:bg-indigo-50/50 " +
                      (isCheapest ? "bg-emerald-50/70" : "")
                    }
                  >

                    <td className="px-4 py-4 font-medium text-slate-800">
                      {q.vendor_name}
                    </td>

                    <td className="px-4 py-4 font-medium text-indigo-700">
                      {q.quote_number}
                    </td>

                    <td className="min-w-[120px] whitespace-nowrap px-4 py-4">
                      {q.quote_date.split("-").reverse().join("-")}
                    </td>

                    <td className="whitespace-nowrap px-4 py-4 font-semibold text-slate-800">
                      {formatRupees(q.total_amount)}

                      {isCheapest && (
                        <span className="ml-2 inline-block rounded-full bg-emerald-100 px-2.5 py-1 text-xs font-semibold text-emerald-800">
                          Lowest Price
                        </span>
                      )}
                    </td>

                    <td className="px-4 py-4">
                      {q.payment_terms}
                    </td>

                    <td className="whitespace-nowrap px-4 py-4">
                      {q.lead_time_days}

                      {isFastest && (
                        <span className="ml-2 inline-block rounded-full bg-teal-100 px-2.5 py-1 text-xs font-semibold text-teal-800">
                          Fastest
                        </span>
                      )}
                    </td>

                    <td className="px-4 py-4">
                      {q.validity_days}
                    </td>

                  </tr>
                );
              })}

            </tbody>
          </table>
        </div>
      )}

    </div>
  );
}
