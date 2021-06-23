---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "iDEAL QR - Integration and testing - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Integrating and testing iDEAL QR in your ecommerce platform"
layout: 'child'
logo: '/logo/Payment_methods/iDeal-qr.svg'
aliases:
    - /payment-methods/ideal/ideal-testing
---

To integrate iDEAL QR using our API, see API Reference - [iDEAL QR](/api/#ideal-qr).

MultiSafepay supports seamless integration for iDEAL QR. You can:

- Retrieve and process the PNG image for the QR code in your system to display it to the customer.  

- Redirect the customer to a MultiSafepay PayV2 page where the iDEAL QR code is displayed under **Payment methods**.

- Generate a generic link that can be used multiple times. 

- Print a QR code, e.g. on leaflets or menus. 

You can enable an option to allow the customer change the amount.

Only 4 Dutch retail banks support iDEAL QR in their own banking app: Knab, Rabobank, ING, and ABN AMRO. Customers of other banks must use the iDEAL app.

{{< details title="About testing" >}}
  &nbsp;  
You cannot test iDEAL QR in your MultiSafepay test account. You can only make test payments in your live MultiSafepay account.

{{< /details >}}