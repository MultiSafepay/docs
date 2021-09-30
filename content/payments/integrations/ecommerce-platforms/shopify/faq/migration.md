---
title : "Migrating to the app"
meta_title: "Shopify app - Migrating to the app - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
read_more: "."
url: 'shopify/migration'
---

The MultiSafepay Payments app offers a faster and safer connection between your Shopify store and MultiSafepay.

To migrate to our new MultiSafepay Payments app:

1. Enable password protection.
2. Install the [MultiSafepay Payments app](https://apps.shopify.com/multisafepay-payments) from the Shopfy app store.
    - To check whether the new payment method is added, go to **Admin** > **Settings** > **Payments** > **Alternative payment methods**.
4. Test the **MultiSafepay** gateway in your Shopify checkout
5. Disable the deprecated MultiSafepay payment methods, go to **Admin** > **Settings** > **Payments** > **Third-party payment providers**.
6. Disable password protection.

{{< details >}}

**1.** Enable password protection.

**2.** Install the [MultiSafepay Payments app](https://apps.shopify.com/multisafepay-payments) from the Shopfy app store.

The app adds a new payment method to your webshop under **Admin** > **Settings** > **Payments** > **Alternative payment methods**.

If you're using a test API key, enable test mode.

**3.** Go to your Shopify checkout and check whether a new **MultiSafepay** gateway appears.

**4.** Test the new gateway. If it works as expected, disable the old MultiSafepay Payment methods under **Admin** > **Settings** > **Payments** > **Third-party payment providers**.

**5.** Disable password protection so your webshop is operational again.

{{< /details >}}

### Refunds

Processing refunds does not change with the new MultiSafepay Payments app.

For more information, see Shopify [Processing refunds](/shopify/refunds)