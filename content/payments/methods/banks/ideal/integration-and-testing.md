---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "iDEAL - Integration and testing - MultiSafepay Docs"
short_description: "Integrating and testing iDEAL in your ecommerce platform"
layout: 'child'
logo: '/logo/Payment_methods/iDEAL.svg'
url: '/payment-methods/ideal/integration-testing/'
aliases:
    - /payment-methods/ideal/ideal-testing
    - /payments/methods/banks/ideal/integration-and-testing/
    - /payments/methods/banks/idealqr/integration-and-testing/
---

To process payments via our API, see API reference:

- [iDEAL](/api/#ideal)
- [iDEAL QR](/api/#ideal-qr)

## iDEAL QR

MultiSafepay supports seamless integration for iDEAL QR. You can:

- Retrieve and process the PNG image for the QR code in your system to display it to the customer.  

- Redirect the customer to a [MultiSafepay payment page](/payment-pages/) where the iDEAL QR code is displayed under **Payment methods**.

- Generate a generic link that can be used multiple times. 

- Print a QR code, e.g. on leaflets or menus. 

You can enable an option to allow the customer change the amount.

Only 4 Dutch banks support iDEAL QR in their own banking app: Knab, Rabobank, ING, and ABN AMRO. Customers of other banks must use the iDEAL app.

## Testing

{{< details title="View credentials and testing process" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test an iDEAL order**

1. To test an iDEAL order, make a [direct](/api/#ideal---direct) or [redirect](/api/#ideal---redirect) API request.
2. If you make a redirect API request, select a bank.
3. On the Test platform page, from the **Test scenario** list, select **Completed**.
4. Click **Test**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

**Test cancelling an order**

To test cancelling an order:

1. Make a [direct](/api/#ideal---direct) or [redirect](/api/#ideal---redirect) API request.
2. If you make a redirect API request, select a bank. 
3. On the Test platform page, from the **Test scenario** list, select **Cancelled**.
4. Click **Test**.  
  The order status changes to **Void**.

Use the following test scenarios on the Test platform page to test different transaction statuses.

| Status                | Description              |
| --------------------- | ------------------------ |
| **Declined**              | Transaction was declined |
| **Open** **Completed** | Transaction is initialized. After 1 minute, this changes to **Completed**. |
| **Open** **Declined**  | Transaction is initialized. After 1 minute, this changes to **Declined**. |

**Test refunding an order**

To test refunding an order:

1. Create an order. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Account holder name** field the account holder name of the account you want to refund to. 
    - **IBAN** field the IBAN of the account you want to refund to.
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

**Test an API refund**

To test refunding an order via the API:

1. Create an order. 
2. Make a [refund](/api/#refund-an-order) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
3. In your MultiSafepay test account, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** In the live environment, you can't accept refund orders. These are done automatically.

{{< /details >}}

You can't test iDEAL QR in your MultiSafepay test account. You can only make test payments in your MultiSafepay live account.

## Logos

For the iDEAL and iDEAL QR logos, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).