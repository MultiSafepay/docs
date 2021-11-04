---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Dotpay - Integration and testing - MultiSafepay Docs"
short_description: "Integrating and testing Dotpay in your ecommerce platform"
layout: 'child'
logo: '/logo/Payment_methods/Dotpay.svg'
url: '/payment-methods/dotpay/integration-testing/'
aliases:
    - /payment-methods/dotpay/dotpay-testing
    - /payments/methods/banks/dotpay/integration-and-testing/
---

To process Dotpay payments via our API, see API reference – [Dotpay](/api/#dotpay).

For the Dotpay logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

{{< details title="View credentials and testing process" >}}

Test credentials:

- [API key](/account/site-id-api-key-secure-code/)

**Test a Dotpay order**

1. To test a Dotpay order, send a [redirect](/api/#dotpay) API request.
2. On the Dotpay page, in the **E-mail address** field, enter any email address.
3. In the **Phone number** field, enter any phone number.
4. Select a bank.  
  You are automatically redirected.
5. On the Test platform page, from the **Test scenario** list, select **Completed**, and then click **Test**.
6. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

---

**Note:** You may see more banks available in the live environment.

---

**Test refunding an order**

To test refunding an order:

1. Create an order.
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, in the **Account holder name** field, enter the account holder name of the account you want to refund to. 
4. In the **IBAN** field, enter the IBAN of the account you want to refund to.
5. In the **Reason/Description** field, enter a reason for the refund. 
6. In the **Amount** field, enter the amount to refund, and then click **Continue**.
7. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
8. Under **Related transactions**, select the **ID** of the refund order.
9. Under **Order summary**, click **Accept**.
10. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** 

- You can't test cancelling an order. 
- You can't test sending a refund API request.
- In the live environment you can't accept a refund order. This is done automatically.

{{< /details >}}