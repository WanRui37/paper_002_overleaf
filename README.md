# Overleaf 同步工作区

已使用 Python 3.12 虚拟环境安装本地 overleaf-sync 2.0.1。

刷新四个项目的登录凭证：

```bash
cd /home/cambricon/Workspace/1-git_repository/paper_003_overleaf
python3 login_overleaf.py
./overleaf-sync list
```

进入任意项目目录同步，例如：

```bash
cd FlashNAS-BNN-IMAVIS_manuscript
../overleaf-sync       # 双向同步
../overleaf-sync -r    # 远端到本地
../overleaf-sync -l    # 本地到远端
../overleaf-sync download  # 下载编译 PDF
```

冲突时按提示选择；单向同步也可能提示删除。首次初始化采用远端到本地同步。
Cookie 从 `../paper_003/.env/.key/overleaf.env` 读取；凭证及同步状态已加入 Git 忽略规则。每个项目有 `.olignore`，保留 `.bbl` 和 PDF 图片。
