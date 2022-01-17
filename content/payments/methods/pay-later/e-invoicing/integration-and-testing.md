---
title: 'Integrating and testing E-Invoicing'
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Integrating and testing E-Invoicing - MultiSafepay Docs"
short_description: "Options for integrating E-Invoicing and testing payments"
layout: 'child'
url: '/payment-methods/e-invoicing/integration-testing/'
aliases:
    - /payments/methods/billing-suite/e-invoicing/integration-and-testing/
---
## Integration

| | |
|---|---|
| **API** | [Direct](/api/#e-invoicing---direct) and [redirect](/api/#e-invoicing---redirect) |
| **Ready-made integrations** | E-Invoicing (direct) is supported in all our [ready-made integrations](/integrations/ready-made/).  |
| **Checkout options** | [Multisafepay payment pages](/payment-pages/) {{< br >}} [Payment links](/payment-links/about/) – You can't adjust the lifetime. |
| **Logo** | See MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons). |

## Testing 

Test credentials: [API key](/account/site-id-api-key-secure-code/)

### Test an E-Invoicing order

To test an E-Invoicing order, make a [direct](/api/#e-invoicing---direct) or [redirect](/api/#e-invoicing---redirect) API request.

If you make a redirect API request:
- Enter in the:
  - **Birthdate** field any date of birth. Format: DD-MM-YYYY.
  - **Bank account** field any 10-digit bank account number.
  - **Email address** field any email address.
  - **Phone number** field any phone number.
- Click **Confirm**.

The payment is processed in the test environment as **Successful**, with order and transaction statuses **Uncleared**.

### Test declining an order

To decline an order, in your test dashboard under **Order summary**, click **Decline**.  
The order and transaction statuses change to **Void**.

### Test shipping an order

To test shipping an order, make an [update an order](/api/#update-an-order) API request with status `"shipped"`. You receive the `invoice_url` in the API response.

**Notes:** 
You can't test:
- Processing refunds
- Cancelling orders
