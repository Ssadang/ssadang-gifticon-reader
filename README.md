# Settings

## Activate Virtualenv
```bash
$ pip install virtualenv
$ virtualenv env
$ source env/Scripts/activate
```

```bash
$ pip install -r requirements.txt
```

---

# Usage

## start python file
```bash
$ python flask_server.py
```

## send request

- data request url : POST `https://localhost:5000/process-ocr`
- Content-Type : application/json
- Body : {"imageUrl" : "<imageurl>"}
- Response
  - ```
    {
      "text" : "<result text (ex: "교환처 : 스타벅스\n\n상품명 : 카페 아메리카노\n\n수량 : 1개\n\n 유효기간 : 24.11.08 ~ 24.12.08\n(Barcode Number)\n"
    }
    ```

