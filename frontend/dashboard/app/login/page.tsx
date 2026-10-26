"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";

export default function LoginPage() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  function handleLogin() {
    if (!email || !password) {
      setError("Please enter email and password");
      return;
    }
    localStorage.setItem("loggedIn", "true");
    router.push("/");
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-100">
      <div className="bg-white text-gray-900 p-8 rounded shadow w-80 space-y-4">
        <h1 className="text-xl font-bold">Vendor Quotation Engine</h1>
        <p className="text-sm text-gray-500">Sign in to continue</p>
        <input
          className="w-full border rounded px-3 py-2"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          className="w-full border rounded px-3 py-2"
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        {error && <p className="text-sm text-red-600">{error}</p>}
        <button
          onClick={handleLogin}
          className="w-full bg-blue-600 text-white rounded py-2 hover:bg-blue-700"
        >
          Login
        </button>
      </div>
    </div>
  );
}