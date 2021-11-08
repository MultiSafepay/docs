---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Bancontact - Integration and testing - MultiSafepay Docs"
short_description: "Integrating and testing Bancontact in your ecommerce platform"
layout: 'child'
logo: '/logo/Payment_methods/bancontact.svg'
url: '/payment-methods/bancontact/integration-testing/'
aliases:
    - /payment-methods/bancontact/bancontact-testing
    - /payments/methods/banks/bancontact/integration-and-testing/
    - /payments/methods/banks/bancontact-qr/integration-and-testing/
---

To process payments via our API, see API reference:

- [Bancontact](/api/#bancontact)
- [Bancontact QR](/api/#bancontact-qr)

For the Bancontact logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

{{< details title="View credentials and testing process" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test a Bancontact order**

1. To test a Bancontact order, send a [redirect](/api/#bancontact) API request.
2. Open the payment link.
3. In the **Card number** field, enter a 16-digit card number.
4. In the **Expiry date** fields, enter any future date, and then click **Confirm**.

Use the following card numbers to test different transaction statuses.

| Card number| Status    | Description              |
| ---------| --------- | ------------------------ |
| 67034500054620008 | **Completed** | Transaction was completed (3D enrolled) |
| 67034500054610009| **Declined**  | Transaction was declined (card must be 3D enrolled) |
| 67039902990000045| **Declined**  | Transaction was declined (3D authentication failed) |
| 67039902990000011| **Declined**  | Transaction was declined (3D authentication successful, but insufficient funds) |

---

**Note:** You can see the reason a transaction was declined in your MultiSafepay test account under **Notes**.

---

**Test a Bancontact QR code**
1. Send a [redirect](/api/#bancontact-qr) API request.
2. Open the payment link.
3. Scan the QR code with a general QR reader (**not** the Bancontact app - an error occurs).
4. On the Test platform page, from the **Test scenario** list, select **Completed**, and then click **Test**.

**Test refunding an order**

To test refunding an order:

1. Create an order using card number `67034500054620008`. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

**Test an API refund**

To test refunding an order via the API:

1. Create an order using card number `67034500054620008`. 
2. Send a [refund](/api/#refund-an-order) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
3. In your MultiSafepay test account, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** 

- You can't test cancelling orders. 
- In the live environment, you can't accept refund orders. These are done automatically.

{{< /details >}}

