
// Mock data for Sprint 3.
// Field names mirror the vendors and quotes tables.

export const vendors = [
  {
    id: 1,
    vendor_name: "TechNova Distributors",
    contact_email: "sales@technova.example",
    phone: "9876500001",
    address: "Bengaluru",
    gst_number: "29ABCDE1234F1Z5",
  },
  {
    id: 2,
    vendor_name: "Bharat IT Hardware",
    contact_email: "quotes@bharatit.example",
    phone: "9876500002",
    address: "Chennai",
    gst_number: "33BHRTI5678K1Z2",
  },
  {
    id: 3,
    vendor_name: "Orion Systems Pvt Ltd",
    contact_email: "sales@orionsys.example",
    phone: "9876500003",
    address: "Mumbai",
    gst_number: "27ORNSY9012M1Z8",
  },
  {
    id: 4,
    vendor_name: "Nova Industrial Supplies",
    contact_email: "info@novaindustrial.example",
    phone: "9876500004",
    address: "Hyderabad",
    gst_number: "36NOVAI3456P1Z1",
  },
  {
    id: 5,
    vendor_name: "Sigma Networks",
    contact_email: "sales@sigmanet.example",
    phone: "9876500005",
    address: "Delhi",
    gst_number: "07SIGMN7890Q1Z4",
  },
];

export const quotes = [
  { id: 1, vendor_id: 1, vendor_name: "TechNova Distributors", quote_number: "Q-1001", quote_date: "2026-09-20", total_amount: 120000, payment_terms: "Net-30", lead_time_days: 15, validity_days: 30 },
  { id: 2, vendor_id: 1, vendor_name: "TechNova Distributors", quote_number: "Q-1002", quote_date: "2026-09-28", total_amount: 98500, payment_terms: "Net-45", lead_time_days: 21, validity_days: 45 },
  { id: 3, vendor_id: 2, vendor_name: "Bharat IT Hardware", quote_number: "Q-2001", quote_date: "2026-09-18", total_amount: 95000, payment_terms: "Net-30", lead_time_days: 10, validity_days: 60 },
  { id: 4, vendor_id: 2, vendor_name: "Bharat IT Hardware", quote_number: "Q-2002", quote_date: "2026-09-30", total_amount: 134000, payment_terms: "Advance", lead_time_days: 7, validity_days: 30 },
  { id: 5, vendor_id: 3, vendor_name: "Orion Systems Pvt Ltd", quote_number: "Q-3001", quote_date: "2026-09-22", total_amount: 110250, payment_terms: "Net-45", lead_time_days: 18, validity_days: 45 },
  { id: 6, vendor_id: 3, vendor_name: "Orion Systems Pvt Ltd", quote_number: "Q-3002", quote_date: "2026-10-01", total_amount: 87500, payment_terms: "Net-30", lead_time_days: 30, validity_days: 30 },
  { id: 7, vendor_id: 4, vendor_name: "Nova Industrial Supplies", quote_number: "Q-4001", quote_date: "2026-09-25", total_amount: 142000, payment_terms: "Net-45", lead_time_days: 12, validity_days: 60 },
  { id: 8, vendor_id: 4, vendor_name: "Nova Industrial Supplies", quote_number: "Q-4002", quote_date: "2026-10-02", total_amount: 105000, payment_terms: "Advance", lead_time_days: 9, validity_days: 15 },
  { id: 9, vendor_id: 5, vendor_name: "Sigma Networks", quote_number: "Q-5001", quote_date: "2026-09-27", total_amount: 76500, payment_terms: "Net-30", lead_time_days: 25, validity_days: 30 },
  { id: 10, vendor_id: 5, vendor_name: "Sigma Networks", quote_number: "Q-5002", quote_date: "2026-10-03", total_amount: 118750, payment_terms: "Net-45", lead_time_days: 14, validity_days: 45 },
];
