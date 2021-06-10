---
title: "How to refund a Request to Pay order"
weight: 23
meta_title: "Request to Pay, how to refund a transaction - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
aliases: 
    - /payment-methods/banks/direct-bank-transfer/#request-refund
    - /payment-methods/banks/direct-bank-transfer/#refund-flow
---
## Request refund
Please follow these steps to refund a Request to Pay transaction:

1. Log in to your [MultiSafepay Control](https://merchant.multisafepay.com)
2. Select **Transactions** > **Transaction overview**
3. Find the transaction through search
4. Open the transaction
5. Select **refund**
6. Fill in the amount that you are going to refund to the customer
7. Confirm the refund.

The transaction status is now **initialized**. As long as the transaction status is marked as **initialized**, the refund can be cancelled. When the transaction status is marked as **completed**, the refund is processed correctly. The customer will receive the refund to the bank account number in which the transaction was originally paid to, within the next business day

Refunds are only processed if your MultiSafepay balance is sufficient.

**Note**: All refunds will be processed by Deutsche Bank.





