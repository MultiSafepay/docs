---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Bank Transfer - Integration and testing - MultiSafepay Docs"
short_description: "Integrating and testing Bank Transfer in your ecommerce platform"
layout: 'child'
logo: '/logo/Payment_methods/banktransfer-en.svg'
url: '/payment-methods/bank-transfer/integration-testing/'
aliases:
    - /payment-methods/bancontact/bank-transfer-testing
    - /payments/methods/banks/bank-transfer/integration-and-testing/
---

To process Bank Transfer payments via our API, see API reference - [Bank Transfer](/api/#bank-transfer).

For the Bank Transfer logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

{{< details title="View credentials and testing process" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test a Bank Transfer order**

1. To test a Bank Transfer order, send a [redirect](/api/#bank-transfer---redirect) API request.
2. Open the payment link. 
3. In the **Your bank account** field, enter an IBAN. 
4. From the **Bank's country** list, select a country, and then click **Confirm**.

Use the following IBANs to test different transaction statuses.

| IBAN | Status    | Description              |
| ---------| --------- | ------------------------ |
| NL87ABNA0000000001| **Initialized**/ **Completed** | Transaction is initialized. After 2 minutes, this changes to **Completed**. |
| NL87ABNA0000000002| **Initialized**/ **Expired** | Transaction is initialized. After 2 minutes, this changes to **Expired**. |
| NL87ABNA0000000004| **Initialized**/ **Declined** | Transaction is initialized. After 2 minutes, this changes to **Declined**. |
| Any other IBAN | **Initialized**/ **Expired** | Transaction is initialized. After 5 days, this changes to **Expired**. |

**Test cancelling an order**

To test cancelling an order, either:

- Send an [update an order](/api/#update-an-order) API request with status **Cancelled**, or 
- In your MultiSafepay test account, go to **Order summary**, and then click **Cancel**.  
The transaction status changes to **Void**.

**Test refunding an order**

To test refunding an order:

1. Create an order using IBAN: NL87ABNA0000000001. 
2. Wait until the transaction status changes to **Completed**.
3. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
4. Under **Refund**, enter in the:
    - **Account holder name** field the account holder name of the account you want to refund to. 
    - **IBAN** field the IBAN of the account you want to refund to.
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
5. Click **Continue**.
6. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
7. Under **Related transactions**, select the **ID** of the refund order.
8. Under **Order summary**, click **Accept**.
9. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** 

- You can't test the following:
  - Sending a refund API request
  - Sending a direct API request with an IBAN to test different transaction statuses
- In the live environment it is not possible to accept a refund order. This is done automatically.


{{< /details >}}