---
title: "Validating the customer IP address"
weight: 10
meta_title: "FAQ API - Validating customer IP address - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /faq/api/ip_address
---

#### ip_address
For post-payment and credit card payment methods, the customer's `ip_address` must be validated. The normally optional `ip_address` parameter in the JSON request becomes a required parameter.

**Note:** When validating the localhost `ip_address` instead of the customer's `ip_address`, transactions may receive **Uncleared** status, any may even be declined.


   "customer": {
        "ip_address": "31.148.195.10",
        "forwarded_ip": "" 
```

#### forwarded_ip

The X-FORWARDED-FOR header of the customer request when using a proxy.

To retrieve the customer's IP address:

- If there is a proxy, use `forwarded_ip`
- Otherwise, use `ip_address`


#### Uncleared or Declined status
Validating the customer's IP address may cause a transaction to unnecessarily receive **Uncleared** status, or even to be declined. 

Before a payment is accepted, we run a fraud check on the transaction, including checking the required `ip_address` parameter. If the parameter is empty or incorrect (e.g. it's the IP address of the webshop instead of the customer), the transaction will likely receive **Uncleared** status. 

Credit cards and post-payment methods carry a high risk of fraud, so each transaction is automatically validated for your protection. 
