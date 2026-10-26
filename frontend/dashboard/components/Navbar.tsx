"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";

const links = [
  { href: "/", label: "Dashboard" },
  { href: "/vendors", label: "Vendor List" },
  { href: "/quote-comparison", label: "Quote Comparison" },
];

export default function Navbar() {
  const pathname = usePathname();
  return (
    <nav className="w-56 min-h-screen bg-slate-900 text-white p-4">
      <h2 className="text-lg font-bold mb-6">Quotation Engine</h2>
      <ul className="space-y-2">
        {links.map((l) => (
          <li key={l.href}>
            <Link
              href={l.href}
              className={`block rounded px-3 py-2 ${
                pathname === l.href ? "bg-blue-600" : "hover:bg-slate-700"
              }`}
            >
              {l.label}
            </Link>
          </li>
        ))}
      </ul>
    </nav>
  );
}