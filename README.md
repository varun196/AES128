# AES encryption decryption app

A simple AES-128 bit encryption - decryption app.  

### Host

Hosted on encryptit.herokuapp.com  

### Usage

For encryption / decryption, send a POST request to:  
`encryptit.herokuapp.com/encrypt/`  

Ensure that `Content-Type` is set to `application/json`.  

Encryption:
```json
{
  "key":"16 char key",
  "mode":"e",
  "values":[
    "First str","second str","and so on"
  ]
}
```

Decryption:
```json
{
  "key":"16 char key",
  "mode":"d",
  "values":[
    "0AvVP4YQTyMyqfmoClruHotgCE/E0w0pvKNhP79kay0=","0AvVP4YQTyMyqfmoClruHotgCE/E0w0pvKNhP79kay0="
  ]
}
```

### Future extensions  

- [ ] Ensure input key is 16-digit key 
- [ ] Ensure requests come over HTTPS
- [ ] Upgrade to djago 2.2.3 or later
- [ ] provide 256 bit encryption support

- [ ] Create a webapp to facilitate e/d 