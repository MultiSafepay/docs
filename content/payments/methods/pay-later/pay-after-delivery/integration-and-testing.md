---
title: 'Integration and testing Pay After Delivery'
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Integrating and testing Pay After Delivery - MultiSafepay Docs"
short_description: "Options for integrating Pay After Delivery and testing payments"
layout: 'child'
logo: '/logo/Payment_methods/Pay_After_Delivery.svg'
url: '/payment-methods/pay-after-delivery/integration-testing/'
aliases:
    - /payments/methods/billing-suite/pay-after-delivery/integration-and-testing/
---
## Integration

| | |
|---|---|
| **API** | [Direct](/api/#pay-after-delivery---direct) and [redirect](/api/#pay-after-delivery---redirect) |
| **Ready-made integrations** | Pay After Delivery (direct) is supported in all our [ready-made integrations](/integrations/ready-made/).   |
| **Checkout options** | [Multisafepay payment pages](/payment-pages/) {{< br >}} [Payment links](/payment-links/about/) – You can't adjust the lifetime. |
| **Logo** | See MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons). |

## Testing

Test credentials: [API key](/account/site-id-api-key-secure-code/)

### Test a Pay After Delivery order


To test a Pay After Delivery order, make a [direct](api/#pay-after-delivery---direct) or [redirect](api/#pay-after-delivery---redirect) API request.

If you make a redirect API request, click **Pay After Delivery**.  
- Enter in the:
  - **Birthdate** field any date of birth. Format: DD-MM-YYYY.
  - **Bank account** field any 10-digit bank account number.
  - **E-mail address** field any email address.
  - **Phone number** field any phone number.  
- Click **Confirm**.

The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.

### Test declining an order

To decline an order, in your test account under **Order summary**, click **Decline**.  
The order and transaction statuses change to **Void**.

**Notes:** 
You can't test:  
  - Processing refunds
  - Changing the order status to shipped
  - Cancelling orders

