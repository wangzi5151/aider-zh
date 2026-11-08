# 翻译同步 Checklist

本仓库是 [Aider-AI/aider](https://github.com/Aider-AI/aider) 官方 README 的**非官方**简体中文翻译，与上游项目及作者无隶属关系。英文原版始终是唯一权威来源。

## 维护基线

- 上游仓库：<https://github.com/Aider-AI/aider>
- 当前基线：`5dc9490bb35f9729ef2c95d00a19ccd30c26339c`
- 同步日期：2026-11-07
- 徽章数值（安装量 6.8M、Singularity 88%、每周 token 数、OpenRouter 排名）和模型清单均为上游 README 快照，可能已过期，不要当作实时数据。

## 每次同步

- [ ] 获取上游最新 README 与 commit：

  ```bash
  git ls-remote https://github.com/Aider-AI/aider.git HEAD
  curl -fsSL https://raw.githubusercontent.com/Aider-AI/aider/main/README.md -o /tmp/aider-upstream-README.md
  ```

- [ ] 对比上游与当前译文，同步章节、列表、表格、图片和链接。
- [ ] 检查徽章数值是否变化；变化时同步更新 `README.md`，并同步修改 `scripts/generate_badges.py` 中的快照常量。
- [ ] 检查模型清单、安装命令和功能描述是否过期；无法核实的内容保留快照标注，不虚构新版本。
- [ ] 更新 `README.md` 页首“维护基线”的 commit 与同步日期。
- [ ] 运行检查：

  ```bash
  python3 scripts/check_readme.py --external
  python3 scripts/generate_badges.py --check
  ```

- [ ] 确认没有提交与翻译无关的文件。
- [ ] 本地提交（除非维护者明确要求，不要 push）：

  ```bash
  git add README.md SYNC_CHECKLIST.md scripts/ .github/workflows/docs.yml
  git commit -m "docs: 同步上游 README（<short-sha>）"
  ```

## 翻译约定

- 保持原文结构；不翻译命令、路径、配置项、代码、URL 和许可证名称。
- 中文标点；中英文之间保留一个空格；不添加原文没有的结论或数据。
- 外部链接保留原地址；链接文字可以翻译。
- 上游数据无法核实时，明确标注“快照，可能已过期”。
- 一次提交只处理一个主题。
