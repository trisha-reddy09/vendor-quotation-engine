"use client";

import { useEffect, useSyncExternalStore, type ReactNode } from "react";
import { useRouter } from "next/navigation";

function subscribe(callback: () => void) {
  window.addEventListener("storage", callback);
  return () => window.removeEventListener("storage", callback);
}

export default function AuthGuard({ children }: { children: ReactNode }) {
  const router = useRouter();

  const loggedIn = useSyncExternalStore(
    subscribe,
    () => localStorage.getItem("loggedIn") === "true", // value in the browser
    () => false // value while the server renders
  );

  useEffect(() => {
    if (!loggedIn) router.replace("/login");
  }, [loggedIn, router]);

  return loggedIn ? <>{children}</> : null;
}