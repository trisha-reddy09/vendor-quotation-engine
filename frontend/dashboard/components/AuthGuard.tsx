"use client";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

export default function AuthGuard({ children }: { children: React.ReactNode }) {
  const router = useRouter();
  const [allowed, setAllowed] = useState(false);

  useEffect(() => {
    if (localStorage.getItem("loggedIn") === "true") setAllowed(true);
    else router.replace("/login");
  }, [router]);

  return allowed ? <>{children}</> : null;
}