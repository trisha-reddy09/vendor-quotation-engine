# Vendor Quotation Engine

An AI-driven procurement microservice for processing, standardizing, comparing, and ranking vendor quotations for IT hardware procurement.

## Project Overview

The **Vendor Quotation Engine** is a standalone microservice designed as part of an Enterprise Procurement SaaS/ERP platform for IT hardware distributors, system integrators, and procurement firms.

The system helps procurement teams evaluate vendor quotations by standardizing quotation data and comparing important factors such as pricing, payment terms, shipping lead time, and historical vendor performance.

The goal is to provide a reliable and intelligent way to identify the most suitable and profitable procurement option.

## Objectives

The system aims to:

- Ingest vendor RFQ (Request for Quotation) responses
- Standardize and normalize quotation data
- Store vendor and quotation information
- Compare multiple vendor quotations
- Evaluate payment terms and shipping lead times
- Consider historical vendor performance
- Rank vendors using a Python-based scoring system
- Extract structured information from PDF quotations using local AI models
- Provide procurement teams with a clear vendor comparison dashboard

## System Components

### 1. Vendor Management

Manages vendor information and provides APIs for creating, retrieving, updating, and deleting vendor records.

### 2. Quote Management

Handles vendor RFQ responses and stores structured quotation information for comparison.

### 3. Quote Normalization

Converts different vendor quotation formats into a standardized structure so that quotations can be compared consistently.

### 4. Vendor Ranking Engine

Uses Python-based scoring logic to evaluate vendors based on factors such as:

- Pricing
- Payment terms
- Shipping lead time
- Historical performance
- Other relevant procurement factors

### 5. AI-Powered PDF Extraction

Uses **LangChain** and local Large Language Models (LLMs) to extract relevant information from vendor PDF quotations and map the extracted data into the database.

### 6. Procurement Dashboard

Provides a web-based interface for viewing vendors, comparing quotations, and displaying ranked procurement options.

## Technology Stack

| Component | Technology |
|-----------|------------|
| Backend | Python, FastAPI |
| Database | PostgreSQL |
| Frontend | React.js / Next.js |
| AI / LLM | LangChain + Local LLMs |
| Containerization | Docker |
| Testing | PyTest, Jest |
| API Documentation | Swagger / OpenAPI |
| Version Control | Git + GitHub |

## Project Structure

```text
vendor-quotation-engine/
│
├── backend/
│   ├── app/
│   └── tests/
│
├── frontend/
│
├── README.md
├── .gitignore
└── docker-compose.yml

## Contributors

Trisha Reddy
Tanmayi Maram

## Project Status

🚧 Currently under development
