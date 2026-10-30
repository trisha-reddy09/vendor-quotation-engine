"use client"; // needed because this page uses useState
 
import { useState } from "react";
 
// 1) A component, with props
function VendorItem({ name, city }) {
  return (
    <li className="border-b p-2">
      {name} - {city}
    </li>
  );
}
 
export default function Practice() {
  // 2) State: React re-draws the screen when these change
  const [count, setCount] = useState(0);
  const [text, setText] = useState("");
 
  const list = [
    { id: 1, name: "TechNova", city: "Bengaluru" },
    { id: 2, name: "Orion Systems", city: "Mumbai" },
    { id: 3, name: "Sigma Networks", city: "Delhi" },
  ];
 
  // 3) .filter() keeps matching items
  const shown = list.filter((v) =>
    v.name.toLowerCase().includes(text.toLowerCase())
  );
 
  return (
    <div className="p-6">
      <button
        className="rounded bg-blue-600 px-3 py-1 text-white"
        onClick={() => setCount(count + 1)}
      >
        Clicked {count} times
      </button>
 
      <input
        className="mt-4 block rounded border p-2"
        placeholder="Type to filter"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
 
      {/* 4) .map() draws one component per item; key is required */}
      <ul className="mt-4">
        {shown.map((v) => (
          <VendorItem key={v.id} name={v.name} city={v.city} />
        ))}
      </ul>
    </div>
  );
}
