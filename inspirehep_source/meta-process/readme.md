# download.py 

单老师下载（debug强制重置）
python inspirehep_source/meta-process/download.py --teacher "曹庆宏+"  --force

通用下载
python inspirehep_source/meta-process/download.py 
更新元数据
python inspirehep_source/meta-process/download.py --teacher "曹庆宏"  --metadata-only

--only-main 仅下载原文

--force 强制重置

--method doi_source 强制降级

--retry 重新下载没有md的文章

--convert-only 只转md

# 其他工具

python tools/update_have_md.py

python tools/visualize_progress.py