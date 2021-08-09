---
title : "Handling errors"
meta_title: "Gift cards - Handling errors - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
weight: 40
---

VVV gift cards can sometimes throw an error where the credit balance appears to be 0, but is then restored within 24 hours (potentially affected by weekends and holidays). This appears to be due to temporary failures in the card issuer's system. 

If a customer completes a payment and receives this error message, advise them to wait for 1 hour for a confirmation email before trying again to avoid placing two orders.