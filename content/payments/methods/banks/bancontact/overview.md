---
title: "Bancontact overview"
breadcrumb_title: 'Overview'
weight: 10
meta_title: "Bancontact overview - MultiSafepay Docs"
short_description: "Key information, supported countries, currencies, and features"
layout: 'child'
logo: '/logo/Payment_methods/bancontact.svg'
url: '/payment-methods/bancontact/overview/'
aliases: 
    - /payment-methods/bancontact/what-is-bancontact/
    - /payments/methods/banks/bancontact/about/
    - /payments/methods/bancontact/product-rules/
    - /payments/methods/bancontact-qr/product-rules/
    - /payment-methods/bancontact/product-rules/
---
[Bancontact](https://www.bancontact.com/en) is a leading Belgian payment method that supports online, mobile, QR, POS, and wallet payments. It is a household name and supported by over 80% of Belgian webshops. 

Once payment is completed, the customer cannot reverse it and Bancontact guarantees settlement. 

Non-mobile payments always use [3D Secure](/features/3d-secure/) 1.0 verification.

|   |   |   
|---|---|
| **Countries**  | Belgium  | 
| **Currencies**  | EUR | 
| **Chargebacks**  | No – See [Chargebacks](/payments/chargebacks/). | 
| **Refunds** | [Full and partial](/refunds/full-partial/) |
| **Payment features**  | [Recurring Payments](/features/recurring-payments/) (banking only) {{< br >}} [Second Chance](/features/second-chance/) |
| **Transactions expire after**  | Banking: 1 hour, QR: Doesn't apply | 

## Bancontact WIP Service

Bancontact WIP is a wallet initiated payment service you can use for:

- Bancontact One-Click Pay: customer-initiated one-click payments to make checkout faster and increase conversion
- Bancontact Recurring: merchant-initiated subscription payments

### How it works

Bancontact Payconiq gives you access to a merchant wallet to securely store customers' payment details in. Customers give one-time consent and only need to pass [strong customer authentication (SCA)](/payment-regulations/sca/) for their first purchase. 

There is no liability shift from [issuer](/glossaries/multisafepay-glossary/#issuer) to [acquirer](/glossaries/multisafepay-glossary/#acquirer) since your fraud and disputes volumes are monitored quarterly. A maximum transaction amount applies. 

### Criteria and activation

- Bancontact WIP is only available to low-risk, high-volume merchants (25,000 transactions quarterly), within the SEPA area. 
- You must be [PCI DSS](/payment-regulations/pci-dss/) compliant.
- You must have easy-to-use procedures in place for refunds, cancellations, and disputes.
- Customers must be able to add, update, and delete their stored payment details.  
- You must be able to continually demonstrate low rates of fraudulent transactions, or access to your merchant wallet may be revoked. 

Email a request to activate Bancontact WIP to <sales@multisafepay.com>

Requests are screened and approved by Bancontact Payconiq. 

### Integration

See [Recurring Payments](/features/recurring-payments/).



