---
title: Email authentication
category:
  uri: Developers
slug: email-authentication
position: 0
privacy:
  view: public
---
# SPF records for MultiSafepay emails

Sender Policy Framework (SPF) records let you specify who is authorized to send emails on your domain's behalf. Receiving email servers can check the SPF record to verify the sender. Using an SPF record prevents emails sent by MultiSafepay on your behalf from being marked as spam.

1. Through your hosting provider, domain registrar, or DNS provider, create a DNS TXT record that is named after your domain, e.g. `example.com`.
2. Add the following string your TXT record containing `v=spf1`: `include:spf.multisafepay.com`

**⚠️ Note:** SPF records may contain a total of 10 DNS lookups (`include` and `mx`). If you have reached this limit, add our IP addresses instead: `ip4:213.189.0.0/23 ip4:185.99.128.0/22`.

✅ **Success!** You have created an SPF record.

### Examples

#### Original TXT record

```
example.com.              180     IN      TXT     "v=spf1 mx ip4:188.18.131.146/32 ip4:177.50.28.21/32 ~all"
```

#### Modified TXT record with DNS lookup

```
example.com.              180     IN      TXT     "v=spf1 mx ip4:188.18.131.146/32 ip4:177.50.28.21/32 include:spf.multisafepay.com ~all"
```

#### Modified TXT record with IP addresses

```
example.com.              180     IN      TXT     "v=spf1 mx ip4:188.18.131.146/32 ip4:177.50.28.21/32 ip4:213.189.0.0/23 ip4:185.99.128.0/22 ~all"
```

# DKIM email authentication

MultiSafepay supports DomainKeys Identified Mail (DKIM) email authentication for all emails that we send. DKIM lets email servers verify that received emails actually came from the specified domain and haven't been altered or forged.

To set up DKIM you need to add a TXT record for MultiSafepay through your hosting provider, domain registrar, or DNS provider.

## MultiSafepay email servers

1. Add a TXT record named: `msp-2021._domainkey.{your domain}`, e.g. `msp-2021._domainkey.example.com`.
2. Add the following content to your TXT record:
   ```
   v=DKIM1; h=sha256; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4pizvsOWTWxtcxthGR0k4rEcGsJH4hRy1fpoUAs3fUi0yMkygwsYUCtFLQY2TwrOtfPfaZ/2bPKXwyjC4kg93zFvSJTIQtQiFfKNT2aDtnDmZRwII4+s2k7+LHn4V/SjIxEBylN3Rt0g4iVlkZzgncEXeVksXj5eux8uDAUeZxj0Fp8PWSkxsBNVaJFb5sfR+c5piJ+8RmlqYUf7w/gXOW8mChC509//V9dfMaV39b7WoEf/JRw9KGM69C3hIdtb7cVKD/B6VxQIq3z1DCAcmSCXpcaXUaFbVaF4u/vEi+3v5DdPtDl/0rOy2NUFNL5XULW8OxdofzUbdL9SWN/IbwIDAQAB;
   ```

✅ **Success!** You have added a TXT record for MultiSafepay's email servers.

## Mandrill

If you have [E-Invoicing](/docs/e-invoicing/) or [Pay After Delivery](/docs/pay-after-delivery/) activated, we also use Mandrill to send emails in addition to our own mail servers. In this case, you need to add another TXT record for Mandrill.

1. Add a TXT record named: `mandrill._domainkey.{your domain}`, e.g. `mandrill._domainkey.example.com`.
2. Add the following content to your TXT record:
   ```
   v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCrLHiExVd55zd/IQ/J/mRwSRMAocV/hMB3jXwaHH36d9NaVynQFYV8NaWi69c1veUtRzGt7yAioXqLj7Z4TeEUoOLgrKsn8YnckGs9i3B3tVFB+Ch/4mPhXWiNfNdynHWBcPcbJ8kjEQ2U8y78dHZj1YeRXXVvWob2OaKynO8/lQIDAQAB;
   ```

✅ **Success!** You have added a TXT record for Mandrill.

***

<blockquote class="callout callout_info">
    <h3 class="callout-heading false">
        <span class="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:integration@multisafepay.com">integration@multisafepay.com</a></p>
</blockquote>

[Top of page](#)
