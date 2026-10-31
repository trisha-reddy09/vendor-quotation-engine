
import { vendors } from "../../src/data/mockData";

export default function VendorsPage() {
  return (
    <div className="min-h-screen bg-slate-50 p-6 text-slate-800">
      <h1 className="mb-2 text-2xl font-bold text-slate-900">
        Vendor List
      </h1>

      <p className="mb-6 text-sm text-slate-500">
        View all registered vendors and their details.
      </p>

      <div className="mb-5 rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
        <p className="text-sm font-medium text-slate-500">
          Total Registered Vendors
        </p>
        <p className="mt-2 text-3xl font-bold text-indigo-700">
          {vendors.length}
        </p>
      </div>

      <div className="overflow-x-auto rounded-xl border border-slate-200 bg-white shadow-sm">
        <table className="min-w-full text-left text-sm">
          <thead className="bg-slate-100 text-slate-700">
            <tr>
              <th className="px-4 py-4">Vendor Name</th>
              <th className="px-4 py-4">Email</th>
              <th className="px-4 py-4">Phone</th>
              <th className="px-4 py-4">Address</th>
              <th className="px-4 py-4">GST Number</th>
            </tr>
          </thead>

          <tbody>
            {vendors.map((vendor) => (
              <tr
                key={vendor.id}
                className="border-t border-slate-200 hover:bg-indigo-50"
              >
                <td className="px-4 py-4 font-semibold">
                  {vendor.vendor_name}
                </td>
                <td className="px-4 py-4">{vendor.contact_email}</td>
                <td className="px-4 py-4">{vendor.phone}</td>
                <td className="px-4 py-4">{vendor.address}</td>
                <td className="px-4 py-4">{vendor.gst_number}</td>
              </tr>
            ))}
          </tbody>
        </table>

        {vendors.length === 0 && (
          <p className="p-6 text-center text-slate-500">
            No vendors found.
          </p>
        )}
      </div>
    </div>
  );
}
