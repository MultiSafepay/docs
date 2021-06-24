---
title : "Emailing payment instructions yourself"
meta_title: "Bank Transfer - Emailing payment instructions yourself - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
weight: 20

---

To email the payment instructions to the customer yourself, in your POST `/orders` API request, set the `disable_send_email` parameter to `false`. 

This prevents MultiSafepay emailing the customer.

For more information, see API Reference – [Direct bank transfer](/api/#direct-bank-transfer).