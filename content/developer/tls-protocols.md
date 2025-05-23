---
title: TLS protocols
category: 62962df622e99600810c117d
slug: 'tls-protocols-1'
order: 7
hidden: true
---

To maintain safety and reliability of our services, we periodically upgrade our systems to support the latest security protocols. This update ensures that all payment transactions remain secure and compliant with industry standards. 

**⚠️ Note:** Outdated TLS versions and operating systems may no longer be compatible with our platform.  
This can result in transaction errors, or notifications not being delivered correctly. 

## Required actions

- **Check TLS and cipher suite**: Ensure your systems are supporting TLS 1.2 or higher.
- Review supported **certificates**
- **Check your Operating system**: If you're using older versioned operating systems, consider upgrading to a supported version to ensure compatibility with the newer TLS versions.

## Server used for transaction creation

On the server you use to create transactions, it is obligatory to **support TLS 1.2** with one of the following ciphers

**TLS 1.2**

```text
TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256  
TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256  
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384  
TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA  
TLS_RSA_WITH_AES_128_GCM_SHA256  
TLS_RSA_WITH_AES_256_GCM_SHA384
```
**TLS 1.3**

```text
TLS_CHACHA20_POLY1305_SHA256
TLS_AES_256_GCM_SHA384
TLS_AES_128_GCM_SHA256
```
**How to test**

You can check if your ciphers are supported using the following methods:

- **OpenSSL Command**: Run the following command:

```text
openssl s_client -connect api.multisafepay.com:443
```

- **SSL Server Test**: Go to <a href="https://www.ssllabs.com/ssltest/analyze.html?d=api.multisafepay.com&hideResults=on" target="_blank">SSL Server Test</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> and enter `api.multisafepay.com` as the hostname.
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)