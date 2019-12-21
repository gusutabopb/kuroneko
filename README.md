# kuroneko

ヤマト運輸の荷物追跡を行うための簡単なCLIツール。

## インストール

```bash
$ git clone https://github.com/gusutabopb/kuroneko.git
$ pip install kuroneko
```

## 使い方

```text
usage: kuroneko [-h] [--ascii] tracking_codes [tracking_codes ...]

Get delivery status of takyubin package

positional arguments:
  tracking_codes  Tracking codes

optional arguments:
  -h, --help      show this help message and exit
  --ascii         Print using ASCII characters only
```