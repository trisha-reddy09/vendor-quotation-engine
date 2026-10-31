
"use client";

import Link from "next/link";
import { vendors, quotes } from "../src/data/mockData";
import { formatRupees } from "../src/lib/formatters";

export default function HomePage() {
  const totalVendors = vendors.length;
  const totalQuotes = quotes.length;

  const lowestQuote = Math.min(
    ...quotes.map((q) => q.total_amount)
  );

  const averageLeadTime =
    quotes.reduce((total, q) => total + q.lead_time_days, 0) /
    totalQuotes;

  const cards = [
    {
      title: "Total Vendors",
      value: totalVendors,
      description: "Registered vendors",
      color: "border-indigo-200 text-indigo-700",
    },
    {
      title: "Total Quotes",
      value: totalQuotes,
      description: "Quotations received",
      color: "border-blue-200 text-blue-700",
    },
    {
      title: "Lowest Quote",
      value: formatRupees(lowestQuote),
      description: "Most affordable quotation",
      color: "border-emerald-200 text-emerald-700",
    },
    {
      title: "Average Lead Time",
      value: averageLeadTime.toFixed(1) + " days",
      description: "Average vendor delivery time",
      color: "border-teal-200 text-teal-700",
    },
  ];

  return (
    <div className="min-h-screen bg-slate-50 p-6">

      <h1 className="mb-2 text-2xl font-bold text-slate-900">
        Dashboard
      </h1>

      <p className="mb-6 text-sm text-slate-500">
        Welcome to the Vendor Quotation Engine.
        Here is your quotation overview.
      </p>

      {/* Summary Cards */}
      <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">

        {cards.map((card) => (
          <div
            key={card.title}
            className={`rounded-xl border bg-white p-5 shadow-sm ${card.color}`}
          >
            <p className="text-sm font-semibold">
              {card.title}
            </p>

            <h2 className="mt-3 text-2xl font-bold">
              {card.value}
            </h2>

            <p className="mt-2 text-xs text-slate-500">
              {card.description}
            </p>
          </div>
        ))}

      </div>

      {/* Quick Links */}
      <div className="mt-8 rounded-xl border border-slate-200 bg-white p-6 shadow-sm">

        <h2 className="mb-4 text-lg font-bold text-slate-800">
          Quick Actions
        </h2>

        <div className="flex flex-wrap gap-4">

          <Link
            href="/vendors"
            className="rounded-lg bg-indigo-700 px-5 py-3 text-sm font-semibold text-white transition hover:bg-indigo-800"
          >
            View Vendors
          </Link>

          <Link
            href="/quote-comparison"
            className="rounded-lg bg-teal-700 px-5 py-3 text-sm font-semibold text-white transition hover:bg-teal-800"
          >
            Compare Quotes
          </Link>

        </div>

      </div>

    </div>
  );
}
