> 🌏 **简体中文** | [English](https://github.com/Aider-AI/aider)
>
> 本仓库是 [Aider-AI/aider](https://github.com/Aider-AI/aider) 官方 README 的非官方简体中文翻译，仅供学习交流。
> 原项目采用 Apache-2.0 许可证，本翻译遵循相同许可证。翻译可能滞后于原文，请以[英文原版](https://github.com/Aider-AI/aider)为准。

<p align="center">
    <a href="https://aider.chat/"><img src="https://aider.chat/assets/logo.svg" alt="Aider Logo" width="300"></a>
</p>

<h1 align="center">
终端里的 AI 结对编程
</h1>


<p align="center">
Aider 让你与 LLM 结对编程，无论是从零开始一个新项目，还是在现有代码库上继续开发。
</p>

<p align="center">
  <img
    src="https://aider.chat/assets/screencast.svg"
    alt="aider screencast"
  >
</p>

<p align="center">
<!--[[[cog
from scripts.homepage import get_badges_md
text = get_badges_md()
cog.out(text)
]]]-->
  <a href="https://github.com/Aider-AI/aider/stargazers"><img alt="GitHub Stars" title="Total number of GitHub stars the Aider project has received"
src="https://img.shields.io/github/stars/Aider-AI/aider?style=flat-square&logo=github&color=f1c40f&labelColor=555555"/></a>
  <a href="https://pypi.org/project/aider-chat/"><img alt="PyPI Downloads" title="Total number of installations via pip from PyPI"
src="https://img.shields.io/badge/📦%20Installs-6.8M-2ecc71?style=flat-square&labelColor=555555"/></a>
  <img alt="Tokens per week" title="Number of tokens processed weekly by Aider users"
src="https://img.shields.io/badge/📈%20Tokens%2Fweek-15B-3498db?style=flat-square&labelColor=555555"/>
  <a href="https://openrouter.ai/#options-menu"><img alt="OpenRouter Ranking" title="Aider's ranking among applications on the OpenRouter platform"
src="https://img.shields.io/badge/🏆%20OpenRouter-Top%2020-9b59b6?style=flat-square&labelColor=555555"/></a>
  <a href="https://aider.chat/HISTORY.html"><img alt="Singularity" title="Percentage of the new code in Aider's last release written by Aider itself"
src="https://img.shields.io/badge/🔄%20Singularity-88%25-e74c3c?style=flat-square&labelColor=555555"/></a>
<!--[[[end]]]-->
</p>

## 功能特性

### [云端与本地 LLM](https://aider.chat/docs/llms.html)

<a href="https://aider.chat/docs/llms.html"><img src="https://aider.chat/assets/icons/brain.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
Aider 在 Claude 3.7 Sonnet、DeepSeek R1 & Chat V3、OpenAI o1、o3-mini 和 GPT-4o 上表现最佳，但几乎可以连接任何 LLM，包括本地模型。

<br>

### [代码库地图](https://aider.chat/docs/repomap.html)

<a href="https://aider.chat/docs/repomap.html"><img src="https://aider.chat/assets/icons/map-outline.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
Aider 会为你的整个代码库生成一张地图，这让它在大型项目中也能游刃有余。

<br>

### [支持 100+ 种编程语言](https://aider.chat/docs/languages.html)

<a href="https://aider.chat/docs/languages.html"><img src="https://aider.chat/assets/icons/code-tags.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
Aider 支持绝大多数流行的编程语言：python、javascript、rust、ruby、go、cpp、php、html、css，还有几十种更多。

<br>

### [Git 集成](https://aider.chat/docs/git.html)

<a href="https://aider.chat/docs/git.html"><img src="https://aider.chat/assets/icons/source-branch.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
Aider 会自动提交修改，并附上合理的提交信息。用你熟悉的 git 工具轻松 diff、管理和撤销 AI 的改动。

<br>

### [在 IDE 中使用](https://aider.chat/docs/usage/watch.html)

<a href="https://aider.chat/docs/usage/watch.html"><img src="https://aider.chat/assets/icons/monitor.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
在你喜欢的 IDE 或编辑器中使用 aider。在代码里加一条注释提出修改需求，aider 就会开工。

<br>

### [图片与网页](https://aider.chat/docs/usage/images-urls.html)

<a href="https://aider.chat/docs/usage/images-urls.html"><img src="https://aider.chat/assets/icons/image-multiple.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
把图片和网页加入对话，提供视觉上下文、截图、参考文档等。

<br>

### [语音编程](https://aider.chat/docs/usage/voice.html)

<a href="https://aider.chat/docs/usage/voice.html"><img src="https://aider.chat/assets/icons/microphone.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
直接跟 aider 聊你的代码！用语音提出新功能、测试用例或 bug 修复需求，让 aider 去实现改动。

<br>

### [代码检查与测试](https://aider.chat/docs/usage/lint-test.html)

<a href="https://aider.chat/docs/usage/lint-test.html"><img src="https://aider.chat/assets/icons/check-all.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
每次 aider 修改代码后自动做 lint 和测试。Aider 还能修复 linter 和测试套件发现的问题。

<br>

### [复制粘贴到网页对话](https://aider.chat/docs/usage/copypaste.html)

<a href="https://aider.chat/docs/usage/copypaste.html"><img src="https://aider.chat/assets/icons/content-copy.svg" width="32" height="32" align="left" valign="middle" style="margin-right:10px"></a>
通过网页对话界面使用任何 LLM。Aider 让代码上下文与修改在浏览器之间来回复制粘贴变得顺畅。

## 快速上手

```bash
python -m pip install aider-install
aider-install

# 进入你的代码库目录
cd /to/your/project

# DeepSeek
aider --model deepseek --api-key deepseek=<key>

# Claude 3.7 Sonnet
aider --model sonnet --api-key anthropic=<key>

# o3-mini
aider --model o3-mini --api-key openai=<key>
```

更多细节请参阅[安装指南](https://aider.chat/docs/install.html)与[使用文档](https://aider.chat/docs/usage.html)。

## 更多信息

### 文档
- [安装指南](https://aider.chat/docs/install.html)
- [使用指南](https://aider.chat/docs/usage.html)
- [视频教程](https://aider.chat/docs/usage/tutorials.html)
- [连接 LLM](https://aider.chat/docs/llms.html)
- [配置选项](https://aider.chat/docs/config.html)
- [故障排查](https://aider.chat/docs/troubleshooting.html)
- [常见问题](https://aider.chat/docs/faq.html)

### 社区与资源
- [LLM 排行榜](https://aider.chat/docs/leaderboards/)
- [GitHub 仓库](https://github.com/Aider-AI/aider)
- [Discord 社区](https://discord.gg/Y7X7bhMQFV)
- [发布说明](https://aider.chat/HISTORY.html)
- [博客](https://aider.chat/blog/)

## 用户评价

- *“我的生活彻底改变了……Aider……它会震撼你的世界。”* — [Eric S. Raymond on X](https://x.com/esrtweet/status/1910809356381413593)
- *“最好的免费开源 AI 编程助手。”* — [IndyDevDan on YouTube](https://youtu.be/YALpX8oOn78)
- *“迄今为止最好的 AI 编程助手。”* — [Matthew Berman on YouTube](https://www.youtube.com/watch?v=df8afeb1FY8)
- *“Aider 轻松让我的编码效率翻了四倍。”* — [SOLAR_FIELDS on Hacker News](https://news.ycombinator.com/item?id=36212100)
- *“很酷的工作流……Aider 的人体工学设计太适合我了。”* — [qup on Hacker News](https://news.ycombinator.com/item?id=38185326)
- *“就像有一位资深开发住进了你的 Git 仓库——太神奇了！”* — [rappster on GitHub](https://github.com/Aider-AI/aider/issues/124)
- *“多么惊人的工具，难以置信。”* — [valyagolev on GitHub](https://github.com/Aider-AI/aider/issues/6#issue-1722897858)
- *“Aider 真是个了不起的东西！”* — [cgrothaus on GitHub](https://github.com/Aider-AI/aider/issues/82#issuecomment-1631876700)
- *“它从零起步、做出前几个可用版本的速度，比我自己快太多了。”* — [Daniel Feldman on X](https://twitter.com/d_feldman/status/1662295077387923456)
- *“感谢 Aider！它真的让我瞥见了编程的未来。”* — [derwiki on Hacker News](https://news.ycombinator.com/item?id=38205643)
- *“太神奇了。它让我敢去做以前觉得超出能力范围的事。”* — [Dougie on Discord](https://discord.com/channels/1131200896827654144/1174002618058678323/1174084556257775656)
- *“这个项目太出色了。”* — [funkytaco on GitHub](https://github.com/Aider-AI/aider/issues/112#issuecomment-1637429008)
- *“惊人的项目，绝对是我用过最好的 AI 编程助手。”* — [joshuavial on GitHub](https://github.com/Aider-AI/aider/issues/84)
- *“我非常喜欢用 Aider……它让软件开发这件事感觉轻盈了许多。”* — [principalideal0 on Discord](https://discord.com/channels/1131200896827654144/1133421607499595858/1229689636012691468)
- *“我一直在从手术中恢复……aider 让我得以保持生产力。”* — [codeninja on Reddit](https://www.reddit.com/r/OpenAI/s/nmNwkHy1zG)
- *“我是 aider 重度用户。用更少的时间，完成了更多的工作。”* — [dandandan on Discord](https://discord.com/channels/1131200896827654144/1131200896827654149/1135913253483069470)
- *“Aider 毫无悬念地碾压其他一切工具，根本没有对手。”* — [SystemSculpt on Discord](https://discord.com/channels/1131200896827654144/1131200896827654149/1178736602797846548)
- *“Aider 很神奇，配上 Sonnet 3.5 简直令人震撼。”* — [Josh Dingus on Discord](https://discord.com/channels/1131200896827654144/1133060684540813372/1262374225298198548)
- *“毫无疑问，这是迄今为止最好的 AI 编程助手工具。”* — [IndyDevDan on YouTube](https://www.youtube.com/watch?v=MPYFPvxfGZs)
- *“[Aider] 改变了我的日常编码工作流。它能改变你的生活，这太不可思议了。”* — [maledorak on Discord](https://discord.com/channels/1131200896827654144/1131200896827654149/1258453375620747264)
- *“在现有代码库中做实际开发工作的最佳智能体。”* — [Nick Dobos on X](https://twitter.com/NickADobos/status/1690408967963652097?s=20)
- *“我最喜欢的软件之一，正在开辟新范式！”* — [Chris Wall on X](https://x.com/chris65536/status/1905053299251798432)
- *“Aider 对我和我的工作来说是革命性的。”* — [Starry Hope on X](https://x.com/starryhopeblog/status/1904985812137132056)
- *“试试 aider！氛围编程的最佳方式之一。”* — [Chris Wall on X](https://x.com/Chris65536/status/1905053418961391929)
- *“太爱 Aider 了。”* — [hztar on Hacker News](https://news.ycombinator.com/item?id=44035015)
- *“Aider 毫无疑问是最好的，而且免费开源。”* — [AriyaSavakaLurker on Reddit](https://www.reddit.com/r/ChatGPTCoding/comments/1ik16y6/whats_your_take_on_aider/mbip39n/)
- *“Aider 也是我最好的朋友。”* — [jzn21 on Reddit](https://www.reddit.com/r/ChatGPTCoding/comments/1heuvuo/aider_vs_cline_vs_windsurf_vs_cursor/m27dcnb/)
- *“试试 Aider，值得。”* — [jorgejhms on Reddit](https://www.reddit.com/r/ChatGPTCoding/comments/1heuvuo/aider_vs_cline_vs_windsurf_vs_cursor/m27cp99/)
- *“我喜欢 aider :)”* — [Chenwei Cui on X](https://x.com/ccui42/status/1904965344999145696)
- *“Aider 是 LLM 代码生成中的精密工具……极简、深思熟虑，能做外科手术式的精准修改……同时让开发者始终掌控全局。”* — [Reilly Sweetland on X](https://x.com/rsweetland/status/1904963807237259586)
- *“不敢相信 aider 今天一次就 vibe coding 出了一个横跨 service 和 cli 的 650 行功能。”* - [autopoietist on Discord](https://discord.com/channels/1131200896827654144/1131200896827654149/1355675042259796101)
- *“哦不，秘密藏不住了！没错，Aider 是最棒的编程工具，我强烈、强烈推荐给所有人。”* — [Joshua D Vander Hook on X](https://x.com/jodavaho/status/1911154899057795218)
- *“多亏了 aider，我在过去两天里启动并完成了三个个人项目”* — [joseph stalzyn on X](https://x.com/anitaheeder/status/1908338609645904160)
- *“把 aider 当主力工具用了一年多……我对这个工具的喜爱已经无法用言语表达。”* — [koleok on Discord](https://discord.com/channels/1131200896827654144/1273248471394291754/1356727448372252783)
- *“Aider……是衡量其他工具的标杆。”* — [BeetleB on Hacker News](https://news.ycombinator.com/item?id=43930201)
- *“aider 真的很酷”* — [kache on X](https://x.com/yacineMTB/status/1911224442430124387)
