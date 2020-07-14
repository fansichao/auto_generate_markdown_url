'''
功能说明:
- 根据文件目录 自动生成 文件目录树
- 根据文件目录 自动生成 MarkDown URL 链接

使用说明:
- python .\dirtree.py --help
- python .\dirtree.py --local_path=demo --save_path=/demo
'''
from pathlib import Path
import copy
import os
import sys

from optparse import OptionGroup, OptionParser

if not sys.version.startswith('3'):
    raise ValueError('>> 请使用 Python3 版本')


class DirectionTree(object):

    def __init__(self,   local_path='.', save_path='/', github_username=None,
                 github_reponame=None, tree_file_path='tree.txt', ignore_items=None):
        u"""
            :params local_path: 本地文件路径
            :params save_path: 保存在Github的位置
            :params github_username: Github用户名称
            :params github_reponame: Github仓库名称
            :params tree_file_path: 保存文件路径. 目录树保存位置           
            :params ignore_items: 忽略项
        """
        super(DirectionTree, self).__init__()

        self.pathname = Path(local_path)
        self.tree_file_path = tree_file_path
        self.github_username = github_username
        self.github_reponame = github_reponame
        self.save_path = save_path

        self.local_path_dirnames = self.get_base_dir(local_path)
        # 忽略项
        self.ignore_items = ignore_items or ['.git', '.vscode', 'Private']
        # 生成目录
        self.generate_github_dir()

        # 目录树
        self.tree = ''
        # MarkDown链接
        self.href = ''

    def _print_config_info(self):
        u"""输出配置信息"""
        pass

    def generate_github_dir(self):
        u""" 生成 github 文件目录

        exp:
            # github 有目录情况 文件实际路径
            github_hav_dir_url = 'https://github.com/fansichao/auto_generate_markdown_url/tree/master/'
            # github 无目录情况 文件实际路径
            github_not_dir_url = 'https://github.com/fansichao/auto_generate_markdown_url/blob/master/'
        """

        self.github_hav_dir_url = '/'.join(['https://github.com', self.github_username,
                                            self.github_reponame, 'tree/master'])
        self.github_not_dir_url = '/'.join(['https://github.com', self.github_username,
                                            self.github_reponame, 'blob/master'])

    def set_local_path(self, local_path):
        " 重设本地目录 "
        self.pathname = Path(local_path)

    def set_save_path(self, tree_file_path):
        " 重设保存文件 "
        self.tree_file_path = tree_file_path

    def get_base_dir(self, filepath):
        '''
        @msg: 获取文件路径的所有子目录/文件
        filepath = 'D:\@vscode\Code\dirtree.py'
        @return: [WindowsPath('D:/'), '@vscode', 'Code', 'dirtree.py']
        '''

        filepath = Path(filepath)
        dirnames = []
        dirname = copy.deepcopy(filepath)
        for i in range(10):
            dir1 = dirname.parent
            name1 = dirname.name
            dirname = copy.deepcopy(dir1)
            if name1 not in dirnames and bool(name1):
                dirnames.insert(0, name1)
            if i == 9:
                dirnames.insert(0, dir1)

        return dirnames

    def generate_tree(self, n=0):

        if self.pathname.is_file():
            dirnames = self.get_base_dir(self.pathname)
            # self.local_path_dirnames [WindowsPath('D:/'), '@vscode']

            for i in self.local_path_dirnames:
                # dirnames ['Code', 'dirtree.py']
                if i in dirnames:
                    dirnames.pop(dirnames.index(i))
                else:
                    return
            # dirnames.pop(0)

            name = self.pathname.name
            self.tree += '    |' * n + '-' * 4 + name + '\n'
            # path_name Code/dirtree.py
            path_name = '/'.join([str(a) for a in dirnames])

            if self.save_path == '/':
                remote_github_path = self.github_not_dir_url + '/' + path_name
            else:
                remote_github_path = self.github_not_dir_url + self.save_path + '/' + path_name

            self.href += '  '*n + \
                '- [%s](%s)' % (name,  remote_github_path) + '\n'
        elif self.pathname.is_dir():
            name = str(self.pathname.relative_to(self.pathname.parent))
            self.tree += '    |' * n + '-' * 4 + name + '\\' + '\n'
            if self.save_path == '/':
                remote_github_path = self.github_hav_dir_url
            else:
                remote_github_path = self.github_hav_dir_url + self.save_path

            if not bool(self.href):
                self.href += '  '*n + \
                    '- [%s](%s)' % (name, remote_github_path) + '\n'
            else:
                self.href += '  '*n + \
                    '- [%s](%s)' % (name, remote_github_path+'/'+name) + '\n'

            for cp in self.pathname.iterdir():
                if bool([i for i in self.ignore_items if str(cp).find(i) != -1]):
                    continue
                self.pathname = Path(cp)
                self.generate_tree(n + 1)

    def save_file(self):
        # with open(self.tree_file_path, 'w',encoding='utf-8') as f:
        with open(self.tree_file_path, 'wb') as f:
            f.write(self.tree.encode('utf-8'))


if __name__ == '__main__':
    # 配置默认参数
    defalut_tree_file_path = 'tree.txt'
    defalut_local_path = 'D:\\@vscode\\auto_generate_markdown_url'
    defalut_local_path = '.'
    default_github_username = 'fansichao'
    default_github_reponame = 'auto_generate_markdown_url'
    defalut_save_path = '/'

    usage = "根据目录 生成 文件目录树 和 MarkDown链接"
    parser = OptionParser(usage)  # 带参的话会把参数变量的内容作为帮助信息输出
    parser.add_option("--name", "--username", dest="github_username", action="store",
                      help="Github 用户名称:", metavar="FILE", type="string", default=default_github_username)
    parser.add_option("--repo", "--reponame", dest="github_reponame", action="store",
                      help="GitHub 仓库名称:", default=default_github_reponame)
    parser.add_option("--local", "--local_path", dest="local_path", action="store",
                      help="本地文件目录:", default=defalut_local_path)
    parser.add_option("--save", "--save_path", dest="save_path", action="store",
                      help="保存在Github的位置:", default=defalut_save_path)
    parser.add_option("--tree", "--tree_file_path", dest="tree_file_path", action="store",
                      help="目录树保存的文件名称:", default=defalut_tree_file_path)

    (options, args) = parser.parse_args()
    print('> 输入参数如下: \n', options)

    dirtree = DirectionTree(**options.__dict__)
    dirtree.generate_tree()
    dirtree.save_file()
    print((dirtree.tree))
    print((dirtree.href))
