---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Mastercard - Integration and testing - MultiSafepay Docs"
short_description: "Integrating and testing Mastercard in your ecommerce platform"
layout: 'child'
aliases:
    - /payment-methods/credit-and-debit-cards/mastercard/mastercard-testing
    - /payment-methods/credit-and-debit-cards/mastercard/credit-card-payment-page
---

There are two options for integrating Mastercard, depending on whether you want to accept multiple credit cards or Mastercard only. 

#### Multiple credit cards
 
Customers are redirected to a MultiSafepay credit card payment page, where all credit cards are bundled together. This saves space in your checkout. Customers enter their payment details and the page detects the specific card scheme based on the first four digits.

See API reference – [Credit cards](/api/#credit-cards).

#### Mastercard only
Customers are redirected straight to Mastercard. 

See API reference – [Mastercard](/api/#mastercard).

## Testing

{{< details title="View credentials and testing process" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

Testing Mastercard is similar to Visa. For extensive testing, see [Visa](/testing/test-payment-details/#details-visa). 

**Test a Mastercard order**  

1. Make a [redirect](/api/#mastercard) API request.
2. On the payment page:
    - In the **Card number** field, enter `5500000000000004`.
    - In the **Card holder** field, enter any name.
    - From the **Expiry date** lists, select any future date.
    - In the **CVC/CVV** field, enter `123`.
    - Click **Confirm**.
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

**Test refunding an order**

To refund an order:

1. Create an order. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
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

For the Mastercard logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).