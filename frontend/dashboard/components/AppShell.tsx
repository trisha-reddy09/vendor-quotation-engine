"use client";
import { usePathname } from "next/navigation";
import Navbar from "./Navbar";
import AuthGuard from "./AuthGuard";

export default function AppShell({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  if (pathname === "/login") return <>{children}</>;
  return (
    <AuthGuard>
      <div className="flex min-h-screen">
        <Navbar />
        <main className="flex-1 p-6">{children}</main>
      </div>
    </AuthGuard>
  );
}