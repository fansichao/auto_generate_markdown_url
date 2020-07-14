# auto_generate_markdown_url

功能说明

- 根据文件目录，自动生成 MarkDown URL 链接。
- 根据文件目录，自动生成 文件目录树
- 适合 Windows 系统

## 命令说明

```bash
PS D:\@vscode\auto_generate_markdown_url> python .\dirtree.py --help
Usage: 根据目录 生成 文件目录树 和 MarkDown链接

Options:
  -h, --help            show this help message and exit
  --name=FILE, --username=FILE
                        Github 用户名称:
  --repo=GITHUB_REPONAME, --reponame=GITHUB_REPONAME
                        GitHub 仓库名称:
  --local=LOCAL_PATH, --local_path=LOCAL_PATH
                        本地文件目录:
  --save=SAVE_PATH, --save_path=SAVE_PATH
                        保存在Github的位置:
  --tree=TREE_FILE_PATH, --tree_file_path=TREE_FILE_PATH
                        目录树保存的文件名称:
```

## 命令样例

```bash
python .\dirtree.py --local_path=demo --save_path=/demo
```

## 目录树效果

目录树，效果如下

```bash
----demo\
    |----A1\
    |    |----A11\
    |    |    |----demo110.txt
    |    |    |----readme.md
    |    |----demo11.txt
    |    |----demo12.txt
    |    |----readme.md
    |----A2\
    |----demo01.txt
    |----demo02.txt
    |----readme.md

```

## 目录 MarkDown 链接效果

目录 MarkDown 链接，效果如下

- [demo](https://github.com/fansichao/auto_generate_markdown_url/tree/master/demo)
  - [A1](https://github.com/fansichao/auto_generate_markdown_url/tree/master/demo/A1)
    - [A11](https://github.com/fansichao/auto_generate_markdown_url/tree/master/demo/A11)
      - [demo110.txt](https://github.com/fansichao/auto_generate_markdown_url/blob/master/demo/A1/A11/demo110.txt)
      - [readme.md](https://github.com/fansichao/auto_generate_markdown_url/blob/master/demo/A1/A11/readme.md)
    - [demo11.txt](https://github.com/fansichao/auto_generate_markdown_url/blob/master/demo/A1/demo11.txt)
    - [demo12.txt](https://github.com/fansichao/auto_generate_markdown_url/blob/master/demo/A1/demo12.txt)
    - [readme.md](https://github.com/fansichao/auto_generate_markdown_url/blob/master/demo/A1/readme.md)
  - [A2](https://github.com/fansichao/auto_generate_markdown_url/tree/master/demo/A2)
  - [demo01.txt](https://github.com/fansichao/auto_generate_markdown_url/blob/master/demo/demo01.txt)
  - [demo02.txt](https://github.com/fansichao/auto_generate_markdown_url/blob/master/demo/demo02.txt)
  - [readme.md](https://github.com/fansichao/auto_generate_markdown_url/blob/master/demo/readme.md)
