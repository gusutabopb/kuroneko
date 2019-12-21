# kuroneko

ヤマト運輸の荷物追跡を行うための簡単なCLIツール。

Python環境(v2.7, v3.5+)が必要です。

## インストール

```bash
$ git clone https://github.com/gusutabopb/kuroneko.git
$ pip install ./kuroneko
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

![](https://user-images.githubusercontent.com/4231387/71304052-3f60d080-2404-11ea-902e-af18c572bd4b.gif)
