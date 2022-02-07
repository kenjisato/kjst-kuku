kjst-kuku
=========

掛け算ドリル

Install
-------

```sh
python -m pip install --upgrade git+https://github.com/kenjisato/kjst-kuku
```

Usage
-----

### 3の段を順番に出題

```sh
kjst-kuku start -o 3
```

### 5の段のシャッフル

```sh
kjst-kuku start 5
```

### 全部をシャッフル

```sh
kjst-kuku start
```

### 3, 4, 6, 8の段をシャッフルしない

```sh
kjst-kuku start -o 3-4/6-8
```


Show Records
------------

Helper commands will come soon. Until then, see 

```sh
cat ~/.kuku_records
```
