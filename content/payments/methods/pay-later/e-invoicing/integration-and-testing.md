---
title: 'Integration and testing'
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "E-Invoicing - Integration and testing - MultiSafepay Docs"
short_description: "Integrating and testing E-Invoicing in your ecommerce platform"
layout: 'child'
url: '/payment-methods/e-invoicing/integration-testing/'
aliases:
    - /payments/methods/billing-suite/e-invoicing/integration-and-testing/
---

To integrate E-Invoicing using our API, see API reference – [E-Invoicing](/api/#e-invoicing).

For the E-Invoicing logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

{{< details title="View credentials and testing process" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test an E-Invoicing order**

To test an E-Invoicing order, send a [direct](/api/#e-invoicing---direct) or [redirect](/api/#e-invoicing---redirect) API request.

If you send a redirect API request:
- Enter in the:
  - **Birthdate** field any date of birth. Format: DD-MM-YYYY.
  - **Bank account** field any 10-digit bank account number.
  - **Email address** field any email address.
  - **Phone number** field any phone number.
- Click **Confirm**.

The payment is processed in the test environment as **Successful**, with order and transaction statuses **Uncleared**.

**Test declining an order**  

To decline an order, in your test account under **Order summary**, click **Decline**.  
The order and transaction statuses change to **Void**.

**Test cancelling an order**

To test cancelling an order:

1. Send a [direct](/api/#e-invoicing---direct) API request.
2. Either:
    - Send an [update an order](/api/#update-an-order) API request with status `"cancelled"`, or 
    - In your MultiSafepay test account, go to **Order summary** > **Order status**.
    - From **Change status to**, select **Cancelled**
    - In the **memo** field enter a reason
    - Click **Ok**.  
  The transaction status changes to **Void** and the order status changes to **Cancelled**.

**Test shipping an order**  

To test shipping an order, send an [update an order](/api/#update-an-order) API request with status `"shipped"`. You receive the `invoice_url` in the API response.

---

**Note:** You can't test processing refunds.

{{< /details >}}