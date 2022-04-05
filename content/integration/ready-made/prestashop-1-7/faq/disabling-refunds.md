---
title : "Disabling refunds"
meta_title: "PrestaShop 1.7 - Disabling refunds - MultiSafepay Docs"
read_more: "."
url: '/prestashop-1-7/disable-refunds/'
---
**Disable refunds**

if you don't want refunds made from your PrestaShop [backend](/glossaries/multisafepay-glossary/#backend) to automatically process with the MultiSafepay API, you can disable this by following these steps:

1. Sign in to your PrestaShop 1.7 backend.
2. Go to **MultiSafepay module** > **Manage hooks**.
3. Select **Display non-positionable hooks**.
4. Find **actionOrderSlipAdd**, select the three dots and click on **Unhook**.